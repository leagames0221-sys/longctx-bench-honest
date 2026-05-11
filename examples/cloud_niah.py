# SPDX-License-Identifier: MIT
# Cloud NIAH runner: same single-needle task as baseline_niah.py, run against
# GitHub Models free-tier endpoint (zero credit card, GitHub OAuth token only).
#
# Decomposed prior art:
#   - examples/baseline_niah.py (this repo) — haystack + needle pattern
#   - OpenAI Python SDK (openai>=1.50) — OpenAI-compatible chat completions API
#   - GitHub Models inference endpoint: https://models.github.ai/inference
"""
Cloud single-needle NIAH runner against GitHub Models.

Usage:
    python examples/cloud_niah.py --model openai/gpt-4.1-mini --context-tokens 4000
    python examples/cloud_niah.py --model openai/gpt-5 --context-tokens 4000
    python examples/cloud_niah.py --model meta/llama-3.3-70b-instruct --context-tokens 4000

Outputs: artifacts/cloud_<model_slug>_<context>.json with literal numeric evidence.
"""
import argparse
import json
import os
import random
import re
import subprocess
import time
from pathlib import Path

from openai import OpenAI
from transformers import AutoTokenizer

REPO_ROOT = Path(__file__).resolve().parent.parent
ESSAY_DIR = REPO_ROOT / "eval" / "niah" / "needlehaystack" / "PaulGrahamEssays"
MODEL_DIR = Path(r"D:\hf_cache\hub\models--Qwen--Qwen2.5-7B-Instruct-1M\snapshots\e28526f7bb80e2a9c8af03b831a9af3812f18fba")
ARTIFACTS = REPO_ROOT / "artifacts"
ARTIFACTS.mkdir(exist_ok=True)


def get_github_token() -> str:
    """Read token from env first, then fall back to gh CLI."""
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token
    try:
        result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10, check=True)
        return result.stdout.strip()
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError) as e:
        raise RuntimeError(f"Cannot get GitHub token: {e}. Set GITHUB_TOKEN env or run `gh auth login`.")


def load_haystack_text() -> str:
    return "\n\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in sorted(ESSAY_DIR.glob("*.txt")))


def build_prompt_messages(tokenizer, haystack: str, target_tokens: int, needle: str, depth_pct: float) -> tuple[list, int]:
    """Build chat messages matching baseline_niah.py prompt structure.

    Returns (messages_list, approx_input_tokens). We use Qwen tokenizer to
    target a comparable token budget — actual cloud tokenizer may differ slightly.
    """
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
    # Approximate token count via the rendered chat template for comparability
    rendered = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    approx_tokens = len(tokenizer.encode(rendered, add_special_tokens=False))
    return messages, approx_tokens


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, help="GitHub Models id (e.g. openai/gpt-4.1-mini)")
    parser.add_argument("--context-tokens", type=int, required=True)
    parser.add_argument("--depth-pct", type=float, default=50.0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--max-new-tokens", type=int, default=64)
    args = parser.parse_args()

    random.seed(args.seed)
    magic_number = random.randint(1_000_000, 9_999_999)
    needle = f"The special magic number for portfolio-init is: {magic_number}."

    model_slug = re.sub(r"[^a-z0-9]+", "-", args.model.lower()).strip("-")

    result = {
        "schema_version": "1.0",
        "task": "niah_single",
        "provider": "github_models",
        "endpoint": "https://models.github.ai/inference",
        "model": args.model,
        "context_tokens_target": args.context_tokens,
        "depth_pct": args.depth_pct,
        "seed": args.seed,
        "needle_value": str(magic_number),
        "haystack_source": "PaulGrahamEssays (49 essays, repeated as needed)",
        "tokenizer_used_for_budget": "Qwen/Qwen2.5-7B-Instruct-1M (approximation, cloud may differ)",
    }

    try:
        print(f"[1/4] Loading Qwen tokenizer for token-budget approximation", flush=True)
        tokenizer = AutoTokenizer.from_pretrained(str(MODEL_DIR))

        print(f"[2/4] Building haystack + prompt (target {args.context_tokens} tokens, depth {args.depth_pct}%)", flush=True)
        haystack = load_haystack_text()
        messages, approx_tokens = build_prompt_messages(tokenizer, haystack, args.context_tokens, needle, args.depth_pct)
        result["context_tokens_approx"] = approx_tokens
        print(f"      approx tokens (Qwen tokenizer): {approx_tokens}", flush=True)

        print(f"[3/4] Calling GitHub Models endpoint for model: {args.model}", flush=True)
        client = OpenAI(base_url="https://models.github.ai/inference", api_key=get_github_token())
        start = time.time()
        response = client.chat.completions.create(
            model=args.model,
            messages=messages,
            max_completion_tokens=args.max_new_tokens,
            temperature=0,
            seed=args.seed,
        )
        elapsed = time.time() - start
        output_text = response.choices[0].message.content or ""
        result["output_text"] = output_text
        result["inference_sec"] = round(elapsed, 2)
        result["usage_prompt_tokens"] = response.usage.prompt_tokens if response.usage else None
        result["usage_completion_tokens"] = response.usage.completion_tokens if response.usage else None
        result["finish_reason"] = response.choices[0].finish_reason

        found = str(magic_number) in output_text
        result["needle_found"] = found
        result["status"] = "PASS" if found else "FAIL"
        print(f"[4/4] Inference done in {elapsed:.2f}s", flush=True)
        print(f"      output: {output_text[:200]!r}", flush=True)
        print(f"      usage: prompt={result['usage_prompt_tokens']}, completion={result['usage_completion_tokens']}", flush=True)
        print(f"      needle found: {found}", flush=True)

    except Exception as e:
        # Distinguish rate-limit / token-cap / auth from logic errors
        msg = str(e)
        if "rate limit" in msg.lower() or "429" in msg:
            result["status"] = "RATE_LIMIT"
        elif "token" in msg.lower() and ("limit" in msg.lower() or "exceed" in msg.lower() or "context_length" in msg.lower()):
            result["status"] = "TOKEN_LIMIT"
        elif "401" in msg or "403" in msg or "auth" in msg.lower():
            result["status"] = "AUTH_ERROR"
        else:
            result["status"] = "ERROR"
        result["error"] = f"{type(e).__name__}: {msg[:500]}"
        print(f"ERROR ({result['status']}): {result['error']}", flush=True)
    finally:
        out_path = ARTIFACTS / f"cloud_{model_slug}_{args.context_tokens}.json"
        out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Evidence: {out_path}", flush=True)


if __name__ == "__main__":
    main()
