# CubeSandbox Template Builder

Build a reusable **CubeSandbox warm snapshot** with packages baked in, then create a sandbox from
that predefined template using `gllm-tools`.

**Shows:** `CubeTemplateBuilder.ensure()` with a `TemplateSpec` (`image` + `packages`), and reusing
the returned reference as the `template` argument to `CubeSandbox.create()`.

**How it works:** CubeSandbox has no default template, so every sandbox starts from one you
build. The builder converts the image into a template, starts a sandbox from it, installs the
packages, and saves a **warm snapshot**: the running sandbox together with its memory, so every
sandbox created from it starts with the Python kernel already running. The `TemplateRef` value is
the snapshot *name*; on create, that name resolves to the newest ready snapshot, so the reference
stays stable across rebuilds. `ensure()` is idempotent: the first run builds the template (can
take several minutes), later runs skip straight to reuse.

## Prerequisites

- A **running CubeSandbox server** and an API key with template-build permission. The SDK reaches
  its API at `https://api.<CUBE_DOMAIN>`.
- A **container image that carries envd**, CubeSandbox's command and file daemon, pushed to a
  registry the server can pull from. Build it from the gllm-tools
  [Dockerfile template](https://github.com/GDP-ADMIN/gl-sdk/blob/main/libs/gllm-tools/gllm_tools/code_interpreter/code_template/dockerfile_template/README.md),
  which adds envd in its Section 3b.
- `gllm-tools` 0.3.0 or later, which this example pins.
- Access to the `gen-ai-internal` package index (a Google account with GDP Labs SDK access).

> Needs `make`, `uv`, and `gcloud` (run `gcloud auth login` once). See the
> [GL Sandbox README](../../../README.md#installing-make) if `make` is missing.

## Quick Start

1. **Point at your server and image** — create a `.env`:

   ```bash
   cp .env.example .env
   # then fill in CUBE_DOMAIN, CUBE_API_KEY, and CUBE_IMAGE
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

The first run builds the template (can take several minutes); later runs report `skipped`.

```
[template] status=success ref=gllm-tools-pandas
[code] status=success
pandas: 2.x.x
6
```

Use `gllm-tools-pandas` as `CUBE_TEMPLATE` in [`running-sandbox/cubesandbox`](../../running-sandbox/cubesandbox).
