# Active Context — longctx-bench-honest

## Current phase

**Phase 1 + Phase 2a + Phase 2b COMPLETE (2026-05-12). Phase 3 PR open.** Full constraint-optimized AI engineering portfolio thesis literal evidenced from 3 angles: Windows local 6GB VRAM ceiling, GitHub Models free-tier cloud accessibility map, and WSL2 vllm negative result. craftstack cross-repo integration PR [#70](https://github.com/leagames0221-sys/craftstack/pull/70) open pending CI green + user self-merge.

## Current focus

Session-end state. All major deliverables shipped. Awaiting:
1. craftstack PR #70 CI green + user self-merge (status: 10+ checks running, Vercel + Next.js builds typically 10-15 min)
2. (Optional, next session) r/LocalLLaMA + Hacker News post drafting after PR merged

## Completed Phase summary (★★★ tier evidence)

| Phase | Deliverable | Evidence |
|---|---|---|
| 0 | Scaffold + drift CI installed | commit dc5480b initial push |
| 1 partial | Windows transformers 4-cell scaling, 6GB VRAM ceiling characterized at 4k | 4 baseline_*.json + ADR-007 + commit bc9ae3d |
| 2a | Cloud comparison via GitHub Models free tier, 4 model probe, 6 cells | 6 cloud_*.json + ADR-008 + commit 01c4bc1 |
| 2b | WSL2 + vllm NEGATIVE RESULT — Linux/vllm cannot fit weights+activations on 6GB | wsl_vllm_4000.json + ADR-009 + commit e877718 |
| 3 (open) | craftstack PR #70 integration | [PR link](https://github.com/leagames0221-sys/craftstack/pull/70) |

## Aggregate counts (this PJ alone)

- **3 ADRs** (007, 008, 009) — all with citation chains
- **11 JSON evidence files** in `artifacts/`
- **3 runners**: baseline_niah.py / cloud_niah.py / wsl_vllm_niah.py
- **5-column cost-tier table** populated with literal cells + JSON URL citations
- **drift-CI 22+ steps** green on main HEAD ([commit 62e8818](https://github.com/leagames0221-sys/longctx-bench-honest/commit/62e8818))

## Cross-repo portfolio thesis (final form, ★★★★)

> **Constraint-optimized AI engineering** under (zero credit card, consumer laptop, public source / OSS only, drift-CI enforced):
>
> - **Local 6GB VRAM tier** — 4k context ceiling, rescued by Windows shared-mem PCIe spillover (ADR-007); Linux/vllm strict allocator fails (ADR-009)
> - **Cloud zero-CC tier** — gpt-4.1-mini + llama-3.3-70b reachable at 4k (~30-50x faster than local); gpt-5 unavailable; Anthropic Claude absent; some models capped at 4000 tokens (ADR-008)
> - **Cross-repo siblings**: craftstack (full-stack web $0/mo) + browser-agent-demo (5-layer defense-in-depth journey) + this repo (long-context measurement) = three domains, one thesis, all literal JSON / log evidence

## Next session candidates (Phase 4 — Optional)

1. **r/LocalLLaMA post drafting** — title candidate: "Honest map of 6GB VRAM consumer-laptop long-context limits: 4k local ceiling, cloud free-tier disparity, and the counterintuitive WSL2 vllm failure"
2. **Hacker News post drafting** — title candidate: "Show HN: constraint-optimized AI engineering portfolio with literal $0 + 11 JSON evidence cells + 3 ADRs"
3. **Heatmap visualization** — NIAH multi-depth × context heatmap PNG for the 4k cell (single depth currently; extend to 0/25/50/75/100% depths if 4k headroom permits)
4. **WebArena / OSWorld subset attempt** at 4k context using cloud cells (Phase 2a infrastructure already in place)
5. **Lifecycle cleanup decision** — when next-session AI confirms stable state, D: footprint (~20GB) is safe to delete per README Lifecycle section

## Blockers

なし。 craftstack PR #70 = user self-merge after CI green (technical only, no scope blocker).

## Out of scope (acknowledged limits)

- 真の 1M context inference (consumer 6GB tier 物理不可、 ADR-007 + 009 literal evidenced)
- paid API integration (zero CC 制約違反、 literal scope 外)
- 8 GPU server / workstation 級 hardware (D-CONSUMER-HW 違反)
- Anthropic Claude integration (literal absent from GitHub Models, requires paid Anthropic API)
- gpt-5 access (literal blocked on free tier per ADR-008)
