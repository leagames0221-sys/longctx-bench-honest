# Social distribution drafts

Drafts ready to copy-paste into r/LocalLLaMA and Hacker News when ready to submit. Both written in English (target audience). Substance over hype, negative findings surfaced first.

---

## r/LocalLLaMA post

**Suggested title** (pick one, both literal honest):
- `Honest 6GB-VRAM long-context map: Qwen2.5-7B-1M caps at 4k on RTX 3050, Linux/vllm fails harder than Windows`
- `Counterintuitive: WSL2 + vllm cannot fit Qwen2.5-7B-1M on 6GB VRAM where Windows transformers can`

**Suggested flair**: Discussion / Resources

**Body**:

```markdown
TL;DR — I tried to run Qwen2.5-7B-Instruct-1M on a consumer laptop (RTX 3050 Laptop 6GB VRAM) and mapped the literal feasibility frontier. All evidence in JSON, drift-CI enforced. Three honest findings:

1. **4k context = the hard ceiling** on Windows transformers + bitsandbytes int4 NF4. 5k, 6k, 8k all OOM at the first attention forward pass. The 4k cell passes only because Windows kernel shared-memory PCIe spillover (WDDM overcommit) lets allocations spill to system RAM at ~10x latency tax — peak measured 10.8GB on a 6GB GPU.

2. **WSL2 + vllm cannot even fit the model.** vllm 0.7.3 memory profile literal log: "model weights take 5.43GiB; PyTorch activation peak memory takes 1.42GiB; the rest of the memory reserved for KV Cache is **-0.94GiB**". 0 GPU cache blocks allocated, 0.00x concurrency at 4200 tokens. Linux nvidia driver does not provide an equivalent shared-mem fallback — vllm sees only physical 6GB and refuses. The conventional wisdom "vllm > transformers for memory efficiency" is literal disproven at this hardware tier: it fails harder because Windows OS was the enabler, not the inference engine.

3. **Cloud free-tier is also capped, and unevenly.** GitHub Models free tier (zero credit card, gh OAuth only): gpt-4.1-mini PASS @ 4k in 8.54s (~30x faster than local). llama-3.3-70b-instruct PASS @ 4k in 5.17s. But: **gpt-5 returns `unavailable_model` at any context size** on free tier. DeepSeek-V3 + gpt-5 are capped at literal 4000 input tokens. And Anthropic Claude is **not in the GitHub Models catalog at all** — zero CC + Claude = no path.

Full numbers + 11 JSON evidence cells + 3 ADRs at: https://github.com/leagames0221-sys/longctx-bench-honest

Hardware: RTX 3050 Laptop 6GB / driver 560.94 / CUDA 12.6 / Windows 11 + WSL2 Ubuntu 24.04. Software: torch 2.5.1+cu124, transformers (5.8.0 Win / 4.48.3 WSL), bitsandbytes 0.49.2, vllm 0.7.3. Everything fully reproducible — uv.lock committed, runners under examples/.

Related sibling repo for browser RPA on the same constraints (5-layer defense-in-depth journey, 5 honest failures with JSON): https://github.com/leagames0221-sys/browser-agent-demo

Cross-repo thesis is "constraint-optimized AI engineering": map the literal feasibility frontier under (zero credit card, consumer laptop, public OSS only, drift-CI enforced) and publish both the working zone AND the boundary. Happy to answer questions about the methodology or specific runner code.
```

**Subreddit rules check** (verify before posting):
- Self-promotion: substantive technical content + reproducible code → OK in r/LocalLLaMA (community values honest negative results)
- Flair must be set
- Title shouldn't editorialize too hard

---

## Hacker News post

**Submission type**: Show HN

**Title** (under 80 chars, pick one):
- `Show HN: Honest 6GB-VRAM map for Qwen2.5-7B-1M (4k local ceiling, sourced)`
- `Show HN: Constraint-optimized AI engineering portfolio under zero credit card`

**URL**: https://github.com/leagames0221-sys/longctx-bench-honest

**First comment** (post immediately after submission to provide context — HN convention):

```markdown
Author here. This is the long-context measurement repo in a 3-repo constraint-optimized AI engineering portfolio. The constraints are explicit: zero credit card, consumer laptop only (RTX 3050 Laptop 6GB), public OSS only, drift-CI enforced. The thesis is to map both what works AND the literal boundary, with JSON evidence for every numeric claim.

Three findings I think the community might find useful or counterintuitive:

1. The 4k single-needle PASS on Windows transformers depends on Windows kernel shared-memory PCIe spillover (peak 10.8GB on a 6GB GPU, ~10x latency tax). The model itself supports 1M context per its config.json — the bottleneck is purely VRAM + KV cache arithmetic.

2. WSL2 + vllm CANNOT fit the same model on the same hardware. vllm 0.7.3 memory profile shows weights 5.43GiB + activation peak 1.42GiB > 6.00GiB total, KV cache budget literal -0.94GiB. Linux/nvidia has no equivalent shared-mem fallback. This is the opposite of conventional wisdom that "vllm is more memory-efficient than transformers".

3. GitHub Models free tier is uneven: gpt-4.1-mini and llama-3.3-70b reachable at 4k in 5-9 seconds. gpt-5 returns "unavailable_model" regardless of context size. DeepSeek-V3 and gpt-5 are capped at literal 4000 input tokens. Anthropic Claude is not in the catalog at all.

All three findings come from literal API responses + vllm log output, citation chain in 3 ADRs (007, 008, 009). The drift-CI on the repo enforces that every numeric claim in the README matches the JSON evidence — including the OOM cells.

Companion repo (browser RPA under the same constraints, 5-layer defense journey with 5 honest failures): https://github.com/leagames0221-sys/browser-agent-demo

Happy to discuss the methodology or the counterintuitive WSL2/vllm result specifically.
```

**HN etiquette**:
- Post in the morning US time (Tue-Thu) for max visibility
- Don't post and immediately upvote (HN flags this)
- Engage with first 5-10 comments within an hour of posting
- If it dies on first attempt, can repost after a few weeks per HN's "second chance" pool

---

## What user does

1. **r/LocalLLaMA**: log in to reddit → r/LocalLLaMA → New Post → paste title + body → set flair → submit
2. **Hacker News**: log in to HN → submit page → paste title + URL → after submission, click your post → paste the first comment

Total time: ~5 minutes per submission. Best timing: Tuesday-Thursday US morning.
