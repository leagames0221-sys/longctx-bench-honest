# System Patterns — longctx-needle-demo

## Drift prevention pattern

**Goal**: README claims ↔ code reality の literal 同期を CI で構造的に強制。

**Mechanism**:
1. README に `## Verified state` table 配置、 各 claim が drift-check で verify されるか明記
2. `.github/workflows/drift-check.yml` が push / PR 毎に走り、 claim mismatch で CI fail
3. claim 追加時は drift-check.yml にも対応 verify step を追加 (PR で同時 review)
4. Phase 2 で数値 claim (heatmap 正答率 / 所要時間) が入る、 これらは `artifacts/` 内 JSON 出力と CI で照合する仕組みを literal install

**Invariant**: claim を README に書く = drift-check 拡張を同 PR に含める。 違反 = CI fail = merge 不可。

---

## Memory Bank pattern (D-HANDOFF-DUTY literal 順守)

**Goal**: AI multi-session で 「前任 session が何をして、 次が何をすべきか」 が literal 引継ぎ可能。

**5 file 役割分担** (browser-agent-demo と同一):
- `logbook.md`: 時系列 append-only
- `activeContext.md`: current phase + 今 focus + 次 concrete step
- `decisionLog.md`: ADR
- `productContext.md`: what / why / target / success signals
- `systemPatterns.md`: how (本 file)

**Protocol**: session 開始 = activeContext → logbook 末尾 § → 必要 ADR。 session 終了 = logbook append、 ADR 発生時 decisionLog 新規、 focus 変更時 activeContext 更新。

---

## Prior art adoption pattern (D-PRIOR-ART-FIRST literal 順守)

**Step**:
1. 候補 OSS を `~/tmp/prior-art/<repo>/` に隔離 clone (採用前 audit zone)
2. star 数 / 直近 commit / Issues red flag scan (D-PRIOR-ART-SECURITY-GATE)
3. LICENSE 確認 (Apache-2.0 / MIT のみ採用、 Qwen は Apache-2.0、 NeedleInAHaystack は MIT、 vllm は Apache-2.0 で全 OK)
4. 必要 file (eval loop / pretty_graph.py / model wrapper) を 自 repo に literal copy
5. commit msg に `derived from <repo>@<sha>` literal 記録
6. 改造範囲 20% 以内に literal 制限

**Invariant**: ゼロ生成は M0 立証責任。

---

## Measurement-first pattern (D-VERIFY-PRIORITY literal 順守)

**Goal**: 全数値 claim を実測 evidence で literal 裏付け、 推測 0。

**Mechanism**:
1. eval 実行は必ず JSON 出力に literal 書き込み (`artifacts/<context_size>_<model>_<timestamp>.json`)
2. heatmap PNG は JSON から自動生成、 手書き禁止
3. README の数値 claim (成功率 X% / 所要時間 Y sec / context Z token) は JSON 由来のみ、 任意改変禁止
4. CI で JSON 存在 + 数値範囲 sanity check を literal 配線
5. logbook に各 eval run の summary entry を append、 全 run trace 可能

**Invariant**: 数値 claim = JSON evidence + CI sanity check の 2 layer 担保、 「だいたい X」 主張は literal 不可。

---

## Honest failure pattern (D9-CalibratedHonesty literal 順守)

**Goal**: literal 1M 推論が consumer laptop で完走不能だった場合、 隠さず failure analysis を portfolio 価値に変換。

**Mechanism**:
1. 各 context size で eval timeout (24h) を literal 設定、 timeout 到達 = 不能と verify
2. timeout 到達時、 logbook に 「不能検出 + 原因 (VRAM OOM / swap / etc) + 計測値」 を literal 記録
3. README に `## Honest results` section、 成功 size + 不能 size + 不能原因を 完全公開
4. 「1M 真稼働 ★★ tier、 256k まで ★★★」 等の confidence marker を honest 表記

**Invariant**: 失敗を隠す = D9 違反 + recruiter 不信 trigger。 失敗 transparency = strong hire signal の 1 軸。

---

## Phase gate pattern

各 Phase end は 「測れる完成品」 で gate される:
- Phase 0: drift-check workflow green on first push
- Phase 1: baseline 128k heatmap PNG + `pytest` 全 green
- Phase 2: 4 size × 4 model 全 cell 実測値 (or honest 不能宣言) + heatmap 4 PNG + 比較 table + 30s 動画
- Phase 3: craftstack 上位 fold link active + r/LocalLLaMA + HN 投稿完了
