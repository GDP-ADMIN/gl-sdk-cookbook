# CubeSandbox

Run code in a self-hosted [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) sandbox using
`gllm-tools`.

**Shows:** `CubeSandbox.create()` from an existing template, `execute_code()`, and
`execute_command()`.

## Prerequisites

- A **running CubeSandbox server** and an API key for it. The SDK reaches its API at
  `https://api.<CUBE_DOMAIN>`.
- A **CubeSandbox template**. CubeSandbox has no default template, so build one first with
  [`create-template/cubesandbox`](../../create-template/cubesandbox) and use its name
  (`gllm-tools-pandas`), or use a template your team has already built.
- `gllm-tools` 0.3.0 or later, which this example pins.
- Access to the `gen-ai-internal` package index (a Google account with GDP Labs SDK access).

> Needs `make`, `uv`, and `gcloud` (run `gcloud auth login` once). See the
> [GL Sandbox README](../../../README.md#installing-make) if `make` is missing.

## Quick Start

1. **Point at your server and template** — create a `.env`:

   ```bash
   cp .env.example .env
   # then fill in CUBE_DOMAIN, CUBE_API_KEY, and CUBE_TEMPLATE
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
python: 3.x.x
sum: 45
[command] status=success
hello from <sandbox-hostname>
```
