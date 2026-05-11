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

**Phase 1 (next)** — vllm install + Qwen2.5-7B-1M weight DL + RULER/LongBench v2/NIAH clone + audit + baseline 128k run.

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

This is the table Phase 2 populates. Phase 0/1 columns carry `pending Phase 2` markers so the CI can verify the table structure even before numbers exist.

| Benchmark | Qwen2.5-7B-1M (local) | GPT-5 (GitHub Models) | Claude Sonnet (GitHub Models) | Llama 3.3 (GitHub Models) |
|---|---|---|---|---|
| RULER (13-task avg) | pending Phase 2 | pending Phase 2 | pending Phase 2 | pending Phase 2 |
| LongBench v2 (acc) | pending Phase 2 | pending Phase 2 | pending Phase 2 | pending Phase 2 |
| NIAH (1M heatmap mean) | pending Phase 2 | pending Phase 2 | pending Phase 2 | pending Phase 2 |
| Sec per 1M-token eval | pending Phase 2 | pending Phase 2 | pending Phase 2 | pending Phase 2 |
| Cost per full sweep | electricity only | free-tier | free-tier | free-tier |
| Credit card required | no | no (GitHub token only) | no (GitHub token only) | no (GitHub token only) |

## Phase plan

| Phase | Scope | End gate |
|---|---|---|
| **0 (closed)** | scaffold install + overhaul (Qwen2.5-7B-1M + RULER + LongBench v2 + NIAH direction set) | drift CI green on first push + overhaul commit |
| 1 | vllm install + Qwen2.5-7B-1M weight DL + 3 benchmark repo clone/audit + baseline 128k | `pytest` green + baseline RULER subset run |
| 2 | Full 4-model x 3-benchmark sweep + heatmap + honest results section populated | All cost-tier cells filled with JSON evidence + drift CI extended to verify numbers |
| 3 | craftstack integration + r/LocalLLaMA + HN post | craftstack 上位 fold link populated |

## Honest results (populated in Phase 2)

Phase 2 fills this section with full results — including **failures**. If Qwen2.5-7B-1M scores 22% on RULER multi-hop, that 22% goes here, with the failure-mode analysis. If 1M context inference on consumer laptop takes 47 minutes per query, that 47 minutes goes here. The portfolio thesis depends on this section being unflinching.

Expected categories:
- `Where the local 7B model holds up`: tasks where Qwen2.5-7B-1M is within 10% of frontier
- `Where it loses badly`: tasks where the gap is > 30%, with hypothesized root cause
- `Where reasonable engineering fixes the gap`: e.g., chunking + re-ranking, RAG augmentation
- `Where it doesn't (and frontier is the right answer)`: honest "use the API" recommendation

## Quickstart

Phase 1 populates install + run commands. Phase 0 state is scaffolds only.

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
