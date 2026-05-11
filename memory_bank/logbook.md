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

---

## 2026-05-11 — Phase 0 overhaul: repo rename + scope literal 全面書き換え (session: portfolio-init)

**作業**:
- WebSearch + WebFetch で 2026-05 industry state 確認 (Qwen3.6 / DeepSeek V4 / RULER / LongBench v2 / NIAH saturation evidence)
- 2 度の hallucination 自己訂正を ADR archive (ADR-001-archived: Qwen2.5 repo `recipes/long_context/` 実在不在、 ADR-001-r1-archived: Qwen3.6-27B が VLM + 8 GPU 推奨 = D-CONSUMER-HW 違反)
- LLM 確定: ADR-001-r2 で Qwen2.5-7B-Instruct-1M に literal 戻し (consumer laptop 唯一の真 1M 完走候補)
- Benchmark 拡張: ADR-003-r1 で RULER + LongBench v2 + 補助 NIAH の 3 benchmark 構成に literal 移行
- Dataset scope 確定: ADR-004 で 公開 source 限定、 日本語 domain dataset literal scope 外
- repo rename: `gh repo rename longctx-needle-demo → longctx-bench-honest` 成功 + description 更新
- local dir rename: `longctx-needle-demo → longctx-bench-honest` + git remote URL 更新
- 9 file literal 全面書き換え: README.md / spec.md / CLAUDE.md / productContext.md / systemPatterns.md / decisionLog.md (ADR 6 件 + archive marker) / activeContext.md / 本 logbook (append) / drift-check.yml (拡張予定)

**error**: なし (PowerShell native command で stderr が error 扱いされる仕様事象を除く)

**進捗**: 9 file 書き換え完了見込、 drift-check 拡張 + commit + push + 再 verify 待ち

**申し送り (次 session)**:
- overhaul commit + push 完了後の drift-check workflow が new claim 群 (4 model 名 + 3 benchmark 名 + repo 名 canon + cost-tier table 構造 + Phase declaration) を全件 green で verify することを実測
- Phase 1 entry point: 3 prior art audit (RULER + LongBench / vllm + NIAH は既 clone) + LongBench v2 LICENSE 確認 + vllm install path 実測 (Win vs WSL2) + Qwen 1M DL + baseline 128k RULER subset
- portfolio differentiator は **measurement honesty + cost transparency + drift discipline** の 3 軸、 Phase 2 で cost-tier table 16 cell 自動生成 + Honest results section literal 開示が core deliverable

---

## 2026-05-11 — Portfolio unifying thesis 確定 (session: portfolio-init)

**作業**:
- user 提案 「全 free 制約下で best」 を portfolio unifying thesis として literal 採用、 前 entry の 「3 differentiator (measurement honesty + cost transparency + drift discipline)」 を **1 つの thesis** に literal 統合
- README 上位 fold に `## Selected under` section literal 追加 (4 constraint: zero CC / consumer laptop / public source / drift-CI enforced)
- README に `## Why this is the literal best under the constraint set` section literal 追加 (6 row 選定 vs 却下 table、 Qwen3.6-27B 8 GPU 要件 / DeepSeek V4 / Gemma 4 / Anthropic API / OpenAI API / NIAH 単独 / llama.cpp / TGI 等を sourced reason で却下 explicit 化)
- README 上部に 3 constraint badge (shields.io) 追加
- portfolio category: **constraint-optimized AI engineering** に literal 確定 (browser-agent-demo と同 thesis)
- drift-check workflow 拡張: Selected under section + 4 constraint 文字列 + portfolio category line + Why best section + Rejected alternatives column の literal 存在 verify (13 step → 15 step)

**Thesis (literal 永続記録)**:
> Constraint-optimized AI engineering — best possible AI systems under (1) zero credit card, (2) consumer laptop, (3) public source / OSS only, (4) drift-CI enforced。 cross-repo (browser-agent-demo + longctx-bench-honest) で unifying narrative。 採用 / 受託 共通の signal axis: 「制約下で最善を出す engineer」。 2 度の ADR 自己訂正 (Qwen2.5 repo hallucination / Qwen3.6-27B 8 GPU 制約) は本 thesis の literal evidence (= option-space audit の証跡)。

**進捗**: thesis literal 確定 + drift-check 拡張完了見込、 commit + push + 再 verify 待ち

**申し送り (次 session)**:
- Phase 1 着手時、 全 ADR の Context section に `(constraint: zero CC / consumer laptop / public source / drift-CI)` を literal 明記、 thesis を ADR 単位でも literal 反映
- craftstack 上位 fold は Phase 3 で同 thesis を hub message として配置 (2 repo + thesis 1 行)
