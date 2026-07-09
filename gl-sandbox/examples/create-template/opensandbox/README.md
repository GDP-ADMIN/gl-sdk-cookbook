# OpenSandbox Template Builder

Build a reusable **OpenSandbox snapshot** with packages installed, then create a sandbox from
that predefined snapshot using `gllm-tools`.

**Shows:** `OpenSandboxTemplateBuilder.ensure()` with a `TemplateSpec` (base `image` +
`packages`), and reusing the returned reference as `snapshot_name` in `OpenSandbox.create()`.

**How it works:** OpenSandbox has no Dockerfile build. Instead the builder spins up a disposable
sandbox from the base image, installs the packages live, and captures a persistent **snapshot**.
The `TemplateRef` value is the snapshot *name*; on create, that name resolves to the newest
`Ready` snapshot *id*, so the reference stays stable across rebuilds.

## Prerequisites

- A **running OpenSandbox server** reachable at `OPENSANDBOX_DOMAIN` (default `localhost:8080`),
  with Docker and the OpenSandbox runtime available. See the
  [OpenSandbox docs](https://github.com/alibaba/OpenSandbox).
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

The first run builds the snapshot (can take a minute); later runs report `skipped`.

```
[template] status=success ref=gllm-tools-requests
[code] status=success
requests: 2.x.x
```
