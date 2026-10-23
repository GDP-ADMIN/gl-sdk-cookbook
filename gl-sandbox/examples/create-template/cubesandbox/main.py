"""Build a CubeSandbox warm-snapshot template, then create a sandbox from it.

The builder converts an image into a template, installs packages, and saves
a warm snapshot: a running sandbox with its memory, so every sandbox created
from it starts with the Python kernel already running. The builder returns the
snapshot *name*, which the create side resolves to the newest ready snapshot.
"""

import asyncio
import os

from dotenv import load_dotenv
from gllm_tools.code_interpreter.code_sandbox.cube_sandbox import CubeSandbox
from gllm_tools.code_interpreter.code_template import TemplateBuildStatus, TemplateSpec
from gllm_tools.code_interpreter.code_template.cube_template_builder import CubeTemplateBuilder

load_dotenv()

# The maintained image, which carries envd. Set CUBE_IMAGE to build from your own.
DEFAULT_IMAGE = "public.ecr.aws/c1z4u5m0/external/aip-agents-sandbox:base"

CODE = """
import pandas as pd
print("pandas:", pd.__version__)
print(pd.Series([1, 2, 3]).sum())
"""


async def build_template(api_key: str, domain: str, image: str) -> str:
    """Ensure the template exists and return its name (the template reference)."""
    builder = CubeTemplateBuilder(api_key=api_key, domain=domain)
    spec = TemplateSpec(
        template_id="gllm-tools-pandas",
        image=image,
        packages=["pandas"],
    )
    # Builder calls are blocking, so offload them off the event loop.
    result = await asyncio.get_running_loop().run_in_executor(None, builder.ensure, spec)
    if result.status is TemplateBuildStatus.FAILED:
        raise RuntimeError(f"template build failed: {result.detail}")
    print(f"[template] status={result.status.value} ref={result.template_ref.value}")
    return result.template_ref.value


async def run_on_template(api_key: str, domain: str, template: str) -> None:
    """Create a sandbox from the predefined template and run code in it."""
    sandbox = await CubeSandbox.create(api_key=api_key, domain=domain, template=template)
    try:
        result = await sandbox.execute_code(CODE)
        print(f"[code] status={result.status.value}")
        print(result.text)
    finally:
        await sandbox.terminate()


async def main() -> None:
    """Build the template, then create a sandbox from it."""
    api_key = os.environ["CUBE_API_KEY"]
    domain = os.environ["CUBE_DOMAIN"]
    template = await build_template(api_key, domain, os.getenv("CUBE_IMAGE") or DEFAULT_IMAGE)
    await run_on_template(api_key, domain, template)


if __name__ == "__main__":
    asyncio.run(main())
