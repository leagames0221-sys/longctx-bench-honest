# Active Context — longctx-bench-honest

## Current phase

**Phase 1 + 2a + 2b + 3 + post-audit fix COMPLETE (2026-05-12).** Portfolio is at ★★★ tier (post-self-audit + 4 fix). craftstack PR #70 literal merged + main HEAD has "Related portfolio work" cross-link. Social distribution drafts ready in `memory_bank/social_drafts.md`. Next session = distribution (r/LocalLLaMA + HN post) is the highest-ROI move; new portfolio breadth (#5 / #6) is lower priority until distribution generates signal.

## Aggregate deliverable state (post-audit, ★★★ tier)

| # | Item | Evidence |
|---|---|---|
| 1 | longctx-bench-honest main HEAD | [commit 46a5a8c](https://github.com/leagames0221-sys/longctx-bench-honest/commit/46a5a8c), drift-CI 22+ steps green |
| 2 | 11 JSON evidence files | `artifacts/baseline_{4000,5000,6000,8000}.json` + `artifacts/cloud_*_{2000,4000}.json` (6 cloud) + `artifacts/wsl_vllm_4000.json` |
| 3 | 3 runners | `examples/baseline_niah.py` (Win transformers) + `cloud_niah.py` (GitHub Models) + `wsl_vllm_niah.py` (WSL2 vllm) |
| 4 | 3 ADRs | ADR-007 (6GB VRAM ceiling) + ADR-008 (cloud free-tier honest map) + ADR-009 (WSL2 vllm ★★ hypothesis + 3 alternatives + falsification path) |
| 5 | README cost-tier table | 5-col × 10-row matrix with ✅/❌/⏳/⛔ icon legend + sample-size disclosure + cold-load footnote |
| 6 | Honest results section | 4 subsections (holds up / constraint hits / engineering fix / paid frontier honest answer) |
| 7 | Cloud free-tier honest map section | accessibility matrix: Claude absent / gpt-5 unavailable / 4000-token cap pattern |
| 8 | pyproject.toml + uv.lock | exact version pinning (torch==2.5.1 / bitsandbytes==0.49.2 / vllm==0.7.3) matching JSON evidence literal — `uv sync` reproduces measurement environment |
| 9 | drift-CI workflow | 22+ verify steps, all green on every push since Phase 0 |
| 10 | craftstack PR #70 merged | "Related portfolio work" section live on craftstack main HEAD [commit 0b830b9](https://github.com/leagames0221-sys/craftstack/commit/0b830b9) |
| 11 | Social distribution drafts | `memory_bank/social_drafts.md` — r/LocalLLaMA + HN post body + first comment, ready for user submit |

## Post-audit fix history (self-correction signal)

| Fix | Tier | Effect |
|---|---|---|
| #1 reproducibility | ★★★ | pyproject.toml drift fixed; `uv sync` now produces measurement-matching versions |
| #2 ADR-009 honesty tier | ★★ | ★★★★ overclaim → ★★ hypothesis + 3 alternatives + falsification path |
| #3 cost-tier visual icons | ★★ | ✅/❌/⏳/⛔ legend separates measured from predicted; sample-size + cold-load disclosed |
| #7 memory bank drift | ★ | productContext + systemPatterns reflect actual Phase 2a/b delivery, not Phase 0 dream |

## Next session candidates (D-SINGLE-ROUTE honest pick, post-2026-05-12-attempt update)

**2026-05-12 distribution attempt result**: Both Reddit r/LocalLLaMA and HN Show HN have **structural anti-new-account gates** that block immediate posting:
- r/LocalLLaMA: auto-mod removed post within 1 minute of submit (account `u/leagames0221` too new / low karma)
- HN: Show HN explicitly restricted for new accounts per HN's anti-influx page ("become a good contributor, then post an occasional Show HN")

→ Distribution today is **structurally gated**, not a content failure. Pushing more aggressively risks shadow-ban accumulation.

**Recommended single best path: Karma building → re-attempt distribution in 1-2 weeks** ★★★

Rationale:
- Both gates require account standing (5-10 substantive comments + 7+ days age), unavoidable
- GitHub topic tags added today (passive discoverability boost via native search, zero account requirement)
- LinkedIn would bypass these gates but user has no account; account creation = 30-60 min commitment, deferred decision
- 1-2 weeks of comment activity on others' HN/Reddit threads is the literal cheapest path to unblock both channels

**Cadence (AI-assistable)**:
1. Day 1-7: User posts substantive technical comments on HN front-page threads relevant to LLM / consumer-hardware / benchmarks (1-2/day, AI drafts when asked). Target ~5-10 karma + 7+ days account age.
2. Day 8-10: Same in r/LocalLLaMA on others' threads. Target ~5 sub-karma.
3. Day 11+: Re-attempt HN Show HN + r/LocalLLaMA post with the same drafts in `memory_bank/social_drafts.md`.
4. AI helps respond to comments in 30-60 min window after each post lands.

**Alternative immediate distribution (if user wants signal today)**:
- LinkedIn account create (30-60 min) + portfolio announcement post — highest single-channel ROI for engineer portfolio
- Direct contact to known recruiters / 受託 contacts with craftstack URL (the 1 URL surfaces all 3 repos)

**Lower-priority alternatives (Phase 4 deep-work, after distribution generates signal)**:
- ADR-009 falsification experiments (4 zero-CC steps to promote ★★ → ★★★ causal claim)
- Multi-depth NIAH heatmap @ 4k (5 depths × 3 seeds ≈ 30 min, generates 1 PNG that's recruiter-eye-catching)
- New portfolio repo #5/#6 (high effort, low marginal recruiter ROI until existing 3 saturate)

## Blockers

なし。 distribution は user の 5-min click が gating step、 AI 介入余地なし。 user タイミング (Tue-Thu US morning が HN/Reddit 最適) で submit 後、 次 session で feedback response 着手。

## Out of scope (acknowledged limits, ADR-citation 済)

- 真の 1M context inference (consumer 6GB tier 物理不可、 ADR-007 + 009)
- paid API integration (zero CC 制約違反)
- Anthropic Claude (GitHub Models catalog literal 不在、 ADR-008)
- gpt-5 free-tier access (UNAVAILABLE、 ADR-008)
- WSL2 11GB cleanup (user explicit "OK 実行して" 待ち、 portfolio 機能には literal 影響なし)
