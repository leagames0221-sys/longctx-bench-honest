# SPDX-License-Identifier: MIT
# Decomposed prior art (D-PRIOR-ART-FIRST):
#   - NIAH pattern: gkamradt/LLMTest_NeedleInAHaystack (MIT) — needle insertion + retrieval Q
#   - Haystack source: Paul Graham essays from same repo (eval/niah/needlehaystack/PaulGrahamEssays/)
#   - RULER niah.py template (NVIDIA/RULER, Apache 2.0) — query/answer format
# Lightweight self-contained runner: HF transformers + bitsandbytes int4 quant on RTX 3050 6GB.
"""
Single-needle NIAH baseline runner for Qwen2.5-7B-Instruct-1M.

Usage:
    python examples/baseline_niah.py --context-tokens 4000 --depth-pct 50
    python examples/baseline_niah.py --context-tokens 8000
    python examples/baseline_niah.py --context-tokens 16000

Outputs: artifacts/baseline_<context>.json with literal numeric evidence.
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
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

REPO_ROOT = Path(__file__).resolve().parent.parent
ESSAY_DIR = REPO_ROOT / "eval" / "niah" / "needlehaystack" / "PaulGrahamEssays"
MODEL_DIR = Path(r"D:\hf_cache\hub\models--Qwen--Qwen2.5-7B-Instruct-1M\snapshots\e28526f7bb80e2a9c8af03b831a9af3812f18fba")
ARTIFACTS = REPO_ROOT / "artifacts"
ARTIFACTS.mkdir(exist_ok=True)


def load_haystack_text() -> str:
    """Load Paul Graham essays as haystack source (concatenate all 49 essays)."""
    parts = []
    for p in sorted(ESSAY_DIR.glob("*.txt")):
        parts.append(p.read_text(encoding="utf-8", errors="ignore"))
    return "\n\n".join(parts)


def build_prompt(tokenizer, haystack: str, target_tokens: int, needle: str, depth_pct: float) -> tuple[str, int]:
    """Build a chat-template prompt at the requested token count with needle at depth_pct.

    Returns (rendered_prompt_str, actual_input_token_count).
    """
    # Tokenize the entire haystack once; slice to target size, insert needle at depth.
    full_tokens = tokenizer.encode(haystack, add_special_tokens=False)
    if len(full_tokens) < target_tokens * 2:
        # Repeat haystack as needed
        repeats = (target_tokens * 2 // len(full_tokens)) + 2
        full_tokens = full_tokens * repeats

    needle_tokens = tokenizer.encode(needle, add_special_tokens=False)

    # Reserve room for system + question + needle + generation budget (~200 tokens overhead)
    overhead = 200 + len(needle_tokens)
    haystack_budget = target_tokens - overhead
    if haystack_budget < 100:
        haystack_budget = 100
    haystack_slice = full_tokens[:haystack_budget]

    # Insert needle at depth_pct
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
    actual_tokens = len(tokenizer.encode(rendered, add_special_tokens=False))
    return rendered, actual_tokens


def run_inference(model, tokenizer, prompt: str, max_new_tokens: int = 64) -> tuple[str, float, int]:
    """Run inference, return (output_text, elapsed_sec, peak_vram_gb)."""
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    torch.cuda.reset_peak_memory_stats()
    start = time.time()
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            temperature=1.0,
            top_p=1.0,
            pad_token_id=tokenizer.eos_token_id,
        )
    elapsed = time.time() - start
    output_tokens = outputs[0][inputs["input_ids"].shape[1]:]
    output_text = tokenizer.decode(output_tokens, skip_special_tokens=True)
    peak_vram = torch.cuda.max_memory_allocated() / 1024**3
    return output_text, elapsed, peak_vram


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--context-tokens", type=int, required=True, help="Target input token count")
    parser.add_argument("--depth-pct", type=float, default=50.0, help="Needle depth in haystack (0-100)")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--max-new-tokens", type=int, default=64)
    args = parser.parse_args()

    random.seed(args.seed)
    torch.manual_seed(args.seed)

    # Generate a fixed-but-pseudo-random 7-digit magic number from seed
    magic_number = random.randint(1_000_000, 9_999_999)
    needle = f"The special magic number for portfolio-init is: {magic_number}."

    result = {
        "schema_version": "1.0",
        "task": "niah_single",
        "model": "Qwen/Qwen2.5-7B-Instruct-1M",
        "quantization": "int4-nf4-bnb",
        "context_tokens_target": args.context_tokens,
        "depth_pct": args.depth_pct,
        "seed": args.seed,
        "needle_value": str(magic_number),
        "haystack_source": "PaulGrahamEssays (49 essays, repeated as needed)",
        "host": {
            "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu",
            "vram_total_gb": round(torch.cuda.get_device_properties(0).total_memory / 1024**3, 2) if torch.cuda.is_available() else 0,
            "cuda_version": torch.version.cuda,
            "torch_version": torch.__version__,
        },
    }

    try:
        print(f"[1/5] Loading tokenizer from {MODEL_DIR}", flush=True)
        tokenizer = AutoTokenizer.from_pretrained(str(MODEL_DIR))

        print(f"[2/5] Building haystack + prompt (target {args.context_tokens} tokens, depth {args.depth_pct}%)", flush=True)
        haystack = load_haystack_text()
        prompt, actual_tokens = build_prompt(tokenizer, haystack, args.context_tokens, needle, args.depth_pct)
        result["context_tokens_actual"] = actual_tokens
        print(f"      actual tokens: {actual_tokens}", flush=True)

        print(f"[3/5] Loading model with int4 NF4 quant (this loads ~4GB to VRAM)", flush=True)
        bnb_cfg = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
        )
        load_start = time.time()
        # Force GPU-only placement: 6GB total, ~1GB reserved by display/OS, leave 5GB max.
        # If int4 model + activations exceeds this, OOM at load = honest VRAM ceiling evidence.
        model = AutoModelForCausalLM.from_pretrained(
            str(MODEL_DIR),
            quantization_config=bnb_cfg,
            device_map={"": 0},
            torch_dtype=torch.bfloat16,
        )
        model.eval()
        load_elapsed = time.time() - load_start
        result["model_load_sec"] = round(load_elapsed, 2)
        vram_after_load = torch.cuda.memory_allocated() / 1024**3
        result["vram_after_model_load_gb"] = round(vram_after_load, 3)
        print(f"      loaded in {load_elapsed:.1f}s, VRAM in use: {vram_after_load:.2f}GB", flush=True)

        print(f"[4/5] Running inference (max_new_tokens={args.max_new_tokens})", flush=True)
        output_text, inference_elapsed, peak_vram = run_inference(model, tokenizer, prompt, args.max_new_tokens)
        result["output_text"] = output_text
        result["inference_sec"] = round(inference_elapsed, 2)
        result["peak_vram_gb"] = round(peak_vram, 3)

        # Evaluation: did the model output contain the magic number?
        found = str(magic_number) in output_text
        result["needle_found"] = found
        result["status"] = "PASS" if found else "FAIL"
        print(f"[5/5] Inference done in {inference_elapsed:.1f}s, peak VRAM {peak_vram:.2f}GB", flush=True)
        print(f"      output: {output_text[:200]!r}", flush=True)
        print(f"      needle found: {found}", flush=True)

    except torch.cuda.OutOfMemoryError as e:
        result["status"] = "OOM"
        result["error"] = f"CUDA out of memory at context_tokens={args.context_tokens}: {e}"
        result["peak_vram_gb"] = round(torch.cuda.max_memory_allocated() / 1024**3, 3) if torch.cuda.is_available() else 0
        print(f"OOM at context {args.context_tokens}: {e}", flush=True)
    except Exception as e:
        result["status"] = "ERROR"
        result["error"] = f"{type(e).__name__}: {e}"
        print(f"ERROR: {result['error']}", flush=True)
    finally:
        # Save evidence regardless of outcome
        out_path = ARTIFACTS / f"baseline_{args.context_tokens}.json"
        out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Evidence: {out_path}", flush=True)
        # Free VRAM
        try:
            del model
        except Exception:
            pass
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()


if __name__ == "__main__":
    main()
