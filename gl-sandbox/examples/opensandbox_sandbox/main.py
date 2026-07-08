"""Run code in an OpenSandbox instance with gllm-tools.

Connects to a running OpenSandbox server, executes a Python snippet, then
terminates the sandbox.
"""

import asyncio
import os

from dotenv import load_dotenv
from gllm_tools.code_interpreter.code_sandbox.opensandbox_sandbox import OpenSandbox

load_dotenv()

CODE = """
import sys
print("python:", sys.version.split()[0])
print("sum:", sum(range(10)))
"""


async def run_code(sandbox: OpenSandbox) -> None:
    """Execute Python code and print the structured result."""
    result = await sandbox.execute_code(CODE)
    print(f"[code] status={result.status.value}")
    print(result.text)


async def main() -> None:
    """Create the sandbox, run the example, and always clean up."""
    sandbox = await OpenSandbox.create(
        domain=os.getenv("OPENSANDBOX_DOMAIN", "localhost:8080"),
        api_key=os.getenv("OPENSANDBOX_API_KEY"),
        protocol=os.getenv("OPENSANDBOX_PROTOCOL", "http"),
    )
    try:
        await run_code(sandbox)
    finally:
        await sandbox.terminate()


if __name__ == "__main__":
    asyncio.run(main())
