# SETUP — Phase 1 install runbook

> consumer laptop (Windows 11 host + WSL2 Ubuntu for vllm) で zero-credit-card constraint 下に install する literal 手順。
> Linux / macOS native でも同等 path で再現可能 (vllm が直接 install 可能なため WSL2 step skip)。

## Prerequisites

- Windows 11 with WSL2 enabled (Ubuntu 22.04+)、 or Linux / macOS native
- Python 3.12+ (host + WSL2 両方)
- [uv](https://github.com/astral-sh/uv) installed
- Git
- D: drive (or any drive) with **≥25GB free** (15GB Qwen weight + 5GB venv + 5GB transient build)
- GitHub account with personal access token (for GitHub Models API, scope: minimal read; CC NOT required)

## Step 1. D: drive cache redirect (Windows host、 model weight 15GB をC: 外に置く)

```powershell
# Set persistent env vars (one-time setup)
[Environment]::SetEnvironmentVariable("HF_HOME", "D:\hf_cache", "User")
[Environment]::SetEnvironmentVariable("HF_HUB_CACHE", "D:\hf_cache\hub", "User")

# Restart PowerShell session, then verify:
echo $env:HF_HOME
# Expected: D:\hf_cache
```

## Step 2. Download Qwen2.5-7B-Instruct-1M weight (~15GB)

```powershell
# huggingface_hub の hf CLI (new CLI replaces deprecated huggingface-cli)
pip install --upgrade huggingface_hub  # 1.14+ で hf command available
hf download Qwen/Qwen2.5-7B-Instruct-1M --cache-dir "D:\hf_cache\hub"
```

**Time estimate**: 30 min - 2h depending on bandwidth.

**Verify**:
```powershell
Get-ChildItem "D:\hf_cache\hub\models--Qwen--Qwen2.5-7B-Instruct-1M\snapshots\" -Recurse | Measure-Object -Property Length -Sum | ForEach-Object { "Total: {0:N1} GB" -f ($_.Sum / 1GB) }
# Expected: ~15 GB
```

## Step 3. vllm install path

### Linux / macOS native

```bash
export UV_PROJECT_ENVIRONMENT=$HOME/venvs/longctx-bench-honest
cd /path/to/longctx-bench-honest
uv sync
```

### Windows: WSL2 path (vllm Windows native install historically unstable)

```bash
# In WSL2 Ubuntu shell:
sudo apt update && sudo apt install python3.12 python3.12-venv -y
# Install uv in WSL2
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone or access this repo from WSL2 (mounted Windows path or fresh clone)
cd /mnt/c/Users/admin/projects/portfolio/longctx-bench-honest
# or: git clone https://github.com/leagames0221-sys/longctx-bench-honest.git ~/longctx-bench-honest && cd ~/longctx-bench-honest

# vllm install (pin to current stable, lockfile will pin exact)
export UV_PROJECT_ENVIRONMENT=/mnt/d/venvs/longctx-bench-honest  # D: drive accessible from WSL2
uv sync
```

**Verify**:
```bash
uv run python -c "import vllm; print(vllm.__version__)"
```

ADR-005 (Phase 1 で literal 起草) に実測結果記録。

## Step 4. Supply chain audit

```bash
uv run pip-audit --strict
```

**Pass condition**: high severity 0 件。

## Step 5. GitHub Models token setup

1. Go to https://github.com/settings/tokens/new
2. Note: "GitHub Models access"
3. Expiration: 90 days
4. Scopes: `read:packages` (minimum for GitHub Models)
5. Generate, copy token

```powershell
# Save to .env (already in .gitignore)
"GITHUB_TOKEN=ghp_..." | Out-File .env -Encoding utf8 -NoNewline
```

## Step 6. Baseline run — Phase 1 + 2a actual delivery (not the original 128k goal)

> **Reproducibility note**: Phase 0/1 plan called for "RULER 128k subset baseline". Phase 1 measurement (ADR-007) showed this is **infeasible on 6GB VRAM** — the literal ceiling on RTX 3050 Laptop is ~4k tokens. SETUP.md Step 6 reflects what actually works on this hardware tier; the 128k goal is moved to Phase 4 candidate work (requires ≥24GB VRAM or paid cloud, both outside the constraint set).

### 6a. Local Windows transformers path (single-needle NIAH at 4k, the literal ceiling)

```powershell
# Windows host, after Steps 1-5 complete + uv sync ran with the pyproject.toml
# in this repo (which pins torch==2.5.1+cu124 + bitsandbytes==0.49.2 + transformers>=4.46 via the
# [tool.uv.sources] cu124 wheel index — same versions that produced artifacts/baseline_*.json).
$env:VIRTUAL_ENV = "D:\venvs\longctx-bench-honest"
uv run python examples/baseline_niah.py --context-tokens 4000 --depth-pct 50
# Expected: artifacts/baseline_4000.json with status="PASS", inference_sec ≈ 200-300s
```

To reproduce the literal ceiling characterization, also run 5k / 6k / 8k → expect status="OOM".

### 6b. Cloud comparison (GitHub Models, free tier)

```bash
# After Step 5 token setup, GITHUB_TOKEN env var set
uv run python examples/cloud_niah.py --model openai/gpt-4.1-mini --context-tokens 4000
uv run python examples/cloud_niah.py --model meta/llama-3.3-70b-instruct --context-tokens 4000
# Expected: artifacts/cloud_*.json with status="PASS", inference_sec ≈ 5-10s
```

### 6c. WSL2 vllm path (Phase 2b negative result — documented for completeness)

```bash
# Inside WSL2 Ubuntu after uv sync (which pins vllm==0.7.3 to match ADR-009 evidence):
uv run python examples/wsl_vllm_niah.py --context-tokens 4000
# Expected: artifacts/wsl_vllm_4000.json with status="OOM"
# vllm 0.7.3 on 6GB VRAM cannot fit Qwen 7B int4 + activations — see ADR-009 for the literal log evidence
# and 3 alternative causal hypotheses with falsification paths.
```

**Pass condition**: all 7 JSON evidence files materialize in `artifacts/` and match the status field claimed in README cost-tier table. drift-CI enforces this on every push.

## Step 7. Phase 1 commit

```bash
git add eval/ artifacts/baseline_128k.json
git commit -m "Phase 1: baseline 128k RULER subset run (Qwen2.5-7B-1M local, score X.XX%)"
git push
```

drift-check workflow will verify the baseline JSON exists.

## Cleanup (Phase 3 後)

```powershell
Remove-Item -Recurse -Force D:\hf_cache
Remove-Item -Recurse -Force D:\venvs\longctx-bench-honest
# WSL2 venv cleanup:
wsl rm -rf /mnt/d/venvs/longctx-bench-honest
```

Portfolio repo は GitHub に literal 残るので、 portfolio として常時稼働。 第三者が re-run したい時は本 SETUP.md の通り再 install。

## Troubleshooting

- **`hf download` fails with auth**: Qwen2.5-1M is public, but try `hf auth login` first
- **vllm install on Windows native fails**: confirmed unstable, use WSL2 path (ADR-005)
- **GPU VRAM OOM at 1M context**: try Q4 quant via vllm `--quantization fp8` flag, or reduce `--max-model-len`. Record in logbook.
- **GitHub Models rate limit hit**: space 4-model evals by ≥1 min, monitor `x-ratelimit-remaining` header
- **D: drive runs out during DL**: hf snapshot resumes on re-run, clean partial via `Remove-Item D:\hf_cache\hub\.incomplete\* -Recurse`
