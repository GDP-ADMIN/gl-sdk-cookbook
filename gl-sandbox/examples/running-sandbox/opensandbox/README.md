# OpenSandbox

Run code in a self-hosted [OpenSandbox](https://open-sandbox.io) instance using `gllm-tools`.

**Shows:** `OpenSandbox.create()` against a running server and `execute_code()`.

## Prerequisites

- A **running OpenSandbox server** reachable at `OPENSANDBOX_DOMAIN` (default `localhost:8080`).
  OpenSandbox runs your code in a Docker container, so you need Docker and the OpenSandbox
  runtime available. Start one locally, for example:

  ```bash
  docker run --rm -p 8080:8080 opensandbox/server:latest
  ```

  See the [OpenSandbox docs](https://github.com/alibaba/OpenSandbox) for the exact image and
  flags for your version.
- Access to the `gen-ai-internal` package index (a Google account with GDP Labs SDK access).

> Needs `make`, `uv`, and `gcloud` (run `gcloud auth login` once). See the
> [examples README](../README.md#installing-make) if `make` is missing.

## Quick Start

1. **Point at your server** — create a `.env`:

   ```bash
   echo 'OPENSANDBOX_DOMAIN="localhost:8080"' > .env
   # add OPENSANDBOX_API_KEY="..." if your server requires one
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
python: 3.12.x
sum: 45
```
