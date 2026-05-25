# Active Context — longctx-bench-honest

## Current phase

**Phase 1 + 2a + 2b + 3 + post-audit fix + distribution-on-Dev.to COMPLETE (2026-05-12).** craftstack PR #70 literal merged + main HEAD has "Related portfolio work" cross-link. **Dev.to article PUBLISHED**: https://dev.to/leagames0221sys/counterintuitive-wsl2-vllm-cannot-fit-qwen25-7b-1m-on-6gb-vram-where-windows-transformers-can-597b (HTTP 200 verified, 4 tags, full 3-finding narrative). r/LocalLLaMA + HN Show HN pending 1-2 weeks karma building.

## Aggregate deliverable state

| # | Item | Evidence |
|---|---|---|
| 1 | longctx-bench-honest main HEAD | [commit 46a5a8c](https://github.com/leagames0221-sys/longctx-bench-honest/commit/46a5a8c), drift-CI 22+ steps green |
| 2 | 11 JSON evidence files | `artifacts/baseline_{4000,5000,6000,8000}.json` + `artifacts/cloud_*_{2000,4000}.json` (6 cloud) + `artifacts/wsl_vllm_4000.json` |
| 3 | 3 runners | `examples/baseline_niah.py` (Win transformers) + `cloud_niah.py` (GitHub Models) + `wsl_vllm_niah.py` (WSL2 vllm) |
| 4 | 3 ADRs | ADR-007 (6GB VRAM ceiling) + ADR-008 (cloud free-tier honest map) + ADR-009 (WSL2 vllm hypothesis + 3 alternatives + falsification path) |
| 5 | README cost-tier table | 5-col × 10-row matrix with ✅/❌/⏳/⛔ icon legend + sample-size disclosure + cold-load footnote |
| 6 | Honest results section | 4 subsections (holds up / constraint hits / engineering fix / paid frontier honest answer) |
| 7 | Cloud free-tier honest map section | accessibility matrix: Claude absent / gpt-5 unavailable / 4000-token cap pattern |
| 8 | pyproject.toml + uv.lock | exact version pinning (torch==2.5.1 / bitsandbytes==0.49.2 / vllm==0.7.3) matching JSON evidence literal — `uv sync` reproduces measurement environment |
| 9 | drift-CI workflow | 22+ verify steps, all green on every push since Phase 0 |
| 10 | craftstack PR #70 merged | "Related portfolio work" section live on craftstack main HEAD [commit 0b830b9](https://github.com/leagames0221-sys/craftstack/commit/0b830b9) |
| 11 | Social distribution drafts | `memory_bank/social_drafts.md` — r/LocalLLaMA + HN post body + first comment |

## Post-audit fix history

| Fix | Effect |
|---|---|
| #1 reproducibility | pyproject.toml drift fixed; `uv sync` now produces measurement-matching versions |
| #2 ADR-009 honesty tier | overclaim → hypothesis + 3 alternatives + falsification path |
| #3 cost-tier visual icons | ✅/❌/⏳/⛔ legend separates measured from predicted; sample-size + cold-load disclosed |
| #7 memory bank drift | productContext + systemPatterns reflect actual Phase 2a/b delivery, not Phase 0 dream |

## Next session candidates

**2026-05-12 distribution attempt result**: Both Reddit r/LocalLLaMA and HN Show HN have **structural anti-new-account gates** that block immediate posting:
- r/LocalLLaMA: auto-mod removed post within 1 minute of submit (account too new / low karma)
- HN: Show HN explicitly restricted for new accounts per HN's anti-influx page ("become a good contributor, then post an occasional Show HN")

→ Distribution today is **structurally gated**, not a content failure. Pushing more aggressively risks shadow-ban accumulation.

**Recommended path: Karma building → re-attempt distribution in 1-2 weeks**

Rationale:
- Both gates require account standing (5-10 substantive comments + 7+ days age), unavoidable
- GitHub topic tags added today (passive discoverability boost via native search, zero account requirement)
- LinkedIn would bypass these gates but no account exists; account creation = 30-60 min commitment, deferred decision
- 1-2 weeks of comment activity on others' HN/Reddit threads is the literal cheapest path to unblock both channels

**Cadence**:
1. Day 1-7: Post substantive technical comments on HN front-page threads relevant to LLM / consumer-hardware / benchmarks (1-2/day). Target ~5-10 karma + 7+ days account age.
2. Day 8-10: Same in r/LocalLLaMA on others' threads. Target ~5 sub-karma.
3. Day 11+: Re-attempt HN Show HN + r/LocalLLaMA post with the same drafts in `memory_bank/social_drafts.md`.
4. Respond to comments in 30-60 min window after each post lands.

**Alternative immediate distribution**:
- LinkedIn account create (30-60 min) + portfolio announcement post
- Direct contact to known recruiters with craftstack URL (the 1 URL surfaces all 3 repos)

**Lower-priority alternatives (Phase 4 deep-work)**:
- ADR-009 falsification experiments (4 zero-CC steps to promote hypothesis → causal claim)
- Multi-depth NIAH heatmap @ 4k (5 depths × 3 seeds ≈ 30 min, generates 1 PNG)
- New portfolio repo #5/#6 (high effort, low marginal ROI until existing 3 saturate)

## Blockers

None. Distribution is a 5-min click gating step, no automation needed. Submit timing (Tue-Thu US morning is HN/Reddit optimal), then feedback response next cycle.

## Out of scope (acknowledged limits, ADR-citation 済)

- 真の 1M context inference (consumer 6GB tier 物理不可、 ADR-007 + 009)
- paid API integration (zero CC 制約違反)
- Anthropic Claude (GitHub Models catalog literal 不在、 ADR-008)
- gpt-5 free-tier access (UNAVAILABLE、 ADR-008)
- WSL2 11GB cleanup (portfolio 機能には literal 影響なし)
