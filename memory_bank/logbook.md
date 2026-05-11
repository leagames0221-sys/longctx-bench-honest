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
