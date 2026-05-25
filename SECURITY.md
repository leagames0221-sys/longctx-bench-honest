# Security policy — longctx-bench-honest

`longctx-bench-honest` is a portfolio-scope long-context LLM benchmark with
JSON-evidence backing and drift-CI claim verification. The dependency surface
(pip + GitHub Actions) is significant (torch + vllm + transformers + bitsandbytes
+ accelerate) and the surrounding ecosystem is under active supply-chain attack,
so this repo applies the following free defense layers.

## Supply-chain defense layers

Following the ongoing Shai-Hulud / Mini Shai-Hulud / TeamPCP worm waves
(Sep 2025 → May 2026, > 400 packages compromised across at least 5 distinct
campaigns, and Mini Shai-Hulud May 2026 = first known simultaneous npm + PyPI
campaign), this repo applies the following free, no-paid-service defense
layers:

| Layer | Implementation | Effect |
| --- | --- | --- |
| Cooldown (Dependabot side) | `.github/dependabot.yml` `cooldown:` with 5 / 7 / 14 day gates per semver level, applied to pip + github-actions ecosystems | Defers automated update PRs until the cooldown window clears. Absorbs essentially all known supply-chain attack lifetimes (axios 2026-03 = 4-5 h yank; Shai-Hulud TanStack 2026-05 = 22-min publish burst). |
| pip-audit gate | `pip-audit --strict` in CI (existing) | Fails on any PyPI advisory at the install-time vulnerability DB. |
| Drift-CI claim verifier | `.github/workflows/drift-check.yml` (existing) | Catches silent dependency drift via README ↔ repo state cross-check. |
| JSON evidence pinning | Every numeric claim in README is backed by `artifacts/*.json` literal evidence | A compromised dep cannot silently change reported numbers without the JSON evidence cells being regenerated. |
| Lockfile pin | `uv.lock` (Phase 1+) committed | Reproducible installs across environments. |

Primary sources:

- Dependabot `cooldown:` shipped 2025-07-01 ([GitHub Changelog](https://github.blog/changelog/2025-07-01-dependabot-supports-configuration-of-a-minimum-package-age/)).
- 7-day window rationale: [cooldowns.dev](https://cooldowns.dev/).
- Mini Shai-Hulud May 2026 = first npm + PyPI joint campaign: [Snyk](https://snyk.io/blog/mini-shai-hulud-antv-npm-supply-chain-attack/).

## Reporting a vulnerability

If you believe you have found a security vulnerability in `longctx-bench-honest`,
please **do not file a public GitHub issue**. Instead open a private security
advisory at <https://github.com/leagames0221-sys/longctx-bench-honest/security/advisories/new>.

This is a portfolio project, not a supported product. Maintainer response is
best-effort, target acknowledgement within 7 days.

## Scope

In scope:

- Supply-chain risk in repo dependencies (pip + GitHub Actions).
- Claim drift in README that could mislead reviewers.
- Credential leak via commit / artifact.

Out of scope:

- Vulnerabilities in upstream torch / vllm / transformers / Qwen model weights — please report those upstream.
- Issues that only manifest with non-default configuration explicitly forbidden by `CLAUDE.md`.
