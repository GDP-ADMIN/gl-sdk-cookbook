"""Run code in a CubeSandbox sandbox with gllm-tools.

Creates a sandbox from the default CubeSandbox template, or from CUBE_TEMPLATE
when it is set, executes a Python snippet and a shell command, then terminates
the sandbox.
"""

import asyncio
import os

from dotenv import load_dotenv
from gllm_tools.code_interpreter.code_sandbox.cube_sandbox import CubeSandbox

load_dotenv()

CODE = """
import sys
print("python:", sys.version.split()[0])
print("sum:", sum(range(10)))
"""


async def run_code(sandbox: CubeSandbox) -> None:
    """Execute Python code and print the structured result."""
    result = await sandbox.execute_code(CODE)
    print(f"[code] status={result.status.value}")
    print(result.text)


async def run_command(sandbox: CubeSandbox) -> None:
    """Execute a shell command inside the sandbox."""
    result = await sandbox.execute_command("echo hello from $(hostname)")
    print(f"[command] status={result.status.value}")
    print(result.stdout)


async def main() -> None:
    """Create the sandbox, run the examples, and always clean up."""
    sandbox = await CubeSandbox.create(
        api_key=os.environ["CUBE_API_KEY"],
        domain=os.environ["CUBE_DOMAIN"],
        template=os.getenv("CUBE_TEMPLATE") or None,  # None uses the default template
    )
    try:
        await run_code(sandbox)
        await run_command(sandbox)
    finally:
        await sandbox.terminate()


if __name__ == "__main__":
    asyncio.run(main())
