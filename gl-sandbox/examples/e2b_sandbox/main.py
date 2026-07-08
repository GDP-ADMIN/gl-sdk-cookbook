"""Run code in an E2B sandbox with gllm-tools.

Creates a managed E2B sandbox, executes a Python snippet and a shell command,
then terminates the sandbox.
"""

import asyncio
import os

from dotenv import load_dotenv
from gllm_tools.code_interpreter.code_sandbox.e2b_sandbox import E2BSandbox

load_dotenv()

CODE = """
import numpy as np
print("mean:", np.mean([1, 2, 3, 4]))
"""


async def run_code(sandbox: E2BSandbox) -> None:
    """Execute Python code and print the structured result."""
    result = await sandbox.execute_code(CODE)
    print(f"[code] status={result.status.value}")
    print(result.text)


async def run_command(sandbox: E2BSandbox) -> None:
    """Execute a shell command inside the sandbox."""
    result = await sandbox.execute_command("echo hello from $(hostname)")
    print(f"[command] status={result.status.value}")
    print(result.stdout)


async def main() -> None:
    """Create the sandbox, run the examples, and always clean up."""
    sandbox = await E2BSandbox.create(
        api_key=os.environ["E2B_API_KEY"],
        additional_packages=["numpy"],
    )
    try:
        await run_code(sandbox)
        await run_command(sandbox)
    finally:
        await sandbox.terminate()


if __name__ == "__main__":
    asyncio.run(main())
