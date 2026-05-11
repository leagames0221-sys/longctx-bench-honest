# Decision Log — longctx-bench-honest

> ADR (Architecture Decision Record) 形式。 重要決定のみ append。
> Supersede 時は `archived` ヘッダー + redirect marker 必須 (D-HANDOFF-DUTY 順守)。

---

## ADR-001-archived (2026-05-11): LLM は Qwen2.5-7B-Instruct-1M を local (vllm) で採用

→ **superseded by ADR-001-r1 (同日)、 さらに superseded by ADR-001-r2 (同日)**

**Context (original)**: literal 1M token context を扱う portfolio demo が必要、 かつクレカ不要範囲を維持。

**Decision (original)**: `Qwen/Qwen2.5-7B-Instruct-1M` を vllm 経由 local 推論。

**Archive reason**: 当該 ADR 自体の判断は最終的に正解だが、 ADR-003 で `QwenLM/Qwen2.5 recipes/long_context/` を prior art として記載 → 実 path 不在 (hallucination)、 さらに ADR-001-r1 で Qwen3.6-27B に切替を提案 → consumer laptop 完走不可 (D-CONSUMER-HW 違反) → 再度 ADR-001-r2 で literal 戻し、 という 2 度自己訂正の起点となったため archive 化。 原文は D-INFORMATION-ABUNDANCE-OK 順守で literal 保持。

---

## ADR-001-r1-archived (2026-05-11): Qwen3.6-27B に切替を提案

→ **superseded by ADR-001-r2 (同日)**

**Context**: 「2026-05 ベスト?」 user 質問への WebSearch 結果から、 Qwen3.6-27B (2026-03 release、 1M default、 Apache 2.0、 HuggingFace 公開) を frontier として propose。

**Decision (proposed)**: Qwen2.5-7B-1M を撤回、 Qwen3.6-27B に切替。

**Archive reason**: WebFetch で HuggingFace model card を verify した結果、 (1) Qwen3.6-27B は VLM (Vision-Language Model) で image input を持つ、 (2) context は native 262k で 1M は YaRN 拡張、 (3) **8 GPU tensor parallel 推奨** = consumer laptop 完走 literal 不可能 = D-CONSUMER-HW 違反、 (4) 「128K minimum to preserve thinking capabilities」 制約あり、 という 4 点で portfolio constraint 不適合判明。 切替提案は撤回、 ADR-001-r2 で Qwen2.5-7B-1M に literal 戻し。

---

## ADR-001-r2 (2026-05-11): LLM は Qwen2.5-7B-Instruct-1M で literal 確定

**Context**: ADR-001 / ADR-001-r1 の 2 度の自己訂正を経て、 portfolio constraint (D-CONSUMER-HW + クレカ不要 + literal 1M context) を全件満たす唯一の選択肢を確定する必要。

**Decision**: `Qwen/Qwen2.5-7B-Instruct-1M` (Apache-2.0、 HuggingFace 公開) を vllm 経由 local 推論で literal 確定。 frontier model (Qwen3.6 / DeepSeek V4 / Qwen3.5-35B / Gemma 4 26B) は 8 GPU 級要件で consumer laptop 完走不可、 portfolio 軸は 「frontier を選ばなかった理由が説明可能な engineer」 signal に literal 転化。

**Sources (D8)**:
- [Qwen/Qwen2.5-7B-Instruct-1M HuggingFace](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M)
- [Qwen3.6-27B model card](https://huggingface.co/Qwen/Qwen3.6-27B) (8 GPU 推奨 evidence)
- [Open-Source LLM Landscape 2026](https://codersera.com/blog/open-source-llms-landscape-2026/)

**Consequences**:
- ✅ クレカ不要、 offline 実行可能、 consumer laptop literal 完走 (実例多数)
- ✅ Apache 2.0 で commercial portfolio に literal 問題なし
- ✅ portfolio 軸の literal 転化: 「frontier では 8 GPU 必要、 私は 7B-1M を honest 測定」 = 制約下選定 signal
- ⚠️ 2024-2025 vintage = frontier ではない、 recruiter 5 秒判定で 「古い?」 印象 risk → README で literal 説明明記 (「Why Qwen2.5-7B-1M (and not Qwen3.6 / DeepSeek V4)」 section)
- ⚠️ 真 1M 推論時間は consumer laptop で 分〜時間 order の可能性 ★★、 実測値で Phase 2 literal 判断

**Verify**: Phase 1 で baseline 128k 走行成功 + Phase 2 で 1M 走行所要時間 / メモリ / 正答率を `artifacts/` JSON literal 記録、 「Honest results」 section で literal 開示。

---

## ADR-002 (2026-05-11): 比較対象 API は GitHub Models 経由に literal 限定

**Context**: 4 model 比較 (Qwen local + 3 frontier) が必要、 ただし Anthropic / OpenAI 直接 API は CC 必須 → portfolio doctrine 違反。

**Decision**: GitHub Models marketplace (free tier、 GitHub token のみ、 CC 不要) を 唯一の API 経路として採用。 GPT-5 / Claude Sonnet / Llama 3.3 の 3 model を選定。

**Consequences**:
- ✅ クレカ不要維持、 GitHub token は .env で secret 管理
- ✅ OpenAI-compat SDK で接続容易
- ⚠️ rate limit 存在、 Phase 2 で 4 model 同時 eval は間隔配信必須
- ⚠️ Free tier 仕様は GitHub 側の policy 変動 risk ★★、 Phase 2 着手前に literal 確認

**Verify**: Phase 1 末で sample API call (small context) で接続確認、 rate limit 実測値を logbook に記録。

---

## ADR-003-archived (2026-05-11): Eval harness は LLMTest_NeedleInAHaystack を fork-with-attribution

→ **superseded by ADR-003-r1 (同日)**

**Context (original)**: 1M context の literal 検証には needle-in-a-haystack pattern が業界 standard。

**Decision (original)**: `gkamradt/LLMTest_NeedleInAHaystack` (MIT) を prior art に採用、 `QwenLM/Qwen2.5 recipes/long_context/` も併用と記載。

**Archive reason**: (1) `QwenLM/Qwen2.5 recipes/long_context/` は実 path 不在 (clone 結果で確認、 hallucination) + repo 自体が Qwen3 にrename済 + LICENSE missing、 (2) NIAH は 2025-2026 で saturated と業界レポート (NIAH の進化版 RULER 推奨)、 という 2 点で benchmark scope 拡張必要。 ADR-003-r1 で RULER + LongBench v2 + 補助 NIAH の 3 benchmark 構成に literal 移行。

---

## ADR-003-r1 (2026-05-11): Benchmark scope は RULER + LongBench v2 + 補助 NIAH

**Context**: ADR-003 の 2 問題 (Qwen2.5 repo hallucination + NIAH 飽和) を 解消、 2026-05 industry-current benchmark に literal 切替必要。

**Decision**:
- **RULER** (`NVIDIA/RULER`、 Apache 2.0、 13 task 長 context benchmark、 NIAH の進化版、 17 OSS model 評価実績) を **主 benchmark 1** として採用
- **LongBench v2** (`THUDM/LongBench`、 ACL 2025、 503 MCQ で reasoning depth 測定) を **主 benchmark 2** として採用
- **NIAH** (`gkamradt/LLMTest_NeedleInAHaystack`、 MIT) は **補助 visual** として残す (heatmap が recruiter 認知性高い、 ただし saturated の事実を README で literal 明記)

**Sources (D8)**:
- [NVIDIA/RULER github](https://github.com/NVIDIA/RULER)
- [THUDM/LongBench github](https://github.com/THUDM/LongBench)
- [LongBench v2 official](https://longbench2.github.io/)
- [Evaluating Long Context — NIAH saturation note](https://nrehiew.github.io/blog/long_context/)

**Consequences**:
- ✅ industry 2026 standard 採用、 recruiter から 「最新 benchmark を選定できる」 signal
- ✅ 3 benchmark で multi-angle 評価、 single benchmark over-fitting risk 低減
- ✅ NIAH visual は 残すので heatmap PNG の portfolio 訴求力 維持
- ⚠️ 3 benchmark 実装 = Phase 2 scope 拡大、 4 model × 3 benchmark = 12 cell 最低 (RULER は 13 task で 52 cell)
- ⚠️ LongBench v2 LICENSE 詳細は repo audit で Phase 1 literal 確認

**Verify**: Phase 1 で 3 benchmark repo を `~/tmp/prior-art/` 隔離 clone + audit、 Phase 2 で全 sweep + cost-tier table 自動生成。

---

## ADR-004 (2026-05-11): Dataset は公開 source 限定 (受託機密 literal 禁止、 日本語 domain は scope 外)

**Context**: benchmark 実行に dataset 必要、 ただし受託案件 / client 機密 doc は portfolio public repo に literal 投入禁止。 また user は受託案件選定立場で、 日本語 domain への literal 焦点化は不要 (global recruiter signal 一本)。

**Decision**: 公開 dataset のみ使用:
- RULER は generator 同梱、 dataset 自動生成
- LongBench v2 は `zai-org/LongBench-v2` HuggingFace dataset (公開、 license は HuggingFace に従う)
- NIAH は haystack 自動生成 (Paul Graham essays 等の公開 corpus)

日本語 domain dataset (e-Gov 法令 等) は ADR 旧版で言及あったが scope 外に literal 確定。

**Consequences**:
- ✅ public commit に問題なし、 受託 NDA 違反 risk ゼロ
- ✅ 第三者再現性確保 (同 dataset で同 eval 再現可能)
- ✅ scope 縮減、 Phase 2 工数 節約
- ⚠️ HuggingFace dataset url 変動可能性 ★★、 dataset DL script の安定性 Phase 1 verify

**Verify**: Phase 1 で dataset DL script 動作確認、 LICENSE 表記が README に literal 明記。

---

## ADR-005 (Phase 1 で起草予定): vllm install path (Windows host vs WSL2)

**Context**: vllm install を Windows host で行うか WSL2 経由か literal 実測判断必要 (consumer laptop 環境制約)。

**Decision (Phase 1 で確定予定)**:
- Phase 1-3 で Windows host 直接 install を literal 試行
- failure 時は WSL2 経由を試行
- 成功した path を canonical install method として README populate

**Verify**: Phase 1 末で install path + 推論動作確認 + 結果を本 ADR に literal 追記。
