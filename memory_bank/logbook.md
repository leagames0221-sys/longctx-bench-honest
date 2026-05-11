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

---

## 2026-05-11 — Phase 1 prep: supply chain defense + D: disk redirect (session: portfolio-init)

**作業**:
- D: drive 環境変数 set (HF_HOME=D:\hf_cache + HF_HUB_CACHE=D:\hf_cache\hub) + D:\hf_cache\hub + D:\venvs dir 作成
- C: drive 45.6GB free (9.6%) = Windows safe zone 危険水域、 D: 182.7GB free で 15GB Qwen weight + 5GB venv literal 受け止め
- pyproject.toml skeleton 配置: vllm>=0.7 (Windows platform marker 除外、 WSL2 fallback ADR-005) + transformers>=4.46 + huggingface-hub>=0.26 + datasets>=3.0 + openai>=1.50 + matplotlib + seaborn + numpy + pandas + dev (pytest + pip-audit + ruff)
- .github/dependabot.yml 配線 (pip ecosystem + github-actions ecosystem、 weekly schedule)
- drift-check workflow 拡張: pyproject.toml metadata + dependabot.yml pip ecosystem + Disk layout + HF_HOME 文書化 + pip-audit declared の 4 step 追加 (15 step → 19 step)
- README 「Disk layout (consumer laptop constraint, 15GB model weight)」 section 追加、 D: redirect literal command + Lifecycle (Phase 2 後 D: 削除 OK) 明記

**Rationale (D8 source: WebSearch + WebFetch evidence)**:
- vllm Windows native install historically 不安定、 platform_system != 'Windows' marker で Linux/macOS のみ pip install、 Windows は WSL2 経由 (ADR-005 Phase 1 起草)
- 15GB Qwen 1M weight + 5GB vllm/torch deps + 5GB transient build = 合計 25GB、 C: 9.6% free では literal infeasible

**進捗**: Phase 1 prep 配線完了見込、 commit + push + drift-check 再 verify 待ち

**申し送り (次 session = Phase 1 heavy install)**:
- vllm install path 検証: Windows host で `uv sync` failure 確実視 → WSL2 fallback、 結果を ADR-005 literal 起草
- HF DL kickoff (background): `huggingface-cli download Qwen/Qwen2.5-7B-Instruct-1M` (~15GB、 D: hf_cache literal store、 数十分 order)
- RULER の `scripts/data/synthetic/{niah,qa,variable_tracking,common_words_extraction,freq_words_extraction}.py` + `synthetic.yaml` + `run.sh` を 自 repo `eval/ruler/` に literal copy
- LongBench の `pred.py` + `result.py` + `config/` + `prompts/` を 自 repo `eval/longbench/` に literal copy
- NIAH の `needlehaystack/` + `viz/` を 自 repo `eval/niah/` に literal copy (補助 heatmap)
- baseline 128k RULER subset (synthetic.yaml の 1 task で) 走行、 公式 reference 数値範囲内一致 verify
- GitHub Models sample API call (small context) で接続 + free tier rate limit 実測

---

## 2026-05-11 — Phase 1 extract: RULER + LongBench + NIAH 抽出 + NOTICE + SETUP + HF DL kickoff (session: portfolio-init)

**作業**:
- env verified: WSL2 Ubuntu v2 already installed ★★★ (vllm WSL2 path 即実行可能、 ADR-005 起草準備)、 huggingface_hub 1.10.2 (`hf` new CLI 使用、 `huggingface-cli` deprecated)
- prior art literal 抽出:
  - **RULER** (SHA `ab17b7853df4e0a30b78cd5d2b463ac7dff6ee13`、 Apache 2.0、 1,536★、 2025-11-13 push) → `eval/ruler/`、 14 files
    - `scripts/{synthetic.yaml, config_models.sh, config_tasks.sh, run.sh}`
    - `scripts/data/{manifest_utils, prepare, template, tokenizer}.py`
    - `scripts/data/synthetic/*.py` (13 task generators incl niah, qa, variable_tracking, etc.)
  - **LongBench** (SHA `2e00731f8d0bff23dc4325161044d0ed8af94c1e`、 MIT、 1,168★、 2025-01-15 push、 ACL 2025) → `eval/longbench/`、 10 files (pred.py + result.py + config/ + prompts/ + requirements.txt)
  - **NIAH** (SHA `7b90d285651b68d39a94f3d3bd3672f84192c989`、 MIT、 2,282★、 2024-08-17 push、 stale だが補助 visual valid) → `eval/niah/`、 69 files (viz/ + needlehaystack/ + requirements.txt)
- `NOTICE.md` 配置: 4 prior art (RULER + LongBench + NIAH + Qwen + vllm) attribution + audit log + license compatibility note
- `SETUP.md` 配置: Phase 1 install runbook (D: HF cache redirect + Qwen 1M DL + vllm WSL2 path + pip-audit + GitHub Models token + baseline 128k RULER subset)
- **HF DL kickoff (background)**: `hf download Qwen/Qwen2.5-7B-Instruct-1M --cache-dir D:\hf_cache\hub` 走行中、 fetching 15 files、 progress log: D:\hf_cache\dl_progress.log
  - symlink warning出力 (Windows native では non-symlink mode、 容量増 risk ★ 軽微)
  - bandwidth 次第で 30 min - 2h 程度の予測

**error**:
- 当初 `huggingface-cli` command が deprecated でexit 1 fail → `hf` new CLI に切替成功

**進捗**: Phase 1 extract + docs 配線完了見込、 HF DL 進行中 (30 min - 2h ETA)、 commit + push + drift-check verify 待ち。 vllm install (WSL2 経由) は ADR-005 起草と pair で次 session。

**申し送り (次 session)**:
- HF DL 完了 verify (`Get-ChildItem D:\hf_cache\hub\models--Qwen--Qwen2.5-7B-Instruct-1M -Recurse | Measure-Object -Property Length -Sum` で ~15GB 確認)
- WSL2 環境で uv sync (vllm + transformers + 他 deps install)、 ADR-005 「vllm WSL2 install path 確定」 を decisionLog 起草
- GitHub Models token 取得 (read:packages scope、 CC 不要)、 .env (.gitignore 済) に literal 保存
- baseline 128k RULER subset 走行 (1 task = niah_single_1 等)、 公式 RULER reference 数値範囲内一致 verify
- JSON evidence → `artifacts/baseline_128k.json` literal 保存、 logbook に summary append

---

## 2026-05-11 — Phase 1 install layer (Windows host portion): HF DL complete + uv sync + pip-audit (session: portfolio-init)

**作業 (literal 実測値で 全項 GREEN)**:
- **HF DL completed**: `hf download Qwen/Qwen2.5-7B-Instruct-1M --cache-dir D:\hf_cache\hub` → 12:16 duration、 14.22 GB literal 取得、 snapshot path: `D:\hf_cache\hub\models--Qwen--Qwen2.5-7B-Instruct-1M\snapshots\e28526f7bb80e2a9c8af03b831a9af3812f18fba`
- `uv sync --extra dev` (UV_PROJECT_ENVIRONMENT=D:\venvs\longctx-bench-honest) → exit 0、 全 deps install:
  - torch 2.11.0 + transformers 5.8.0 + safetensors 0.7.0 + tokenizers 0.22.2 + huggingface-hub + datasets + openai (GitHub Models 用) + matplotlib + seaborn + pandas + numpy + accelerate + 等
  - vllm は `platform_system != 'Windows'` marker で literal 除外 = Windows host で uv sync 通過 OK、 vllm 必要時は WSL2 path (ADR-005 起草対象)
- `uv run pip-audit --strict` → exit 0、 **"No known vulnerabilities found"** ★★★ (supply chain defense literal verified、 torch + transformers + 全 transitive deps clean)
- `uv.lock` 4909 行 生成 (D-NPM-3GUARD pip equivalent literal lockfile pin)

**重要 finding**:
- Windows host で transformers 5.8.0 + safetensors + huggingface-hub が動くことが verified = **vllm なしでも Qwen 2.5-1M モデル load + 推論可能** (transformers 経由、 vllm より遅いが host で完結)
- → Phase 1 baseline で **Windows host で transformers 経由 128k 推論** を試行する path が literal 可能、 WSL2 vllm install を Phase 2 まで literal 遅延可能
- ただし frontier 1M 真稼働は vllm + WSL2 が standard、 ADR-005 で literal 比較記録

**error**:
- 当初 `huggingface-cli download` で deprecation fail (exit 1) → `hf download` new CLI に切替成功 (logbook 前 entry 記載済)

**進捗**: Windows host portion 全 GREEN。 残 = WSL2 vllm install (Phase 2 移行で OK)、 GitHub Models token、 baseline 走行。

**申し送り (次 session)**:
- uv.lock commit + push、 drift-check 緑保持
- transformers 経由 sample inference 走行: `uv run python -c "from transformers import AutoModelForCausalLM, AutoTokenizer; ..."` で Qwen 2.5-1M load 確認 (128k context 程度から start)
- baseline 128k RULER subset 走行 (single niah task)、 JSON evidence 出力
- WSL2 vllm install は frontier 1M で必要時のみ Phase 2 内で execute、 ADR-005 で 「Windows host transformers vs WSL2 vllm の trade-off」 を literal 記録

---

## 2026-05-12 — Phase 1 partial: CUDA torch install + NIAH baseline scaling + 6GB VRAM ceiling literal characterized (session: portfolio-continue)

**作業 (literal 実測値)**:
- Hardware identified: NVIDIA RTX 3050 Laptop 6GB VRAM, CUDA driver 12.6, compute 8.6 (Ampere); host RAM (not measured this session)
- Replaced cpu-only torch 2.11.0 (from prior session) with **torch 2.5.1+cu124** + torchvision 0.20.1 via official PyTorch wheel index (security-audit OK: official Meta, BSD-3, 86k★, no PyPI typosquat surface)
- `bitsandbytes 0.49.2` installed (MIT, official, int4 NF4 standard) — security audit GREEN
- Authored `examples/baseline_niah.py` (decomposed prior art: PaulGraham haystack from gkamradt/NIAH MIT + RULER niah.py template Apache-2.0, lightweight self-contained ~150 lines)
- Created `artifacts/` dir for JSON evidence
- Ran 4-cell scaling experiment (RUN A-D below)

**実測値** (artifacts/baseline_{4000,5000,6000,8000}.json all committed):

| Run | context_tokens | actual_tokens | status | model_load_sec | inference_sec | peak_vram_gb | output |
|---|---|---|---|---|---|---|---|
| A | 4000 | 3851 | **PASS** | 74.45 | 251.89 | 10.80 | "2867825" (needle correct ★★★) |
| B | 5000 | 4850 | OOM | 66.34 | n/a | 11.18 (req 2.46 more) | n/a |
| C | 6000 | 5851 | OOM | 74.55 | n/a | 9.35 (req 3.57 more) | n/a |
| D | 8000 | 7851 | OOM | 66.93 | n/a | 6.15 (req 6.43 single-block) | n/a |

→ **Hard ceiling: ~4k tokens** on this hardware tier (RTX 3050 6GB Laptop + int4 NF4 Qwen2.5-7B-1M + Win shared-mem fallback).

**Honest finding (portfolio gold ★★★)**:
- 4k PASS uses Windows shared-mem PCIe spillover (peak 10.8GB on a 6GB GPU = 4.8GB system RAM borrowed via DMA — ~5-10x slower than native VRAM access, evidenced by 252s wall-time for what should be a sub-30s task on a workstation GPU)
- 5k+ OOM = shared-mem fallback exhausted; single attention forward pass requires more contiguous addressable memory than physically present
- This is the literal `constraint-optimized AI engineering` boundary — not a failure of the model, not a config error, just the literal physics of 7B params × KV cache vs 6GB VRAM

**Documentation updates (D3-DocSync, all in same commit)**:
- README Status: "Phase 0 closed → Phase 1 partial" with link to Honest results and ADR-007
- README Cost-tier table: 4 literal NIAH cells (4k PASS + 5k/6k/8k OOM) + 3 `infeasible at 6GB VRAM` cells (RULER / LongBench v2 / NIAH 128k+) + inference wall-time row + electricity cost row
- README Honest results: full populated section "Where the local 7B model holds up" / "Where the constraint literally hits" / "Where reasonable engineering fixes the gap" / "Where it doesn't"
- decisionLog ADR-007: literal 6GB VRAM ceiling characterization with citation chain (Qwen config + bitsandbytes + KV cache arithmetic)

**error**:
- 1st run: `device_map="auto"` triggered CPU offload error → fixed by `device_map={"": 0}` (force all on GPU 0)
- `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` is not supported on Windows (UserWarning emitted, ignored) — fragmentation workaround not available, but ceiling determined by literal physical limit not fragmentation
- transformers `torch_dtype` deprecation warning (non-fatal, future-proofed by passing kwarg in legacy form)

**進捗**: Phase 1 partial 完了 — install layer + baseline runner + 4-cell JSON evidence + README + ADR-007 全件 literal commit 待ち。 drift-CI extension は本 commit 後の next iteration で artifact 存在 verify 追加予定。

**申し送り (next session = cloud frontier comparison)**:
- Phase 2 entry: GitHub Models endpoint (https://models.github.ai/inference) 経由で同 NIAH @ 4k task を GPT-5 / Claude Sonnet 4.6 / Llama 3.3 で literal 並列走行 → cost-tier table 4 model × 4k cell literal populate
- token gh auth (`gh auth token`) → .env (gitignore済) → openai SDK base_url 経由
- 8000 token request cap 制約は browser-agent-demo v5 で既 evidence、 4k input + ~100 output = 4100 token は free-tier cap 内 ★★★
- WSL2 + vllm PagedAttention path は Phase 2 後半 candidate (ceiling 8-16k へ literal push 可否 verify)
- craftstack 統合 (Phase 3) は cloud cells populate 後


---

## 2026-05-12 — Phase 2a: Cloud comparison via GitHub Models free tier (session: portfolio-continue)

**作業**:
- GitHub Models catalog API literal probe (`https://models.github.ai/catalog/models`) — enumerated full model list
- Wrote `examples/cloud_niah.py` — OpenAI SDK + GitHub Models endpoint, same NIAH single-needle task as baseline_niah.py
- Ran 6 cloud cells: 4 models × {2k, 4k} subset, captured literal API responses to JSON evidence

**実測値 (artifacts/cloud_*.json all committed)**:

| Model | 2k | 4k |
|---|---|---|
| openai/gpt-4.1-mini | (not run, 4k is primary) | **PASS 8.54s** (prompt=3723 tok) |
| meta/llama-3.3-70b-instruct | (not run, 4k is primary) | **PASS 5.17s** (prompt=3856 tok) |
| openai/gpt-5 | **UNAVAILABLE** ("Unavailable model: gpt-5") | **TOKEN_LIMIT** ("Max size: 4000 tokens") |
| deepseek/deepseek-v3-0324 | **PASS 1.72s** (prompt=1832 tok) | **TOKEN_LIMIT** ("Max size: 4000 tokens") |

**Honest findings ★★★★**:
1. **Anthropic Claude is NOT in GitHub Models catalog** — full enumeration shows zero Anthropic models. Plan-original "Claude Sonnet" cell literal unreachable under zero-CC.
2. **gpt-5 returns `unavailable_model` even at 2k tokens** — catalog-listed but inference-blocked on free tier (likely needs paid Azure OpenAI / GitHub Enterprise tier)
3. **Free-tier token cap differs per model tier**: gpt-4.1-mini ("low") + llama-3.3-70b ("high") = ≥4000 tokens passable; gpt-5 ("custom") + deepseek-v3 ("high") = literal 4000 token hard cap (error: tokens_limit_reached / Max size: 4000 tokens)
4. **Cloud is 30-50x faster than local Qwen 4k**: gpt-4.1-mini 8.54s, llama-3.3-70b 5.17s, deepseek-v3 1.72s (at 2k) vs Qwen 4k local 251.89s

**Documentation updates (D3-DocSync)**:
- README Status: Phase 2a section added with substituted cloud model selection rationale
- README Cost-tier table: 5-column layout (Qwen local + 4 cloud), 9 row literal cells filled with PASS/TOKEN_LIMIT/UNAVAILABLE + JSON URL citations
- README new section: "Cloud free-tier honest map (Phase 2a evidence)" with full accessibility matrix
- decisionLog ADR-008: model selection substitution + literal API response citation chain
- drift-CI: 3 new step (cloud_niah.py exists + 6 cloud JSON evidence + 5 status field verify + README/ADR-008 section verify)

**error**:
- gpt-5 @ 4k: TOKEN_LIMIT (expected, prompt 3851 + chat template > 4000)
- gpt-5 @ 2k: UNAVAILABLE_MODEL (literal, even within token cap — model is inaccessible on free tier)
- deepseek-v3 @ 4k: TOKEN_LIMIT (literal hard 4000 cap)
- Initial plan referenced "Claude Sonnet" — literal absent from catalog, no fix possible without paid Anthropic API (out of scope)

**進捗**: Phase 2a 完遂、 cost-tier table 5 column × 9 row literal populated, drift-CI extended, commit + push 待ち

**申し送り (Phase 2b = WSL2 vllm experiment)**:
- WSL2 Ubuntu 既 install 済 (前 session evidence: huggingface_hub literal callable from WSL2 env)
- vllm PagedAttention は Linux 専用、 WSL2 install path で 6GB VRAM ceiling を 4k → 8-16k に literal 押し上げ可能性 ★ (★★ tier confidence、 PagedAttention KV cache 効率 vs transformers bitsandbytes 差分)
- 試行 → 結果 (PASS or FAIL) を ADR-009 として literal 記録、 cost-tier table の 8k+ cell 更新 候補

**申し送り (Phase 3 = craftstack 統合)**:
- craftstack repo (leagames0221-sys/craftstack) 確認 + 上位 fold に 2 repo link + thesis 1 行
- cost-tier summary 表 embed (本 repo + browser-agent-demo 双方 evidence URL)


---

## 2026-05-12 — Phase 2b: WSL2 + vllm experiment, NEGATIVE RESULT (session: portfolio-continue)

**作業**:
- WSL2 Ubuntu 24.04 startup + verify (CUDA driver 12.6 passthrough working, nvidia-smi inside WSL2 reports same RTX 3050 6GB)
- Installed uv (curl-based, ~5MB) + created Python 3.12 venv at ~/longctx-wsl/.venv (WSL2 native filesystem, 954GB free)
- Installed vllm 0.20.2 first, hit driver compat error (vllm-bundled torch 2.11.0 requires CUDA 12.8+ driver)
- Downgraded to vllm 0.7.3 + torch 2.5.1+cu124 (matches Windows side)
- Hit transformers 5.x API incompat with vllm 0.7.3 (`Qwen2Tokenizer.all_special_tokens_extended` attribute drift)
- Downgraded transformers to 4.48.3 (vllm 0.7.3 contemporaneous version)
- Installed bitsandbytes 0.49.2 in WSL2 venv (Win venv install doesn't carry over)
- Wrote examples/wsl_vllm_niah.py (parallel to Win baseline_niah.py, uses vllm.LLM with bnb int4)

**実測値 (artifacts/wsl_vllm_4000.json)** — the killer line is the vllm memory profile log:

```
the current vLLM instance can use total_gpu_memory (6.00GiB) x gpu_memory_utilization (0.90) = 5.40GiB
model weights take 5.43GiB; non_torch_memory takes -0.51GiB; PyTorch activation peak memory takes 1.42GiB;
the rest of the memory reserved for KV Cache is -0.94GiB.
# cuda blocks: 0, # CPU blocks: 4681
Maximum concurrency for 4200 tokens per request: 0.00x
```

Status: OOM at engine init (before any inference). Literal cause: int4 model weights (5.43 GiB) + activations (1.42 GiB) = 6.85 GiB > 6.00 GiB total VRAM. KV cache budget = literal **negative** 0.94 GiB. vllm allocated 0 GPU cache blocks; concurrency = 0.00x.

**Honest finding (★★★★ critical portfolio insight)**:
- Phase 1 Windows transformers 4k PASS used **Windows kernel-level shared-memory PCIe spillover** (WDDM driver overcommit) to absorb the 10.8GB peak on a 6GB GPU
- Linux nvidia driver does NOT provide an equivalent fallback
- → vllm sees only physical 6GB and refuses to allocate
- → The literal enabler of Phase 1's 4k cell was the **Windows OS**, not the inference engine
- → "Linux/vllm > Windows/transformers for memory efficiency" is literal disproven at this hardware tier

**Documentation updates (D3-DocSync)**:
- README Status: "Phase 2b (NEGATIVE RESULT, sourced)" section added with vllm memory profile evidence
- README Hardware constraint section: WSL2 + vllm negative test result added with ADR-009 link
- decisionLog ADR-009: full vllm memory profile log + Windows shared-mem causal hypothesis + sourced from vllm 0.7.3 log lines (model_runner.py:1115, worker.py:267, executor_base.py:111)
- drift-CI: 1 new step (wsl_vllm_niah.py + JSON evidence + ADR-009 + README link)

**error**:
- vllm 0.20.2 → driver 12.6 incompat (needed 12.8+) → downgraded vllm
- vllm 0.7.3 → transformers 5.x API drift → downgraded transformers
- vllm 0.7.3 → missing bitsandbytes in WSL2 venv → installed
- vllm 0.7.3 → OOM at engine init (the literal honest result, not an install error)

**進捗**: Phase 2b complete with sourced negative result. Total Phase 1+2 deliverable: **3 ADR (007, 008, 009) + 9 JSON evidence files (4 Win local + 6 cloud + 1 WSL vllm) + 3 runners (baseline_niah / cloud_niah / wsl_vllm_niah) + README cost-tier 5-column table populated + Cloud free-tier honest map section + drift-CI 22+ steps green**.

**申し送り (Phase 3 = craftstack 統合、 next session 推奨)**:
- craftstack repo (leagames0221-sys/craftstack) literal locate + scope assessment
- 上位 fold に thesis 1 行 + 2 repo link (browser-agent-demo + longctx-bench-honest)
- Cost-tier summary table embed (本 repo の 5-column matrix + browser-agent-demo の 5 layer journey)
- Phase 3 完了後: r/LocalLLaMA + HN post drafting (thesis = "constraint-optimized AI engineering: literal map of the consumer-laptop intersection")


---

## 2026-05-12 — Phase 3: craftstack integration PR opened (session: portfolio-continue)

**作業**:
- craftstack repo (leagames0221-sys/craftstack) literal probed via gh api (no local clone, C: disk 9.6% free 保護)
- 発見: craftstack matured into production-grade Next.js 16 monorepo (Boardly + Knowlex), 67 ADRs, 276 Vitest + 24 Playwright, branch protection on main per their ADR-0058
- Phase 3 plan re-scoped: 「上位 fold link」 → 「## Related portfolio work」 section addition near bottom (before License), via PR workflow (branch protection enforce)
- Built insertion via Python helper (avoid command-line base64 size limit for gh api PUT)
- PR opened: https://github.com/leagames0221-sys/craftstack/pull/70

**Section content (literal added to craftstack/README.md)**:
- 2-row table linking browser-agent-demo + longctx-bench-honest with thesis-aligned summaries
- Cross-repo unifying thesis paragraph: "constraint-optimized engineering — craftstack answers for full-stack web; the two siblings answer for AI engineering"
- All 3 sibling ADR links (ADR-006 / 007 / 008 / 009) literal cited

**error**:
- gh api PUT with --raw-field hit "Argument list too long" (40KB base64 content > shell arg limit) → switched to --input JSON file workflow (clean)
- Python `python3` on Git Bash returned exit 49 + /tmp path resolution mismatch (Windows Python sees \tmp not /tmp) → wrote helper script to %TEMP% explicitly

**進捗**: PR open + CI running (Vercel preview + lint/typecheck/test/build + doc drift detect + knowlex integration + a11y + CodeQL all queued/running). User self-merge after CI green.

**Final Phase 1+2+3 deliverable summary (★★★ tier portfolio)**:
- **3 ADRs**: ADR-007 (Win 6GB VRAM ceiling 4k) + ADR-008 (cloud free-tier honest map, Claude absent, gpt-5 unavailable, 4000-token cap) + ADR-009 (WSL2 vllm cannot fit weights+activations on 6GB, Windows shared-mem was the literal enabler)
- **11 JSON evidence files**: 4 Win local (4k/5k/6k/8k) + 6 cloud (gpt-4.1-mini/gpt-5×2/llama-3.3-70b/deepseek-v3×2) + 1 WSL2 vllm
- **3 runners**: examples/baseline_niah.py (Win transformers) + cloud_niah.py (GitHub Models) + wsl_vllm_niah.py (WSL2 vllm)
- **README**: Status section literal updated with Phase 1/2a/2b each, 5-column cost-tier transparency table (Qwen local + 4 cloud), Honest results full populated, Cloud free-tier honest map new section
- **drift-CI**: 22+ verify steps green (license + tier 2 + memory bank + cost-tier + honest results + selected under + why best + pyproject + dependabot + disk layout + pip-audit + 4 baseline cells + cloud runner + 6 cloud cells + cloud section + WSL vllm + ADR-007/008/009)
- **Cross-repo integration**: craftstack PR #70 open, linking both AI-eng portfolio siblings with thesis-aligned 2-row summary table

**Total session output (this 1 conversation)**:
- 6+ git commits to longctx-bench-honest
- 1 PR opened to craftstack
- 0 credit card transactions, 0 paid API usage, 0 supercomputer / non-consumer hardware
- All work literal reproducible from public sources

