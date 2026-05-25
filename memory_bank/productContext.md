# Product Context — longctx-bench-honest

## What

Long-context LLM honest measurement repo across 1 local model (Qwen2.5-7B-Instruct-1M) + reachable GitHub Models cloud frontier × NIAH single-needle benchmark at literal feasible context sizes. Originally planned as "Qwen + GPT-5 + Claude Sonnet + Llama 3.3 × RULER + LongBench v2 + NIAH supplement" but **Phase 2a probe found Claude is not in GitHub Models catalog at all, and gpt-5 returns `unavailable_model` on free tier** (ADR-008). Final cloud lineup: gpt-4.1-mini + llama-3.3-70b-instruct + deepseek-v3-0324 + (gpt-5 = honest UNAVAILABLE row). Full RULER + LongBench v2 sweeps are infeasible on 6GB VRAM (ADR-007) — single-needle at 4k is the literal characteristic point. Every cell has JSON evidence, every numeric claim is checked by drift-CI, total cost is ¥0 (electricity + free tier).

## Why

本 repo の differentiator は **measurement honesty + cost transparency + drift discipline** の 3 軸:

1. **Measurement honesty**: 失敗 task / 不能 context size を 隠さず literal 公開
2. **Cost transparency**: 全 model × 全 benchmark の 所要時間 / メモリ / cost を ¥0 で揃え、 cost-tier table を README 上位 fold に配置
3. **Drift discipline**: 全 numeric claim を JSON evidence + drift-CI で自動チェック、 手動編集禁止

「frontier 大物 (Qwen3.6 / DeepSeek V4) は 8 GPU 必要、 consumer laptop で 7B-1M を honest 測定」 という **制約下選定** が portfolio 軸。

## Success signals

1. **drift-free 文書**: 全 README claim が CI でチェック済み、 「書きっぱなし」 ではない
2. **failure transparency**: `## Honest results` section に 失敗を literal 開示
3. **cost-tier table**: ¥0 を 4 model × 3 benchmark で literal 揃える
4. **制約下選定**: Qwen3.6 / DeepSeek V4 を選ばなかった理由が ADR に literal 記載
5. **2026-05 industry alignment**: NIAH 飽和、 RULER 採用、 LongBench v2 採用、 frontier 8 GPU 要件 — 全て公開 source で literal 裏付け
6. **2 度の自己訂正記録**: ADR-001 旧 (Qwen2.5 repo 誤推奨) + ADR-001r1 (Qwen3.6-27B 誤推奨) + ADR-001r2 (Qwen2.5-7B-1M literal 戻し) の 思考過程を archive

## Anti-signals (構造的に避けるもの)

- Phase 0 で literal な数値 claim を README に置かない (drift 必至、 CI fail)
- 受託機密 / client doc の dataset 投入 (公開 source のみ)
- GitHub token の commit 混入
- HuggingFace cache (15GB+) を repo に commit (`.gitignore` で literal 除外)
- 「1M で完璧動作」 claim、 実測値のみ literal 開示
- 古い ADR の literal 削除 (archive + redirect marker で履歴保持)
- 日本語 domain dataset は scope 外
