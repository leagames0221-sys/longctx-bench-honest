# Active Context — longctx-bench-honest

## Current phase

**Phase 1 partial COMPLETE (2026-05-12)** — Install layer GREEN + 4-cell NIAH scaling literal run + 6GB VRAM ceiling characterized + JSON evidence committed + README populated + ADR-007 + drift-CI 19/19 GREEN. Phase 2 (cloud frontier comparison via GitHub Models) is next.

## Current focus

Phase 1 partial deliverable shipped to GitHub main ([commit bc9ae3d](https://github.com/leagames0221-sys/longctx-bench-honest/commit/bc9ae3d)). 4 JSON evidence files + 1 NIAH runner + README cost-tier populated + ADR-007 ceiling characterization + drift-CI extended with 4 new artifact-verify steps.

**Literal hardware ceiling sourced (★★★ tier evidence)**:
- 4k context: PASS (252s inference, peak 10.8GB via Win shared-mem PCIe spillover, needle correctly extracted)
- 5k+ context: OOM (single attention alloc exceeds 6GB physical + shared-mem fallback cap)
- 128k / 1M: infeasible at this hardware tier (sourced in README + ADR-007 with citation chain)

## Next concrete steps (Phase 2 entry)

1. **GitHub Models token setup**: `gh auth token` → `.env` (gitignore済) with `GITHUB_TOKEN` literal export
2. **Cloud cell runner**: `examples/cloud_niah.py` — OpenAI SDK with `base_url=https://models.github.ai/inference`, model param = `openai/gpt-5` / `meta/Llama-3.3-70B-Instruct` / `anthropic/claude-sonnet-4` (verify exact model_id strings via `gh api /catalog/models` or [marketplace catalog API](https://github.com/marketplace/models))
3. **Same NIAH @ 4k task** literal repeated across the 3 cloud models for direct local-vs-frontier comparison at matched context size
4. **Verify 4k input fits in 8000 token free-tier cap** (4k + ~100 output ≈ 4100 tokens = within cap ★★★, evidence: browser-agent-demo v5 hit cap at full DOM context ≈ 6000+ tokens)
5. **Cost-tier table populate**: 3 cloud cells × 4k row literal filled with PASS/FAIL + inference_sec + cost (¥0 for free tier)
6. **JSON evidence**: `artifacts/cloud_gpt5_4000.json` / `cloud_claude_4000.json` / `cloud_llama_4000.json`
7. **drift-CI extension**: 3 new step (cloud artifacts + status + URL)

## Phase 2 后半 candidate (optional, after cloud cells)

- **WSL2 + vllm PagedAttention**: literal install path verify (free, no CC), check if PagedAttention extends ceiling from 4k → 8-16k on same 6GB GPU
  - If yes: re-run scaling experiment in WSL2, populate cost-tier with extended cells, document WSL2 install path in SETUP.md
  - If no / install fail: document the negative result as honest evidence
- **Heatmap visualization**: NIAH-style depth × context heatmap for the 4k cell (single depth = 50% in current run, extend to multiple depths for portfolio visual)

## Phase 3 (after Phase 2)

- craftstack 上位 fold に 2 repo (browser-agent-demo + longctx-bench-honest) link + thesis 1 行 + cost-tier summary
- r/LocalLLaMA + Hacker News post drafting ("constraint-optimized AI engineering: 4k VRAM ceiling on RTX 3050 + free-tier cloud cap at 6k = the literal map of consumer-laptop long-context measurement")

## Blockers

なし。 Phase 2 着手 OK (Phase 1 partial deliverable がGitHub main に literal shipped、 drift-CI green、 evidence URL 全件 live)。

## Out of scope (current phase)

- 真の 1M context inference (consumer 6GB tier では物理不可、 ADR-007 で literal 記録済、 future RTX 4090 24GB / WSL2 PagedAttention path のみ candidate)
- paid API integration (zero CC 制約違反、 literal scope 外)
- 日本語 domain dataset (ADR-004 で literal scope 外確定済)
- 30s 動画撮影 (Phase 3 craftstack 統合時の任意 deliverable)
