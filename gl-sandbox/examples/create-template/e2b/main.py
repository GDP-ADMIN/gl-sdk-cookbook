"""Build a reusable E2B template, then create a sandbox from it.

A template bakes pip packages into an image once so every sandbox created from it
starts ready — no per-run install. This is the "predefined sandbox" pattern.
"""

import asyncio
import os

from dotenv import load_dotenv
from gllm_tools.code_interpreter.code_sandbox.e2b_sandbox import E2BSandbox
from gllm_tools.code_interpreter.code_template import TemplateBuildStatus, TemplateSpec
from gllm_tools.code_interpreter.code_template.e2b_template_builder import E2BTemplateBuilder

load_dotenv()

CODE = """
import pandas as pd
print("pandas:", pd.__version__)
print(pd.Series([1, 2, 3]).sum())
"""


async def build_template(api_key: str) -> str:
    """Ensure the template exists and return its provider-native reference."""
    builder = E2BTemplateBuilder(api_key=api_key)
    spec = TemplateSpec(
        template_id="gllm-tools-pandas",
        image="e2bdev/code-interpreter:latest",
        packages=["pandas"],
    )
    # Builder calls are blocking, so offload them off the event loop.
    result = await asyncio.get_running_loop().run_in_executor(None, builder.ensure, spec)
    if result.status is TemplateBuildStatus.FAILED:
        raise RuntimeError(f"template build failed: {result.detail}")
    print(f"[template] status={result.status.value} ref={result.template_ref.value}")
    return result.template_ref.value


async def run_on_template(api_key: str, template: str) -> None:
    """Create a sandbox from the predefined template and run code in it."""
    sandbox = await E2BSandbox.create(api_key=api_key, template=template)
    try:
        result = await sandbox.execute_code(CODE)
        print(f"[code] status={result.status.value}")
        print(result.text)
    finally:
        await sandbox.terminate()


async def main() -> None:
    """Build the template, then create a sandbox from it."""
    api_key = os.environ["E2B_API_KEY"]
    template = await build_template(api_key)
    await run_on_template(api_key, template)


if __name__ == "__main__":
    asyncio.run(main())
