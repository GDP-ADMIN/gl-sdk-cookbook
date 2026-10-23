# CubeSandbox

Run code in a self-hosted [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) sandbox using
`gllm-tools`.

**Shows:** `CubeSandbox.create()` with the default template, `execute_code()`, and
`execute_command()`.

## Prerequisites

- A **running CubeSandbox server** and an API key for it. The SDK reaches its API at
  `https://api.<CUBE_DOMAIN>`.
- Optionally, a **CubeSandbox template** in `CUBE_TEMPLATE`, such as `gllm-tools-pandas` from
  [`create-template/cubesandbox`](../../create-template/cubesandbox). Without one, the sandbox
  starts from the default template `glsandbox-base`. The first run on a server builds it, which
  takes several minutes and needs an API key with template-build permission.
- `gllm-tools-binary` 0.3.1 or later, which this example pins.

> Needs `make` and `uv`. See the
> [GL Sandbox README](../../../README.md#installing-make) if `make` is missing.

## Quick Start

1. **Point at your server** — create a `.env`:

   ```bash
   cp .env.example .env
   # then fill in CUBE_DOMAIN and CUBE_API_KEY; CUBE_TEMPLATE is optional
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

```
[code] status=success
python: 3.x.x
sum: 45
[command] status=success
hello from <sandbox-hostname>
```
