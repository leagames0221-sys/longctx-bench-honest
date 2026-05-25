# System Patterns — longctx-bench-honest

## Drift prevention pattern

**Goal**: README claims ↔ code reality の literal 同期を CI で構造的に強制。

**Mechanism**:
1. README に `## Verified state` table 配置、 各 claim が drift-check で verify されるか明記
2. `.github/workflows/drift-check.yml` が push / PR 毎に走り、 claim mismatch で CI fail
3. claim 追加時は drift-check.yml にも対応 verify step を追加 (PR で同時 review)
4. Phase 2 で数値 claim (cost-tier table の cell) が入る、 これらは `artifacts/` 内 JSON 出力と CI で照合する仕組みを literal install
5. repo 名 canon (`longctx-bench-honest`) を README + workflow + CLAUDE.md + spec.md 全件で grep verify

**Invariant**: claim を README に書く = drift-check 拡張を同 PR に含める。 違反 = CI fail = merge 不可。

---

## Cost-tier transparency pattern

**Goal**: 4 model × 3 benchmark + cost + 所要時間 + CC requirement の matrix を README 上位 fold に literal 配置。

**Mechanism**:
1. cost-tier table は markdown table、 README L20-40 圏内に literal 配置 (上位 fold)
2. Phase 0/1 では cell に `pending Phase 2` marker、 drift-check が table 構造 (4 column × 6 row) を verify
3. Phase 2 で JSON evidence (`artifacts/<model>_<benchmark>_<context>.json`) を生成、 README cost-tier table を literal 直接 populate (Phase 2a 実装方式; Phase 0 plan の `scripts/build_cost_table.py` 自動生成は Phase 2b/3 candidate に残置)
4. drift-check が 「README cost-tier table cell の status field = JSON evidence の status field」 を grep で literal 照合、 手書き drift を CI で検出 (`grep -q '"status": "PASS"' artifacts/baseline_4000.json` 等、 22+ step が green)

**Invariant**: cost-tier table 数値 = JSON evidence のみ、 手書き編集禁止。

---

## Prior art adoption pattern

**Step**:
1. 候補 OSS を `~/tmp/prior-art/<repo>/` に隔離 clone (採用前 audit zone)
2. star 数 / 直近 commit / Issues red flag scan
3. LICENSE 確認 (Apache-2.0 / MIT のみ採用)
4. 必要 file (RULER の 13 task generator / LongBench v2 の evaluation script / NIAH の pretty_graph.py) を 自 repo に literal copy
5. commit msg に `derived from <repo>@<sha>` literal 記録
6. 改造範囲 20% 以内に literal 制限

**Invariant**: ゼロ生成は立証責任。 過去 2 度 (Qwen2.5 repo `recipes/long_context/` / Qwen3.6-27B consumer laptop 1M 完走) の hallucination 失敗を archive で記録、 同型再発防止。

---

## Measurement-first pattern

**Goal**: 全数値 claim を実測 evidence で literal 裏付け、 推測 0。

**Mechanism**:
1. eval 実行は必ず JSON 出力に literal 書き込み (`artifacts/<model>_<benchmark>_<timestamp>.json`)
2. cost-tier table cell は JSON から自動生成、 手書き禁止
3. README の数値 claim (RULER X% / LongBench Y% / 所要時間 Z sec) は JSON 由来のみ、 任意改変禁止
4. CI で JSON 存在 + 数値範囲 sanity check を literal 配線
5. logbook に各 eval run の summary entry を append、 全 run trace 可能

**Invariant**: 数値 claim = JSON evidence + CI sanity check の 2 layer 担保、 「だいたい X」 主張は literal 不可。

---

## Honest failure pattern

**Goal**: literal 1M 推論が consumer laptop で完走不能だった場合、 隠さず failure analysis を 価値に変換。

**Mechanism**:
1. 各 eval で timeout (24h) を literal 設定、 timeout 到達 = 不能と verify
2. timeout 到達時、 logbook に 「不能検出 + 原因 (VRAM OOM / swap / etc) + 計測値」 を literal 記録
3. README `## Honest results` section に 4 category 配置:
   - holds up (frontier との gap < 10%)
   - loses badly (gap > 30%) + 推定原因
   - reasonable engineering fix (chunking / RAG augment 等)
   - frontier is the right answer (honest "use the API" 推奨)
4. confidence marker を honest 表記

**Invariant**: 失敗 transparency = honest measurement の 1 軸。

---

## Self-correction archive pattern

**Goal**: 発生した hallucination → 訂正 の履歴を literal 保存、 同型再発防止。

**Mechanism**:
1. 誤推奨 検出時は decisionLog で `## ADR-XXX-archived (YYYY-MM-DD)` ヘッダー + redirect marker (`→ superseded by ADR-XXX-rN`)
2. 元 ADR 本文は literal 残す (削除禁止)
3. 訂正版 ADR (`ADR-XXX-rN`) を新規 append、 Context に `Supersedes ADR-XXX (date)` 明記
4. README で 「2 度の自己訂正記録あり」 と literal 明示、 honest 開示

**Invariant**: 「間違えた時に honest 訂正できる」 は honest measurement narrative の 1 軸、 隠蔽は逆方向。

---

## Phase gate pattern

各 Phase end は 「測れる完成品」 で gate される。 actual delivery state (2026-05-12):
- Phase 0: ✅ drift-check workflow green on first push + overhaul commit green
- Phase 1 partial: ✅ 4 baseline cells (4k PASS / 5k/6k/8k OOM) + ADR-007 (6GB VRAM ceiling characterized) + `pip-audit` GREEN + Dependabot configured. Original 128k RULER subset goal was infeasible at this hardware tier (ADR-007 documents why).
- Phase 2a: ✅ 4 cloud models × {2k, 4k} = 6 cells (gpt-4.1-mini + llama-3.3-70b PASS @ 4k, gpt-5 UNAVAILABLE on free tier, deepseek-v3 PASS @ 2k / TOKEN_LIMIT @ 4k) + ADR-008 (Claude absent from catalog, gpt-5 free-tier blocked). Cost-tier table literal populated with ✅/❌/⏳/⛔ icon legend.
- Phase 2b: ✅ NEGATIVE RESULT documented — WSL2 + vllm 0.7.3 cannot fit Qwen 7B int4 + activations on 6GB VRAM (weights 5.43GiB + activation peak 1.42GiB > 6GiB total). ADR-009 documents the literal vllm memory profile log + 3 alternative hypotheses (not yet experimentally isolated). Falsification path documented for future work.
- Phase 3: ✅ craftstack PR #70 merged into main, "Related portfolio work" section live cross-linking the 2 AI portfolio siblings. r/LocalLLaMA + HN post drafts ready in `social_drafts.md` for submission.
- Phase 4 (future, optional): multi-depth NIAH heatmap @ 4k local ceiling (feasible within constraints; ~30 min measurement budget), falsification experiments for ADR-009's 3 hypotheses, automated `scripts/build_cost_table.py` to replace manual cost-tier population
