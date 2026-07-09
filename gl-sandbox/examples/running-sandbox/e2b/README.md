# E2B Sandbox

Run code in a managed [E2B](https://e2b.dev) sandbox using `gllm-tools`.

**Shows:** `E2BSandbox.create()`, `execute_code()`, `execute_command()`, and installing
extra packages with `additional_packages`.

## Prerequisites

- An E2B API key ([dashboard](https://e2b.dev/dashboard)). E2B is a SaaS backend, so no local1
  infrastructure is needed.
- Access to the `gen-ai-internal` package index (a Google account with GDP Labs SDK access).

> Needs `make`, `uv`, and `gcloud` (run `gcloud auth login` once). See the
> [examples README](../README.md#installing-make) if `make` is missing.

## Quick Start

1. **Set your API key** — create a `.env`:

   ```bash
   echo 'E2B_API_KEY="..."' > .env
   ```

2. **Authenticate the package index & install** (mints a gcloud token for you):

   ```bash
   make sync
   ```

3. **Run**

   ```bash
   make run
   ```

## Expected output

```
[code] status=success
mean: 2.5
[command] status=success
hello from <sandbox-hostname>
```
