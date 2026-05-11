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

**Goal**: 4 model × 3 benchmark + cost + 所要時間 + CC requirement の matrix を README 上位 fold に literal 配置、 recruiter 5 秒判定で 「¥0 で frontier 比較できる engineer」 signal を立てる。

**Mechanism**:
1. cost-tier table は markdown table、 README L20-40 圏内に literal 配置 (上位 fold)
2. Phase 0/1 では cell に `pending Phase 2` marker、 drift-check が table 構造 (4 column × 6 row) を verify
3. Phase 2 で JSON evidence (`artifacts/<model>_<benchmark>_<timestamp>.json`) から `scripts/build_cost_table.py` で自動生成、 README に literal 書き戻し
4. drift-check が 「README cost-tier table の数値 = JSON evidence の数値」 を CI で照合、 手動編集を構造的に検出

**Invariant**: cost-tier table 数値 = JSON evidence のみ、 手書き編集禁止 (D-VERIFY-PRIORITY literal 順守)。

---

## Memory Bank pattern (D-HANDOFF-DUTY literal 順守)

**Goal**: AI multi-session で 「前任 session が何をして、 次が何をすべきか」 が literal 引継ぎ可能。

**5 file 役割分担** (browser-agent-demo と同一):
- `logbook.md`: 時系列 append-only
- `activeContext.md`: current phase + 今 focus + 次 concrete step
- `decisionLog.md`: ADR (archive + redirect marker で supersede 履歴保持)
- `productContext.md`: what / why / target / success signals
- `systemPatterns.md`: how (本 file)

**Protocol**: session 開始 = activeContext → logbook 末尾 § → 必要 ADR。 session 終了 = logbook append、 ADR 発生時 decisionLog 新規、 focus 変更時 activeContext 更新。

---

## Prior art adoption pattern (D-PRIOR-ART-FIRST literal 順守)

**Step**:
1. 候補 OSS を `~/tmp/prior-art/<repo>/` に隔離 clone (採用前 audit zone)
2. star 数 / 直近 commit / Issues red flag scan (D-PRIOR-ART-SECURITY-GATE)
3. LICENSE 確認 (Apache-2.0 / MIT のみ採用)
4. 必要 file (RULER の 13 task generator / LongBench v2 の evaluation script / NIAH の pretty_graph.py) を 自 repo に literal copy
5. commit msg に `derived from <repo>@<sha>` literal 記録
6. 改造範囲 20% 以内に literal 制限

**Invariant**: ゼロ生成は M0 立証責任。 過去 2 度 (Qwen2.5 repo `recipes/long_context/` / Qwen3.6-27B consumer laptop 1M 完走) の hallucination 失敗を archive で記録、 同型再発防止。

---

## Measurement-first pattern (D-VERIFY-PRIORITY literal 順守)

**Goal**: 全数値 claim を実測 evidence で literal 裏付け、 推測 0。

**Mechanism**:
1. eval 実行は必ず JSON 出力に literal 書き込み (`artifacts/<model>_<benchmark>_<timestamp>.json`)
2. cost-tier table cell は JSON から自動生成、 手書き禁止
3. README の数値 claim (RULER X% / LongBench Y% / 所要時間 Z sec) は JSON 由来のみ、 任意改変禁止
4. CI で JSON 存在 + 数値範囲 sanity check を literal 配線
5. logbook に各 eval run の summary entry を append、 全 run trace 可能

**Invariant**: 数値 claim = JSON evidence + CI sanity check の 2 layer 担保、 「だいたい X」 主張は literal 不可。

---

## Honest failure pattern (D9-CalibratedHonesty literal 順守)

**Goal**: literal 1M 推論が consumer laptop で完走不能だった場合、 隠さず failure analysis を portfolio 価値に変換。

**Mechanism**:
1. 各 eval で timeout (24h) を literal 設定、 timeout 到達 = 不能と verify
2. timeout 到達時、 logbook に 「不能検出 + 原因 (VRAM OOM / swap / etc) + 計測値」 を literal 記録
3. README `## Honest results` section に 4 category 配置:
   - holds up (frontier との gap < 10%)
   - loses badly (gap > 30%) + 推定原因
   - reasonable engineering fix (chunking / RAG augment 等)
   - frontier is the right answer (honest "use the API" 推奨)
4. 「1M 真稼働 ★★ tier、 256k まで ★★★」 等の confidence marker を honest 表記

**Invariant**: 失敗を隠す = D9 違反 + recruiter 不信 trigger。 失敗 transparency = strong hire signal の 1 軸。

---

## Self-correction archive pattern (D-INFORMATION-ABUNDANCE-OK literal 順守)

**Goal**: AI multi-session で発生する 自身 hallucination → 訂正 の履歴を literal 保存、 同型再発防止 + 思考過程の portfolio 価値転化。

**Mechanism**:
1. 誤推奨 検出時は decisionLog で `## ADR-XXX-archived (YYYY-MM-DD)` ヘッダー + redirect marker (`→ superseded by ADR-XXX-rN`)
2. 元 ADR 本文は literal 残す (削除禁止、 D-INFORMATION-ABUNDANCE-OK)
3. 訂正版 ADR (`ADR-XXX-rN`) を新規 append、 Context に `Supersedes ADR-XXX (date)` 明記
4. README で 「2 度の自己訂正記録あり」 と literal 明示、 採用側に honest 開示

**Invariant**: 「間違えた時に honest 訂正できる engineer」 signal = strong hire 1 軸、 隠蔽は逆 signal。

---

## Phase gate pattern

各 Phase end は 「測れる完成品」 で gate される:
- Phase 0: drift-check workflow green on first push + overhaul commit green
- Phase 1: baseline 128k RULER subset + `pytest` 全 green + pip-audit + Dependabot
- Phase 2: 4 model × 3 benchmark 全 cell 実測値 (or honest 不能宣言) + cost-tier table 自動生成 + Honest results + 30s 動画
- Phase 3: craftstack 上位 fold link active + r/LocalLLaMA + HN 投稿完了
