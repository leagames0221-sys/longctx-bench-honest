# longctx-needle-demo

> Long-context (1M token) needle-in-a-haystack benchmark with local [Qwen2.5-7B-Instruct-1M](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M) vs [GitHub Models](https://github.com/marketplace/models) (GPT / Claude / Llama).
> Zero credit card required. Local-first + free-tier API fallback.

[![drift-check](https://github.com/leagames0221-sys/longctx-needle-demo/actions/workflows/drift-check.yml/badge.svg)](https://github.com/leagames0221-sys/longctx-needle-demo/actions/workflows/drift-check.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Status

**Phase 0** — Scaffolds installed (drift CI / memory_bank / Tier 2 CLAUDE.md / .gitignore / spec.md). Eval execution starts in Phase 1.

## Verified state (drift-checked by CI)

| Item | Expected | Verified by |
|---|---|---|
| License | MIT | `.github/workflows/drift-check.yml` |
| Memory Bank (Cline pattern) | 5 files in `memory_bank/` | drift-check |
| Tier 2 PJ rules | `CLAUDE.md` at repo root | drift-check |
| Spec SSoT | `spec.md` at repo root | drift-check |
| Drift CI | `.github/workflows/drift-check.yml` exists | drift-check |
| Phase claim | Phase 0 (scaffolds only) | manual update on phase transition |

## Phase plan

| Phase | Scope | End gate |
|---|---|---|
| **0 (done)** | scaffold install | drift CI green on first push |
| 1 | vllm + Qwen2.5-1M weight DL + Needle-in-a-Haystack clone + baseline run | `pytest` green、 baseline heatmap output |
| 2 | 4 context size (128k/256k/512k/1M) × 4 model (Qwen local + GPT-5/Claude/Llama via GitHub Models) | 4 heatmap PNG + 比較 table + 30s 動画 |
| 3 | craftstack integration + r/LocalLLaMA + HN literal post | craftstack 上位 fold link populated |

## Quickstart

Phase 1 populates install + run commands. Current Phase 0 state has no runtime code.

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

`memory_bank/` follows the [Cline Memory Bank pattern](https://docs.cline.bot/getting-started/memory-bank): logbook (append-only events), activeContext (current focus), decisionLog (ADRs), productContext (what/why), systemPatterns (how).

## Drift prevention

This repo treats doc/code drift as a structural failure mode. The `.github/workflows/drift-check.yml` CI runs on every push + PR and fails if claims in this README do not match repo reality.

## Honest caveat

Real 1M context inference on consumer laptop hardware is bounded by VRAM and time. Phase 2 measurements (時間 / メモリ / 正答率) are reported as-measured; if 1M context inference is literally infeasible in reasonable time (>24h), the failure analysis itself is part of the portfolio deliverable. Design includes literal 1M; only implementation-phase verified infeasibility triggers refactor (D-NO-COMPROMISE-IN-DESIGN).

## License

MIT — see [LICENSE](LICENSE).

## Prior art

- [Qwen/Qwen2.5-7B-Instruct-1M](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M) — Apache-2.0, 1M context LLM
- [vllm-project/vllm](https://github.com/vllm-project/vllm) — Apache-2.0, inference engine
- [gkamradt/LLMTest_NeedleInAHaystack](https://github.com/gkamradt/LLMTest_NeedleInAHaystack) — MIT, eval harness
- [GitHub Models](https://github.com/marketplace/models) — free-tier API for GPT/Claude/Llama (no CC)
