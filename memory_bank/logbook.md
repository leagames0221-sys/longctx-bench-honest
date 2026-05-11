# Logbook — longctx-needle-demo

> Append-only chronological event log. Latest entry at bottom.
> Each entry: timestamp / session / 作業 / error / 進捗 / 申し送り.

---

## 2026-05-11 — Phase 0 install (session: portfolio-init)

**作業**:
- `~/projects/portfolio/` parent dir 既存 (browser-agent-demo と共用)
- GitHub repo `leagames0221-sys/longctx-needle-demo` を PUBLIC + MIT で create + clone
- Tier 2 scaffold install: CLAUDE.md / spec.md / README.md / .gitignore / .github/workflows/drift-check.yml
- Memory Bank (Cline pattern) 5 file 配置
- .claude/{skills,agents,commands,hooks}/ dir 構造作成

**error**: なし

**進捗**: Phase 0 scaffold install 完了見込、 initial commit + push 待ち

**申し送り (次 session への引継)**:
- Phase 0 end gate = drift-check workflow が initial push で green になるか実測
- 次 session で Phase 1 着手:
  - `~/tmp/prior-art/` に隔離 clone (vllm + Qwen2.5 + NeedleInAHaystack の 3 件)、 audit (star / commit / Issues)
  - `pip install vllm` (Windows は WSL2 経由が安定の可能性、 install phase で literal 検証必要)
  - HuggingFace から `Qwen2.5-7B-Instruct-1M` weight DL (~15GB)、 dual VRAM 不足時は Q4 quant 検討
  - Needle-in-a-Haystack baseline (128k から start) literal 走行確認
- Phase 2 は 4 size × 4 model = 16 cell 実測、 GitHub Models rate limit に注意

---

## 2026-05-11 — Phase 0 closure verified (session: portfolio-init)

**作業**:
- initial commit (dc5480b → 5a85ac4) push 完了、 10 file changes
- drift-check workflow run 25669544190 = **success** (`gh run watch` で完了確認、 evidence: `gh run list --repo leagames0221-sys/longctx-needle-demo`)
- PJ_REGISTRY.yaml に `longctx_needle_demo` entry 登録済

**Phase 0 end gate**: ✅ 達成

**Phase 0 → Phase 1 引継**:
- Phase 1 entry point: 3 prior art (`vllm` / `Qwen2.5` / `LLMTest_NeedleInAHaystack`) を `~/tmp/prior-art/` に隔離 clone → 各 audit (star / commit / LICENSE / Issues red flag)
- vllm install path 検証 (Windows host で動くか / WSL2 必須か) literal 実測、 結果を decisionLog に ADR-005 として追加
- `Qwen2.5-7B-Instruct-1M` HuggingFace DL (~15GB)、 disk 余裕確認 + consumer GPU VRAM 実測 (BF16 vs Q4 quant 判断)
- NeedleInAHaystack の `eval/` と `pretty_graph.py` を 自 repo に literal copy、 commit msg `derived from LLMTest_NeedleInAHaystack@<sha>`
- baseline 128k 走行で公式 sample 数値範囲内一致 verify
- pip 配線: `pyproject.toml` / `uv.lock` / pip-audit CI / Dependabot for pip
- GitHub Models 接続 sample (small context) で free tier rate limit 実測
