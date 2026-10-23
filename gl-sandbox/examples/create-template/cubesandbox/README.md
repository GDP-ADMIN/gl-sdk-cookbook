# CubeSandbox Template Builder

Build a reusable **CubeSandbox warm snapshot** with packages baked in, then create a sandbox from
that predefined template using `gllm-tools`.

**Shows:** `CubeTemplateBuilder.ensure()` with a `TemplateSpec` (`image` + `packages`), and reusing
the returned reference as the `template` argument to `CubeSandbox.create()`.

**How it works:** The builder converts the image into a template, starts a sandbox from it, installs the
packages, and saves a **warm snapshot**: the running sandbox together with its memory, so every
sandbox created from it starts with the Python kernel already running. The `TemplateRef` value is
the snapshot *name*; on create, that name resolves to the newest ready snapshot, so the reference
stays stable across rebuilds. `ensure()` is idempotent: the first run builds the template (can
take several minutes), later runs skip straight to reuse.

## Prerequisites

- A **running CubeSandbox server** and an API key with template-build permission. The SDK reaches
  its API at `https://api.<CUBE_DOMAIN>`.
- Optionally, an image in `CUBE_IMAGE` to build from instead of the maintained
  `aip-agents-sandbox:base`. It must carry envd, CubeSandbox's command and file daemon, and the
  server must be able to pull it. The gllm-tools
  [Dockerfile template](https://github.com/GDP-ADMIN/gl-sdk/blob/main/libs/gllm-tools/gllm_tools/code_interpreter/code_template/dockerfile_template/README.md)
  adds envd in its Section 3b.
- `gllm-tools-binary` 0.3.1 or later, which this example pins.

> Needs `make` and `uv`. See the
> [GL Sandbox README](../../../README.md#installing-make) if `make` is missing.

## Quick Start

1. **Point at your server** — create a `.env`:

   ```bash
   cp .env.example .env
   # then fill in CUBE_DOMAIN and CUBE_API_KEY; CUBE_IMAGE is optional
   ```

2. **Install**

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
