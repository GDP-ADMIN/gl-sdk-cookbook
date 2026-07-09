# E2B Template Builder

Build a reusable **E2B template** with packages baked in, then create a sandbox from that
predefined template using `gllm-tools`.

**Shows:** `E2BTemplateBuilder.ensure()` with a `TemplateSpec` (image + `packages`), and reusing
the returned `TemplateRef` as the `template` argument to `E2BSandbox.create()`.

**Why templates?** Baking dependencies into a template once means every sandbox created from it
starts ready — no per-run `pip install`. `ensure()` is idempotent: the first run builds the
template (can take a few minutes), later runs skip straight to reuse.

## Prerequisites

- An E2B API key ([dashboard](https://e2b.dev/dashboard)).
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

The first run builds the template (streaming build logs); subsequent runs report `skipped`.

```
[template] status=success ref=gllm-tools-pandas
[code] status=success
pandas: 2.x.x
6
```
