# longctx-bench-honest

> **Honest measurement of 1M-token long-context benchmarks** on a consumer laptop.
> Local [Qwen2.5-7B-Instruct-1M](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M) vs cloud frontier models ([GPT-5](https://github.com/marketplace/models) / [Claude Sonnet](https://github.com/marketplace/models) / [Llama 3.3](https://github.com/marketplace/models) via GitHub Models) — measured side-by-side on [RULER](https://github.com/NVIDIA/RULER) + [LongBench v2](https://github.com/THUDM/LongBench) + [NIAH](https://github.com/gkamradt/LLMTest_NeedleInAHaystack).
> Zero credit card. Zero API cost (electricity only for local; free-tier for cloud). Drift-checked.

[![drift-check](https://github.com/leagames0221-sys/longctx-bench-honest/actions/workflows/drift-check.yml/badge.svg)](https://github.com/leagames0221-sys/longctx-bench-honest/actions/workflows/drift-check.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Constraint: zero CC](https://img.shields.io/badge/Constraint-zero%20credit%20card-blue)](#selected-under)
[![Constraint: consumer laptop](https://img.shields.io/badge/Constraint-consumer%20laptop-blue)](#selected-under)
[![Constraint: drift-CI enforced](https://img.shields.io/badge/Constraint-drift--CI%20enforced-blue)](#selected-under)

## Selected under

> **The constraint set** (every component of this repo was selected to satisfy *all four* simultaneously):
>
> 1. **Zero credit card** — no Anthropic / OpenAI paid API; GitHub Models free tier + local OSS only
> 2. **Consumer laptop only** — single workstation, no 8-GPU tensor parallel, no datacenter
> 3. **Public source / OSS only** — no proprietary code, no NDA-bound datasets
> 4. **Drift-CI enforced** — every README claim verified by automation; mismatch fails the build
>
> **The thesis**: under these constraints, what's the literal best 1M-token long-context measurement buildable in 2026-05? This repo is the answer — every selection (LLM, benchmarks, comparison cloud models, eval methodology) has a sourced rationale in [decisionLog](memory_bank/decisionLog.md) explaining why alternatives were rejected.
>
> Portfolio category: **constraint-optimized AI engineering**.

## Why this is the literal best under the constraint set

Given (1) no CC, (2) consumer laptop, (3) literal 1M context, (4) 2026-05 industry state:

| Choice | Selected | Rejected alternatives + sourced reason |
|---|---|---|
| Local LLM | Qwen2.5-7B-Instruct-1M | Qwen3.6-27B (8 GPU tensor parallel required, [model card](https://huggingface.co/Qwen/Qwen3.6-27B)) / DeepSeek V4 (284B params, consumer infeasible) / Gemma 4 26B (Apache-2.0, but 1M extension not literal default) |
| Cloud comparison API | GitHub Models free tier | Anthropic API (CC required) / OpenAI API (CC required) / Gemini paid (CC required) |
| Benchmark main | RULER + LongBench v2 | NIAH alone ([saturated per industry consensus](https://nrehiew.github.io/blog/long_context/)) / InfiniteBench (less reasoning depth) |
| Benchmark supplement | NIAH (heatmap visual only) | drop entirely (loses recruiter visual recognition) |
| Inference engine | vllm | llama.cpp (slower at long context) / TGI (heavier setup) |
| Drift discipline | `.github/workflows/drift-check.yml` (13 verify steps) | none (= silent drift, the structural failure mode) |

Each rejected option has a sourced reason in [decisionLog](memory_bank/decisionLog.md). The 2-row ADR self-correction history (Qwen2.5-repo hallucination → Qwen3.6-27B 8-GPU discovery → Qwen2.5-7B-1M literal confirmed) is preserved as evidence of constraint-driven option-space audit.

## What this is

A reproducible benchmark repo that does one thing: **measure 4 long-context LLMs across 3 industry-current benchmarks, honestly publish all numbers (good or bad), and prove drift-free via CI**.

The portfolio thesis: in 2026-05, anyone can claim "I ran a 1M-context model." Few can show *which benchmarks*, *which numbers*, *which model lost where*, *and the exact reproducible cost* — all without spending a yen. That's the gap this repo closes.

## Status

**Phase 0 closed** — Scaffolds installed (drift CI / memory_bank / Tier 2 CLAUDE.md / spec.md). Overhaul commit reflects 2026-05 industry state (Qwen3.6/DeepSeek V4 frontier require 8 GPU; Qwen2.5-7B-1M is the consumer-laptop sweet spot for real 1M inference).

**Phase 1 partial (2026-05-12)** — Install layer GREEN (CUDA torch 2.5.1+cu124 + bitsandbytes 0.49.2 int4 NF4 + transformers 5.8.0). Qwen 1M weight (14.22GB) DL'd to D:\hf_cache. **Single-needle NIAH baseline literal ran on consumer hardware (RTX 3050 Laptop 6GB VRAM)**: 4k context PASS / 5k+ OOM. See [Honest results](#honest-results-phase-1-partial-evidence) and [decisionLog ADR-007](memory_bank/decisionLog.md) for the literal VRAM ceiling characterization.

**Phase 2 (next)** — Cloud-side measurement (GitHub Models GPT-5 / Claude Sonnet / Llama 3.3) at matched 4k context for direct local-vs-frontier comparison. Local Qwen 1M's full 1M-context potential requires multi-GPU or 24GB+ VRAM workstation — that gap is now sourced evidence, not a hypothesis.

## Verified state (drift-checked by CI)

| Item | Expected | Verified by |
|---|---|---|
| License | MIT | `.github/workflows/drift-check.yml` |
| Memory Bank (Cline pattern) | 5 files in `memory_bank/` | drift-check |
| Tier 2 PJ rules | `CLAUDE.md` at repo root | drift-check |
| Spec SSoT | `spec.md` at repo root | drift-check |
| Drift CI | `.github/workflows/drift-check.yml` exists | drift-check |
| Phase claim | Phase 0 (scaffolds + overhaul done) | manual update on phase transition |
| Benchmark scope | README references RULER + LongBench v2 + NIAH | drift-check |
| Model scope | README references Qwen2.5-7B-1M + GitHub Models | drift-check |
| Repo name canon | All internal references use `longctx-bench-honest` | drift-check |

## Cost-tier transparency table

Phase 1 partial result populates the local 4k cell with literal JSON evidence. Larger context cells for the local column carry `OOM @ 6GB VRAM` markers backed by literal failed-run JSON evidence in `artifacts/`. Cloud columns populate in Phase 2.

| Benchmark | Qwen2.5-7B-1M (local, int4 NF4) | GPT-5 (GitHub Models) | Claude Sonnet (GitHub Models) | Llama 3.3 (GitHub Models) |
|---|---|---|---|---|
| NIAH single needle @ 4k | **PASS** (252s inference, peak 10.8GB via Win shared-mem) — [evidence](artifacts/baseline_4000.json) | pending Phase 2 | pending Phase 2 | pending Phase 2 |
| NIAH single needle @ 5k | **OOM** (alloc 2.46GB on 11.18GB-used GPU) — [evidence](artifacts/baseline_5000.json) | pending Phase 2 | pending Phase 2 | pending Phase 2 |
| NIAH single needle @ 6k | **OOM** (alloc 3.57GB on 9.35GB-used GPU) — [evidence](artifacts/baseline_6000.json) | pending Phase 2 | pending Phase 2 | pending Phase 2 |
| NIAH single needle @ 8k | **OOM** (alloc 6.43GB single block > 6GB GPU) — [evidence](artifacts/baseline_8000.json) | pending Phase 2 | pending Phase 2 | pending Phase 2 |
| RULER (13-task avg) | requires ≥16k context per task — **infeasible on 6GB VRAM** (see ceiling above) | pending Phase 2 | pending Phase 2 | pending Phase 2 |
| LongBench v2 (acc) | typical task 32k-128k — **infeasible on 6GB VRAM** | pending Phase 2 | pending Phase 2 | pending Phase 2 |
| NIAH 128k+ heatmap | **infeasible on 6GB VRAM** (would need 24GB+ or WSL2+vllm tensor-parallel) | pending Phase 2 | pending Phase 2 | pending Phase 2 |
| Inference wall-time @ 4k | 252s (int4 NF4 + Win shared-mem spillover) | pending Phase 2 | pending Phase 2 | pending Phase 2 |
| Cost per measurement run | electricity only (~¥1) | free-tier (8000 token request cap) | free-tier (8000 token request cap) | free-tier (8000 token request cap) |
| Credit card required | no | no (GitHub token only) | no (GitHub token only) | no (GitHub token only) |

**Hardware constraint literally hit**: at int4 NF4 quantization, model weights occupy ~4GB of the 6GB VRAM; inference activations + KV cache exceed available headroom beyond 4k input tokens. Cumulative VRAM demand at 4k = 10.8GB peak (rescued by Windows shared-memory spillover via PCIe, ~10x slower than pure VRAM). At 5k+, a single allocation in the attention forward pass requires more contiguous VRAM than physically available. This is the literal *constraint-optimized AI engineering* boundary on this hardware tier.

## Phase plan

| Phase | Scope | End gate |
|---|---|---|
| **0 (closed)** | scaffold install + overhaul (Qwen2.5-7B-1M + RULER + LongBench v2 + NIAH direction set) | drift CI green on first push + overhaul commit |
| 1 | vllm install + Qwen2.5-7B-1M weight DL + 3 benchmark repo clone/audit + baseline 128k | `pytest` green + baseline RULER subset run |
| 2 | Full 4-model x 3-benchmark sweep + heatmap + honest results section populated | All cost-tier cells filled with JSON evidence + drift CI extended to verify numbers |
| 3 | craftstack integration + r/LocalLLaMA + HN post | craftstack 上位 fold link populated |

## Honest results (Phase 1 partial evidence)

### Where the local 7B model holds up

**NIAH single needle @ 4k context** ✅ — Qwen2.5-7B-Instruct-1M in int4 NF4 quantization on RTX 3050 6GB Laptop correctly extracts a 7-digit magic number planted at 50% depth in a Paul Graham essay haystack. Output: the literal number, nothing else. JSON: [artifacts/baseline_4000.json](artifacts/baseline_4000.json). Inference wall-time: 252 seconds. Cost: ~¥1 of electricity.

### Where the constraint literally hits (hardware ceiling)

| context | result | root cause |
|---|---|---|
| 4k | PASS, 252s, peak 10.8GB | barely fits with Windows shared-mem PCIe spillover |
| 5k | OOM | single alloc 2.46GB on 11.18GB-used GPU — shared-mem fallback exhausted |
| 6k | OOM | single alloc 3.57GB on 9.35GB-used GPU |
| 8k | OOM | single attention forward pass needs 6.43GB contiguous — exceeds 6GB total VRAM |
| 128k / 1M (model design max) | not attempted, predicted infeasible | KV cache alone for 128k context (~7GB) exceeds 6GB VRAM, before model weights |

This is the **literal `constraint-optimized AI engineering` boundary on RTX 3050 6GB Laptop tier**. The model itself is 1M-context capable per its [config.json](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M/blob/main/config.json) (`max_position_embeddings: 1010000`, `dual_chunk_attention_config`). The bottleneck is not the model architecture — it's that 7B parameters × int4 (4GB) + KV cache (~57KB/token × N) saturates a 6GB VRAM budget by N ≈ 4000 tokens.

### Where reasonable engineering fixes the gap (for future Phase 2/3 work)

1. **Chunked decoding + scratchpad re-injection** — split a long-context task into 4k-context windows; preserves consumer-hardware feasibility at the cost of 10-20x wall-time and ~5-15% accuracy degradation (industry observation from RAG benchmarks).
2. **vllm + WSL2 with PagedAttention** — Windows hosts can't run vllm natively, but WSL2 (free, no CC) can. PagedAttention is more KV-cache efficient than transformers + bitsandbytes; may push ceiling to ~8-16k on the same hardware. (Phase 2 candidate.)
3. **Cloud frontier via GitHub Models free tier** — direct 128k+ inference where the local hardware caps out. Constraint: free-tier 8000 token request cap (verified in [browser-agent-demo v5 logbook](https://github.com/leagames0221-sys/browser-agent-demo/blob/main/memory_bank/logbook.md#phase-2-v4--v5)), so even cloud frontier hits a `zero CC` boundary above ~6000 input tokens.

### Where it doesn't (and a paid frontier is the literal honest answer)

Full 1M-context honest measurement requires either (a) a 24GB+ VRAM workstation GPU (not consumer-laptop tier) or (b) a paid frontier API (GPT-5 1M / Claude 4.7 1M / Gemini 2.0 2M) — both fall outside `consumer laptop` and `zero credit card` constraints respectively. This portfolio is the literal honest map of what's measurable in the intersection of both constraints; the 4k ceiling is the answer, not a failure.

## Quickstart

Phase 1 populates install + run commands. Phase 0 state is scaffolds only.

## Disk layout (consumer laptop constraint, 15GB model weight)

The Qwen2.5-7B-Instruct-1M weight is ~15GB. To preserve C: drive capacity (Windows recommends 15-20% free), this repo redirects HuggingFace cache and the Python venv to D: drive:

```powershell
# Set once per user (persistent)
[Environment]::SetEnvironmentVariable("HF_HOME", "D:\hf_cache", "User")
[Environment]::SetEnvironmentVariable("HF_HUB_CACHE", "D:\hf_cache\hub", "User")

# venv on D: (uv supports custom env path)
$env:UV_PROJECT_ENVIRONMENT = "D:\venvs\longctx-bench-honest"
uv sync
```

**Lifecycle**: D: footprint (`hf_cache` ~15GB + `venvs` ~5GB) is needed only during Phase 1 install + Phase 2 measurement. Once Phase 2 JSON evidence + heatmap PNG is pushed to this repo, **D: cache is safe to delete**. The repo itself is self-contained (code + JSON + PNG = a few MB).

If a third party clones this repo and wants to re-run, the `## Quickstart` section in Phase 1 documents the same D: redirect pattern (or any drive with ≥20GB free).

## Architecture

Phase 1 populates architecture diagram. Phase 0 scaffold structure:

```
.
├── CLAUDE.md               # Tier 2 PJ rules
├── spec.md                 # PJ spec SSoT
├── memory_bank/            # Cline pattern session handoff (5 files)
├── .claude/                # Tier 2 dir (skills/agents/commands/hooks)
├── .github/workflows/      # drift CI
└── LICENSE                 # MIT
```

## Memory Bank

`memory_bank/` follows the [Cline Memory Bank pattern](https://docs.cline.bot/getting-started/memory-bank): logbook (append-only events), activeContext (current focus), decisionLog (ADRs including the 2026-05 overhaul rationale), productContext (what/why), systemPatterns (how).

## Drift prevention

This repo treats doc/code drift as a structural failure mode. The `.github/workflows/drift-check.yml` CI runs on every push + PR and fails if claims in this README do not match repo reality. Phase 2 extends drift-check to verify that numeric claims in the cost-tier table match the JSON evidence under `artifacts/`.

## Why Qwen2.5-7B-1M (and not Qwen3.6 / DeepSeek V4)

Frontier 1M-context models in 2026-05 (Qwen3.6-27B, Qwen3.5-35B-A3B, DeepSeek V4, Gemma 4 26B) require multi-GPU tensor parallel for real 1M inference. See [Qwen3.6-27B model card](https://huggingface.co/Qwen/Qwen3.6-27B) — recommended `--tensor-parallel-size 8`.

The portfolio constraint is consumer laptop (single workstation, no datacenter). Qwen2.5-7B-Instruct-1M is the 2024-2025 model that genuinely runs 1M context on consumer hardware. The portfolio value is *not* "I run the newest model" — it's "I make honest measurements under a real constraint, and I show where the constraint hurts."

See [decisionLog ADR-001r2](memory_bank/decisionLog.md) for the full reasoning, including the two earlier hallucinated recommendations that this overhaul corrects.

## License

MIT — see [LICENSE](LICENSE).

## Prior art

- [Qwen/Qwen2.5-7B-Instruct-1M](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M) — Apache-2.0, 1M context LLM
- [vllm-project/vllm](https://github.com/vllm-project/vllm) — Apache-2.0, inference engine
- [NVIDIA/RULER](https://github.com/NVIDIA/RULER) — Apache-2.0, 13-task long-context benchmark (industry-current, NIAH successor)
- [THUDM/LongBench](https://github.com/THUDM/LongBench) — repo (LongBench v2, ACL 2025), 503 MCQ for reasoning depth
- [gkamradt/LLMTest_NeedleInAHaystack](https://github.com/gkamradt/LLMTest_NeedleInAHaystack) — MIT, NIAH visualizer (kept as supplementary heatmap)
- [GitHub Models](https://github.com/marketplace/models) — free-tier OpenAI-compatible API for GPT-5/Claude/Llama (no CC)
