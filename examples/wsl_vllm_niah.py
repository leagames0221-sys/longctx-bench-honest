# SPDX-License-Identifier: MIT
# WSL2 + vllm PagedAttention NIAH runner — Phase 2b experiment
# Tests whether vllm's KV-cache-efficient attention (PagedAttention) can push
# the 6GB VRAM ceiling above the Windows transformers+bitsandbytes 4k limit.
"""
WSL2 vllm NIAH runner. Run inside WSL2 Ubuntu after `source .venv/bin/activate`.

Usage:
    python examples/wsl_vllm_niah.py --context-tokens 4000
    python examples/wsl_vllm_niah.py --context-tokens 8000
    python examples/wsl_vllm_niah.py --context-tokens 16000

Outputs: artifacts/wsl_vllm_<context>.json on the Windows side via /mnt/c path.
"""
import argparse
import gc
import json
import os
import random
import sys
import time
from pathlib import Path

import torch
from transformers import AutoTokenizer

# Path on /mnt/d (Windows D:) accessible from WSL2
MODEL_DIR = Path("/mnt/d/hf_cache/hub/models--Qwen--Qwen2.5-7B-Instruct-1M/snapshots/e28526f7bb80e2a9c8af03b831a9af3812f18fba")
ESSAY_DIR = Path("/mnt/c/Users/admin/projects/portfolio/longctx-bench-honest/eval/niah/needlehaystack/PaulGrahamEssays")
ARTIFACTS = Path("/mnt/c/Users/admin/projects/portfolio/longctx-bench-honest/artifacts")
ARTIFACTS.mkdir(exist_ok=True)


def load_haystack_text() -> str:
    return "\n\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in sorted(ESSAY_DIR.glob("*.txt")))


def build_prompt(tokenizer, haystack: str, target_tokens: int, needle: str, depth_pct: float):
    full_tokens = tokenizer.encode(haystack, add_special_tokens=False)
    if len(full_tokens) < target_tokens * 2:
        repeats = (target_tokens * 2 // len(full_tokens)) + 2
        full_tokens = full_tokens * repeats
    needle_tokens = tokenizer.encode(needle, add_special_tokens=False)
    overhead = 200 + len(needle_tokens)
    haystack_budget = max(target_tokens - overhead, 100)
    haystack_slice = full_tokens[:haystack_budget]
    insert_at = int(len(haystack_slice) * (depth_pct / 100.0))
    haystack_with_needle = haystack_slice[:insert_at] + needle_tokens + haystack_slice[insert_at:]
    haystack_text = tokenizer.decode(haystack_with_needle, skip_special_tokens=True)
    user_content = (
        f"{haystack_text}\n\n"
        f"What is the special magic number for portfolio-init mentioned in the text above? "
        f"Answer with only the number, nothing else."
    )
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Answer questions about the provided text."},
        {"role": "user", "content": user_content},
    ]
    rendered = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    actual = len(tokenizer.encode(rendered, add_special_tokens=False))
    return rendered, actual


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--context-tokens", type=int, required=True)
    parser.add_argument("--depth-pct", type=float, default=50.0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--max-new-tokens", type=int, default=64)
    parser.add_argument("--max-model-len", type=int, default=None, help="vllm max_model_len; defaults to context_tokens + 200")
    parser.add_argument("--gpu-mem-util", type=float, default=0.85)
    args = parser.parse_args()

    random.seed(args.seed)
    magic = random.randint(1_000_000, 9_999_999)
    needle = f"The special magic number for portfolio-init is: {magic}."
    max_model_len = args.max_model_len or (args.context_tokens + 200)

    result = {
        "schema_version": "1.0",
        "task": "niah_single",
        "runtime": "wsl2_vllm",
        "model": "Qwen/Qwen2.5-7B-Instruct-1M",
        "quantization": "bitsandbytes-int4",
        "vllm_version": "0.7.3",
        "context_tokens_target": args.context_tokens,
        "max_model_len": max_model_len,
        "gpu_memory_utilization": args.gpu_mem_util,
        "depth_pct": args.depth_pct,
        "seed": args.seed,
        "needle_value": str(magic),
        "host": {
            "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu",
            "vram_total_gb": round(torch.cuda.get_device_properties(0).total_memory / 1024**3, 2) if torch.cuda.is_available() else 0,
            "cuda_version": torch.version.cuda,
            "torch_version": torch.__version__,
        },
    }

    try:
        print(f"[1/5] Loading tokenizer", flush=True)
        tokenizer = AutoTokenizer.from_pretrained(str(MODEL_DIR))

        print(f"[2/5] Building prompt (target {args.context_tokens} tokens)", flush=True)
        haystack = load_haystack_text()
        prompt, actual_tokens = build_prompt(tokenizer, haystack, args.context_tokens, needle, args.depth_pct)
        result["context_tokens_actual"] = actual_tokens
        print(f"      actual tokens: {actual_tokens}", flush=True)

        print(f"[3/5] Loading model via vllm (bnb int4, max_model_len={max_model_len}, gpu_util={args.gpu_mem_util})", flush=True)
        from vllm import LLM, SamplingParams
        load_start = time.time()
        llm = LLM(
            model=str(MODEL_DIR),
            quantization="bitsandbytes",
            load_format="bitsandbytes",
            dtype="bfloat16",
            max_model_len=max_model_len,
            gpu_memory_utilization=args.gpu_mem_util,
            enforce_eager=True,
            trust_remote_code=False,
        )
        load_elapsed = time.time() - load_start
        result["model_load_sec"] = round(load_elapsed, 2)
        if torch.cuda.is_available():
            result["vram_after_model_load_gb"] = round(torch.cuda.memory_allocated() / 1024**3, 3)
        print(f"      loaded in {load_elapsed:.1f}s", flush=True)

        print(f"[4/5] Running inference", flush=True)
        sp = SamplingParams(temperature=0, max_tokens=args.max_new_tokens, seed=args.seed)
        if torch.cuda.is_available():
            torch.cuda.reset_peak_memory_stats()
        inf_start = time.time()
        outputs = llm.generate([prompt], sp)
        inf_elapsed = time.time() - inf_start
        output_text = outputs[0].outputs[0].text
        result["output_text"] = output_text
        result["inference_sec"] = round(inf_elapsed, 2)
        if torch.cuda.is_available():
            result["peak_vram_gb"] = round(torch.cuda.max_memory_allocated() / 1024**3, 3)

        found = str(magic) in output_text
        result["needle_found"] = found
        result["status"] = "PASS" if found else "FAIL"
        print(f"[5/5] Inference in {inf_elapsed:.2f}s, output: {output_text[:200]!r}", flush=True)
        print(f"      needle found: {found}", flush=True)

    except torch.cuda.OutOfMemoryError as e:
        result["status"] = "OOM"
        result["error"] = f"CUDA OOM at context {args.context_tokens}: {str(e)[:300]}"
        if torch.cuda.is_available():
            result["peak_vram_gb"] = round(torch.cuda.max_memory_allocated() / 1024**3, 3)
        print(f"OOM: {result['error']}", flush=True)
    except Exception as e:
        msg = str(e)
        if "out of memory" in msg.lower() or "OOM" in msg or "no available memory for the cache blocks" in msg.lower():
            result["status"] = "OOM"
        else:
            result["status"] = "ERROR"
        result["error"] = f"{type(e).__name__}: {msg[:500]}"
        print(f"{result['status']}: {result['error']}", flush=True)
    finally:
        out_path = ARTIFACTS / f"wsl_vllm_{args.context_tokens}.json"
        out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Evidence: {out_path}", flush=True)
        try:
            del llm
        except Exception:
            pass
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()


if __name__ == "__main__":
    main()
