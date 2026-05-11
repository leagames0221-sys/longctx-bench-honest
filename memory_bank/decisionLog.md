# Decision Log — longctx-needle-demo

> ADR (Architecture Decision Record) 形式。 重要決定のみ append。

---

## ADR-001 (2026-05-11): LLM は Qwen2.5-7B-Instruct-1M を local (vllm) で採用

**Context**: literal 1M token context を扱う portfolio demo が必要、 かつクレカ不要範囲 (Anthropic API / Gemini paid tier 不使用) を維持。

**Decision**: `Qwen/Qwen2.5-7B-Instruct-1M` (Apache-2.0、 HuggingFace 公開) を vllm 経由 local 推論。 真 1M context literal 対応の数少ない open weights model。

**Consequences**:
- ✅ クレカ不要、 offline 実行可能、 portfolio 唯一性 (local 1M 実用化) literal 達成
- ✅ Apache-2.0 で commercial portfolio に問題なし
- ⚠️ 7B size + 1M context は consumer laptop で推論時間が分〜時間 order 可能性 ★★、 実測値で literal 判断 (D-NO-COMPROMISE-IN-DESIGN: 設計に 1M 含める、 実装 phase で literal 不能検出時のみ refactor)
- ⚠️ VRAM 不足時は Q4 quant 適用、 quality drop は heatmap で literal 計測

**Verify**: Phase 1 で baseline 128k 走行成功、 Phase 2 で 1M 走行所要時間 / メモリ / 正答率を memory_bank/logbook.md に literal 記録。

---

## ADR-002 (2026-05-11): 比較対象 API は GitHub Models 経由に literal 限定

**Context**: 4 model 比較 (Qwen local + 3 frontier) が必要、 ただし Anthropic / OpenAI 直接 API は CC 必須 → portfolio doctrine 違反。

**Decision**: GitHub Models marketplace (free tier、 GitHub token のみ、 CC 不要) を 唯一の API 経路として採用。 GPT-5 / Claude Sonnet / Llama 3.3 (long-context) の 3 model を選定。

**Consequences**:
- ✅ クレカ不要維持、 GitHub token は .env で secret 管理
- ✅ OpenAI-compat SDK で接続容易、 既存 sample 流用可
- ⚠️ rate limit 存在、 Phase 2 で 4 model 同時 eval は間隔配信必須
- ⚠️ Free tier 仕様は GitHub 側の policy 変動 risk ★★、 Phase 2 着手前に literal 確認

**Verify**: Phase 1 末で sample API call (small context) で接続確認、 rate limit 実測値を logbook に記録。

---

## ADR-003 (2026-05-11): Eval harness は LLMTest_NeedleInAHaystack を fork-with-attribution

**Context**: 1M context の literal 検証には needle-in-a-haystack pattern が業界 standard、 ゼロ実装は D-PRIOR-ART-FIRST 違反。

**Decision**: `gkamradt/LLMTest_NeedleInAHaystack` (MIT) を `~/tmp/prior-art/` に隔離 clone → audit → 必要 file (eval loop / pretty_graph.py / dataset format) を自 repo に literal 抽出。 commit msg に `derived from LLMTest_NeedleInAHaystack@<sha>` 記録。

**Consequences**:
- ✅ 1M eval が baseline 含めて 1-2 日に圧縮
- ✅ heatmap 可視化 (`pretty_graph.py`) を流用、 portfolio 視覚映え担保
- ⚠️ 改造範囲 20% 以内に literal 制限、 超える = 別 prior art 探す judgment trigger

**Verify**: Phase 1 で baseline 128k heatmap が公式 sample と数値範囲 内一致。

---

## ADR-004 (2026-05-11): Haystack dataset は公開 source 限定 (受託機密 literal 禁止)

**Context**: 1M token 文書を入れる必要、 ただし受託案件 / client 機密 doc は portfolio public repo に literal 投入禁止。

**Decision**: 公開 dataset のみ使用 — e-Gov 法令 全文 (公的 free)、 Wikipedia 日本語 dump (CC-BY-SA)、 UE5 公式 docs (公開)、 arXiv 公開論文。 出典 + LICENSE を README に明記。

**Consequences**:
- ✅ public commit に問題なし、 受託 NDA 違反 risk ゼロ
- ✅ 第三者再現性確保 (同 dataset で同 eval 再現可能)
- ⚠️ dataset 取得 script の安定性、 source URL 変動可能性 ★★ → snapshot を artifacts (LFS) に保存検討

**Verify**: dataset DL script が repo clone 直後に literal 動く、 LICENSE 表記が README + dataset/ dir 両方に存在。
