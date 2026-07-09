# GL Sandbox — Code Interpreter Examples

Runnable examples for the **code interpreter** capabilities of
[`gllm-tools`](https://gdplabs.gitbook.io/sdk) — executing untrusted code inside an isolated
sandbox, and pre-building reusable sandbox templates.

`gllm_tools.code_interpreter` exposes two layers:

- **`code_sandbox`** — backends that execute code in an isolated environment. Every backend
  returns the same `ExecutionResult` (`.status`, `.stdout`, `.stderr`, `.text`, `.error`), so
  your code stays backend-agnostic.
- **`code_template`** — build-time companions that bake dependencies into a reusable template
  (an E2B alias / OpenSandbox snapshot) so a sandbox can be created *predefined* and start ready.

## Examples


Examples are grouped by what they do: **`running-sandbox/`** executes code in a sandbox, and
**`create-template/`** pre-builds a reusable template first. Each group has one directory per
backend.

| Example                                                      | Demonstrates                                         | Prerequisites                       |
| -------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------- |
| [`running-sandbox/e2b`](./running-sandbox/e2b)               | Run code + shell commands on E2B                     | E2B API key                         |
| [`running-sandbox/opensandbox`](./running-sandbox/opensandbox) | Run code on a self-hosted OpenSandbox                | Running OpenSandbox server (Docker) |
| [`create-template/e2b`](./create-template/e2b)               | Build an E2B template, then create a sandbox from it | E2B API key                         |
| [`create-template/opensandbox`](./create-template/opensandbox) | Build an OpenSandbox snapshot, then create from it   | Running OpenSandbox server (Docker) |

## Shared setup

Every example ships a `Makefile` with three targets — `uv-auth`, `sync`, and `run`. All examples
resolve `gllm-tools` from the private **`gen-ai-internal`** uv index, which authenticates with a
short-lived Google access token; `make sync` mints that token from `gcloud` for you.

You need [`uv`](https://docs.astral.sh/uv/), the [`gcloud` CLI](https://cloud.google.com/sdk/docs/install),
and `make` (see [Installing make](#installing-make)). In each example directory:

1. **Authenticate once** (a Google account with GDP Labs SDK access):

   ```bash
   gcloud auth login
   ```
2. **Set the backend values** — create a `.env` with the keys that example needs, e.g.:

   ```bash
   echo 'E2B_API_KEY="..."' > .env          # E2B examples
   # or: echo 'OPENSANDBOX_DOMAIN="localhost:8080"' > .env   # OpenSandbox examples
   ```

   The uv-index credentials are handled by `make sync` — they do **not** go in `.env`.
3. **Install and run**

   ```bash
   make sync   # mints a gcloud token, then `uv sync`
   make run    # `uv run main.py`
   ```

## Installing make

`make` ships by default on most Linux distros and macOS. If `make --version` fails, install it:

- **macOS** — comes with the Xcode command-line tools:

  ```bash
  xcode-select --install
  ```

  Or via [Homebrew](https://brew.sh): `brew install make`.
- **Linux (Debian/Ubuntu)**: `sudo apt-get update && sudo apt-get install -y build-essential`
- **Linux (Fedora/RHEL)**: `sudo dnf install make` &nbsp;·&nbsp; **Arch**: `sudo pacman -S make`
- **Windows** — pick one:

  - [winget](https://learn.microsoft.com/windows/package-manager/): `winget install GnuWin32.Make`
  - [Chocolatey](https://chocolatey.org/): `choco install make`
  - [Scoop](https://scoop.sh/): `scoop install make`
  - Or run the examples inside **WSL** / **Git Bash**, where `make` is available as on Linux.

Verify with:

```bash
make --version
```

## Reference

- [GL SDK Documentation](https://gdplabs.gitbook.io/sdk)
- [E2B](https://e2b.dev/docs) · [OpenSandbox](https://github.com/alibaba/OpenSandbox)
