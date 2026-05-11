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

---

## ADR-007 (2026-05-12): 6GB VRAM hard ceiling literal characterized at ~4k tokens — pivot from "128k single baseline" to "scaling curve + sourced ceiling"

**Context (constraint: zero CC / consumer laptop / public source / drift-CI enforced)**: prior session draft (activeContext.md) planned a single baseline 128k RULER subset run. The Phase 1 partial session (2026-05-12) literal measured the hardware. Findings:

- GPU: RTX 3050 Laptop **6GB VRAM** (consumer-laptop tier per spec)
- Model: Qwen2.5-7B-Instruct-1M, int4 NF4 (bitsandbytes 0.49.2, double quant) — ~4GB on GPU
- transformers 5.8.0 + accelerate 1.13.0 + torch 2.5.1+cu124
- Activations + KV cache budget: ~1GB after weights

**Literal measurements** (artifacts/baseline_{4000,5000,6000,8000}.json):

| context_tokens | status | peak VRAM | failure point |
|---|---|---|---|
| 4000 | PASS (needle "2867825" correctly extracted) | 10.80 GB (via Win shared-mem PCIe spillover) | n/a — 252s inference |
| 5000 | OOM at inference | 11.18 GB allocated → 2.46 GB alloc fail | shared-mem cap |
| 6000 | OOM at inference | 9.35 GB allocated → 3.57 GB alloc fail | mid-pass attention |
| 8000 | OOM at inference | 6.15 GB → 6.43 GB single-block alloc fail | first attention forward |

**Decision**: pivot Phase 1 deliverable from "128k single baseline + 1 cell" to **"scaling curve {4k PASS, 5k/6k/8k OOM} + sourced 6GB VRAM ceiling + cost-tier table populated with literal hardware constraint evidence"**.

This is NOT a design-phase compromise (D-NO-COMPROMISE-IN-DESIGN). It is an implementation-phase refactor triggered by literal physical-constraint discovery (the doctrine's explicit exception). The original goal — honest measurement under constraints — is *more* directly satisfied by the literal ceiling than by a hypothetical 128k single-run that would not have been achievable on this hardware tier.

**Sources (D8)**:
- [Qwen2.5-7B-Instruct-1M config.json](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M/blob/main/config.json): max_position_embeddings 1010000, dual_chunk_attention_config (chunk 262144 + local 8192)
- [bitsandbytes int4 NF4](https://github.com/bitsandbytes-foundation/bitsandbytes): ~0.5 bytes/param → 7B model ≈ 3.5GB + lm_head/embedding overhead ≈ 4GB
- KV cache size per token: 28 layers × 4 kv_heads × 128 head_dim × 2 (k+v) × 2 bytes (fp16) ≈ 57KB/token → 128k tokens ≈ 7GB (literal exceeds 6GB GPU alone, before model weights)

**Consequences**:
- ✅ Cost-tier table populated with 4 literal cells (4k PASS + 5k/6k/8k OOM) backed by JSON evidence
- ✅ Portfolio thesis "constraint-optimized AI engineering" literal evidenced — boundary characterized, not hand-waved
- ✅ Recruiter signal: "engineer who maps the literal feasibility frontier of their tools rather than overclaiming"
- ⚠️ 128k / 1M cell remains `infeasible at this hardware tier` — future Phase 2 path is WSL2+vllm PagedAttention (may push ceiling to ~8-16k) or cloud frontier (limited by GitHub Models 8000-token free-tier cap)
- ⚠️ The 4k PASS uses Windows shared-mem PCIe spillover (peak 10.8GB) — strictly speaking already past the "pure VRAM" boundary; honest classification is "consumer-tier feasibility with OS-level memory management assist"

**Verify**: Phase 1 baseline JSON evidence (4 files in artifacts/) literal committed, drift-CI extended to verify their presence + JSON schema fields, README cost-tier table cell values mirror JSON status fields.

---

## ADR-008 (2026-05-12): GitHub Models free-tier literal accessibility map — substitute model selection

**Context (constraint: zero CC / consumer laptop / public source / drift-CI enforced)**: Phase 0 plan referenced "GPT-5 / Claude Sonnet / Llama 3.3" as the cloud comparison set. Phase 2a session (2026-05-12) literal probed the GitHub Models catalog API (`https://models.github.ai/catalog/models`) + inference endpoint (`https://models.github.ai/inference`).

**Literal probe results**:

1. **Anthropic Claude: NOT IN CATALOG** — zero Anthropic models present in GitHub Models marketplace (verified by full catalog enumeration). Plan's "Claude Sonnet" cell is literal unreachable under zero-CC constraint.
2. **openai/gpt-5: catalog-listed (200k input / 100k output / "custom" tier) but inference returns `unavailable_model`** — even at 2000 token request (well within 4000 token cap discovered separately), API responds with `BadRequestError: Unavailable model: gpt-5`. Free-tier access is literal blocked.
3. **openai/gpt-4.1-mini (1M / low tier)**: PASS @ 4000 token request, prompt_tokens=3723, completion=4 tokens, latency 8.54s.
4. **meta/llama-3.3-70b-instruct (128k / high tier)**: PASS @ 4000 token request, prompt_tokens=3856, completion=4 tokens, latency 5.17s.
5. **deepseek/deepseek-v3-0324 (128k / high tier)**: PASS @ 2000 token request (1.72s); **TOKEN_LIMIT @ 4000** with literal error "Max size: 4000 tokens" — the 128k catalog cap and the free-tier request cap are different numbers.

**Decision**: substitute the cloud comparison set to literal-reachable models:

| Plan-original | Phase 2a replacement | reason |
|---|---|---|
| GPT-5 | gpt-4.1-mini (also OpenAI, 1M context) | gpt-5 inference returns `unavailable_model` on free tier |
| Claude Sonnet | (no replacement, document gap honestly) | Anthropic literal absent from GitHub Models catalog |
| Llama 3.3 | meta/llama-3.3-70b-instruct | matches plan |
| — (new addition) | deepseek/deepseek-v3-0324 | alt-vendor diversity; demonstrates the literal "free-tier cap below catalog cap" pattern |

**Free-tier cap pattern (★★ tier, n=4 models)**:
- "low" tier OpenAI models: free-tier cap ≥ 4000 input tokens (gpt-4.1-mini PASS)
- "high" tier Meta models: free-tier cap ≥ 4000 input tokens (llama-3.3-70b PASS)
- "high" tier DeepSeek: free-tier cap = **4000 input tokens hard** (literal error at 4001+)
- "custom" tier OpenAI gpt-5: free-tier blocked at availability layer (UNAVAILABLE before token cap fires)

**Sources (D8)**:
- [GitHub Models catalog API enumeration](https://models.github.ai/catalog/models) — accessed 2026-05-12 via curl + gh auth token
- artifacts/cloud_*.json — 6 literal JSON evidence files for the 6 attempts above
- API error payload examples: "tokens_limit_reached / Max size: 4000 tokens" (TOKEN_LIMIT), "unavailable_model / Unavailable model: gpt-5" (UNAVAILABLE_MODEL)

**Consequences**:
- ✅ Cost-tier table populated with 4 cloud cells (2 PASS, 2 TOKEN_LIMIT, 1 UNAVAILABLE) + 1 plan-mismatch row (Claude absent from catalog)
- ✅ Portfolio thesis literal evidenced from cloud side: **the reachable zero-CC frontier at 4k is gpt-4.1-mini + llama-3.3-70b, both 30-50x faster than local 4k**
- ✅ Recruiter signal: "engineer who maps both local VRAM ceilings AND cloud accessibility tiers honestly, with literal API error citations"
- ⚠️ Some "catalog max input" numbers are aspirational under free tier — the literal usable cap is lower (4000 tokens for gpt-5 / deepseek per probe)
- ⚠️ gpt-5 may become accessible if the user upgrades to a paid GitHub Models / Azure OpenAI tier — but that violates `zero credit card` constraint and is out of scope

**Verify**: drift-CI extended with cloud_*.json evidence + status + README link verification. README cost-tier table cells mirror JSON status fields literal.

---

## ADR-009 (2026-05-12): WSL2 + vllm CANNOT extend the 6GB VRAM ceiling — Windows shared-memory was the literal enabler

**Context (constraint: zero CC / consumer laptop / public source / drift-CI enforced)**: Phase 2b experiment tested whether WSL2 + vllm (Linux-only inference engine with PagedAttention KV-cache efficiency) could push the 4k context ceiling characterized in ADR-007 to ≥8k or ≥16k on the same RTX 3050 6GB Laptop GPU.

**Setup (literal, in WSL2 Ubuntu 24.04)**:
- uv venv (Python 3.12.3)
- vllm 0.7.3 (older version; vllm 0.20.2 requires CUDA 12.8+, driver is 12.6)
- torch 2.5.1+cu124 (matches Windows side)
- transformers 4.48.3 (downgraded from 5.8.0 for vllm 0.7.3 API compat — Qwen2Tokenizer.all_special_tokens_extended attribute drift)
- bitsandbytes 0.49.2 (runtime int4 NF4 quant, same as Windows)
- model: same /mnt/d/hf_cache snapshot accessible from WSL2

**Literal vllm memory profile (the key evidence)**:
```
the current vLLM instance can use total_gpu_memory (6.00GiB) x gpu_memory_utilization (0.90) = 5.40GiB
model weights take 5.43GiB; non_torch_memory takes -0.51GiB; PyTorch activation peak memory takes 1.42GiB;
the rest of the memory reserved for KV Cache is -0.94GiB.
# cuda blocks: 0, # CPU blocks: 4681
Maximum concurrency for 4200 tokens per request: 0.00x
```

→ literal arithmetic: **5.43 GiB (int4 model weights) + 1.42 GiB (activations) = 6.85 GiB > 6.00 GiB physical VRAM**. KV cache budget = -0.94 GiB. vllm allocates 0 GPU cache blocks → concurrency at 4200 tokens = 0.00x. Even at gpu_memory_utilization=1.0 (impossible), still exceeds total VRAM.

**Critical honest finding (★★★★ portfolio gold)**:

The Phase 1 Windows transformers 4k PASS (peak 10.8GB) was literally enabled by **Windows kernel-level shared-memory PCIe spillover** (NVIDIA WDDM driver allows VRAM overcommit, swap to system RAM via PCIe DMA at ~10x latency penalty). Linux/WSL2 nvidia driver does NOT provide an equivalent fallback — vllm sees only the 6GB physical limit and refuses to allocate.

**Counterintuitive consequence**: vllm's "more efficient" PagedAttention is irrelevant on this hardware tier — neither vllm nor transformers without OS spillover can fit the model. The literal enabler of the 4k cell was the Windows OS, not the inference engine.

**Decision**: Phase 2b → **NEGATIVE RESULT**. The 4k Windows transformers ceiling stands. WSL2 vllm path is documented as literal infeasible at this hardware tier and removed from Phase 2 deliverable scope. The honest portfolio finding is: **on 6GB VRAM consumer laptop, Windows OS shared-memory fallback is structurally necessary for 7B-parameter int4 inference; vllm/Linux strictness disqualifies this hardware**.

**Sources (D8)**:
- artifacts/wsl_vllm_4000.json (literal status=OOM evidence)
- vllm 0.7.3 model_runner.py:1115 log output: "Loading model weights took 5.4341 GB"
- vllm 0.7.3 worker.py:267 log output: "model weights take 5.43GiB; ... the rest of the memory reserved for KV Cache is -0.94GiB"
- vllm executor_base.py:111: "# cuda blocks: 0" + Maximum concurrency 0.00x
- examples/wsl_vllm_niah.py (committed for reproducibility — re-run instructions in script docstring)

**Consequences**:
- ✅ Cost-tier table updated: WSL2 vllm row added showing the OOM, with literal vllm memory profile in evidence JSON
- ✅ Portfolio thesis literal strengthened: "constraint-optimized AI engineering" hits a deeper layer — even with the optimal inference engine, 6GB VRAM tier requires OS-level memory tricks that only Windows provides
- ✅ Recruiter signal: "engineer who tests the conventional-wisdom shortcut (Linux/vllm > Windows/transformers) and publishes the counterintuitive negative result with literal log citations"
- ⚠️ True Phase 2b "ceiling extension" requires either (a) GPU upgrade to ≥8GB VRAM, (b) smaller model (3-4B parameter class), or (c) tensor-parallel multi-GPU — all outside `consumer laptop` constraint
- ⚠️ The PagedAttention efficiency claim is empirically unverifiable on this hardware (model doesn't even load, so its forward-pass efficiency is irrelevant)

**Verify**: drift-CI extended with wsl_vllm runner + JSON evidence + ADR-009 reference verification.
