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

## Next session candidates (D-SINGLE-ROUTE honest pick)

**Recommended single best path: Distribution before new building** ★★★

Rationale:
- 3 portfolio repos at ★★★ tier with drift-CI + JSON evidence is already strong
- Without distribution, no signal reaches recruiters / 受託先 → portfolio sits idle
- r/LocalLLaMA + HN drafts already ready in `social_drafts.md` (5-min user click to submit)
- Community feedback (good or bad) is the literal next data point — without it, more portfolio building is "designing in a vacuum"
- After distribution generates signal, then decide: more breadth (portfolio #5/#6) vs more depth (multi-depth heatmap / falsification experiments)

**Path (next session, AI-assistable steps)**:
1. User submits r/LocalLLaMA post (5 min, user click) → 24h to see comments / votes
2. User submits HN Show HN (5 min, user click) → 4h to see front-page chance
3. Next session: AI helps respond to comments + draft replies + extract signal from feedback
4. After 1 week of signal: decide if portfolio expansion (#5/#6) is warranted or if existing 3 are saturating the recruiter funnel

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
