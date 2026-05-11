# Product Context — longctx-bench-honest

## What

4 long-context LLM (Qwen2.5-7B-1M local + GPT-5 + Claude Sonnet + Llama 3.3 via GitHub Models) × 3 industry-current benchmarks (RULER + LongBench v2 + NIAH 補助) の literal honest measurement repo。 全 cell に JSON evidence、 全数値が drift-CI で verified、 全 cost が ¥0 (electricity + free tier)。

## Why

portfolio 2 件目 (1 件目 = browser-agent-demo)。 「1M context 動かしてみた」 repo は 2026-05 時点で GitHub 上 数百件以上存在 = 飽和領域。 本 repo の differentiator は **measurement honesty + cost transparency + drift discipline** の 3 軸:

1. **Measurement honesty**: 失敗 task / 不能 context size を 隠さず literal 公開 (D9-CalibratedHonesty 体現)
2. **Cost transparency**: 全 model × 全 benchmark の 所要時間 / メモリ / cost を ¥0 で揃え、 cost-tier table を README 上位 fold に配置
3. **Drift discipline**: 全 numeric claim を JSON evidence + drift-CI で自動 verify、 手動編集禁止

「frontier 大物 (Qwen3.6 / DeepSeek V4) は 8 GPU 必要、 私は consumer laptop で 7B-1M を honest 測定」 という **制約下選定** signal が portfolio 軸。

## Target audience

- 採用担当 (AI lab / 上位 startup / 受託 premium 帯、 global)
- AI ops engineer community (cost/quality trade-off に literal 関心ある層)
- r/LocalLLaMA / Hacker News (1M context は常に話題、 honest measurement は希少 = 反応強い)

## Success signals (採用側が読み取るもの)

1. **drift-free 文書**: 全 README claim が CI で literal verified、 「書きっぱなし」 ではない
2. **failure transparency**: `## Honest results` section に 失敗を literal 開示、 「数値悪くても出せる engineer」 = strong hire 1 軸
3. **cost-tier table**: ¥0 を 4 model × 3 benchmark で literal 揃える、 「無料で frontier 比較できる engineer」 signal
4. **制約下選定**: Qwen3.6 / DeepSeek V4 を選ばなかった理由が ADR に literal 記載、 「制約を理解した上で選定できる engineer」 signal
5. **2026-05 industry alignment**: NIAH 飽和、 RULER 採用、 LongBench v2 採用、 frontier 8 GPU 要件 — 全て公開 source で literal 裏付け
6. **2 度の自己訂正記録**: ADR-001 旧 (Qwen2.5 repo 誤推奨) + ADR-001r1 (Qwen3.6-27B 誤推奨) + ADR-001r2 (Qwen2.5-7B-1M literal 戻し) の 思考過程を archive、 「間違えた時に honest 訂正できる engineer」 signal

## Anti-signals (構造的に避けるもの)

- Phase 0 で literal な数値 claim を README に置かない (drift 必至、 CI fail)
- 受託機密 / client doc の dataset 投入 (公開 source のみ)
- GitHub token の commit 混入
- HuggingFace cache (15GB+) を repo に commit (`.gitignore` で literal 除外)
- 「1M で完璧動作」 claim、 実測値のみ literal 開示
- 古い ADR の literal 削除 (archive + redirect marker で履歴保持、 D-INFORMATION-ABUNDANCE-OK 順守)
- 日本語 domain dataset は scope 外 (user 「選んでる側」、 global recruiter signal 一本に literal 焦点化)
