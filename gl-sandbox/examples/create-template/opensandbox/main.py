"""Build an OpenSandbox snapshot template, then create a sandbox from it.

OpenSandbox has no Dockerfile build; its "template" is a persistent snapshot
captured from a running sandbox with packages installed. The builder returns the
snapshot *name*, which the create side resolves to the newest Ready snapshot id.
"""

import asyncio
import os

from dotenv import load_dotenv
from gllm_tools.code_interpreter.code_sandbox.opensandbox_sandbox import OpenSandbox
from gllm_tools.code_interpreter.code_template import TemplateBuildStatus, TemplateSpec
from gllm_tools.code_interpreter.code_template.opensandbox_template_builder import OpenSandboxTemplateBuilder

load_dotenv()

CODE = """
import requests
print("requests:", requests.__version__)
"""


async def build_template() -> str:
    """Ensure the snapshot exists and return its name (the template reference)."""
    builder = OpenSandboxTemplateBuilder(domain=DOMAIN, api_key=os.getenv("OPENSANDBOX_API_KEY"))
    spec = TemplateSpec(
        template_id="gllm-tools-requests",
        image="opensandbox/code-interpreter:v1.0.2",
        packages=["requests"],
    )
    # Builder calls are blocking, so offload them off the event loop.
    result = await asyncio.get_running_loop().run_in_executor(None, builder.ensure, spec)
    if result.status is TemplateBuildStatus.FAILED:
        raise RuntimeError(f"snapshot build failed: {result.detail}")
    print(f"[template] status={result.status.value} ref={result.template_ref.value}")
    return result.template_ref.value


async def run_on_template(snapshot_name: str) -> None:
    """Create a sandbox from the predefined snapshot and run code in it."""
    sandbox = await OpenSandbox.create(
        domain=os.getenv("OPENSANDBOX_DOMAIN", "localhost:8080"),
        api_key=os.getenv("OPENSANDBOX_API_KEY"),
        protocol=os.getenv("OPENSANDBOX_PROTOCOL", "http"),
        use_server_proxy=os.getenv("OPENSANDBOX_SERVER_PROXY", "true").lower() == "true",
        snapshot_name=snapshot_name,
    )
    try:
        result = await sandbox.execute_code(CODE)
        print(f"[code] status={result.status.value}")
        print(result.text)
    finally:
        await sandbox.terminate()


async def main() -> None:
    """Build the snapshot template, then create a sandbox from it."""
    snapshot_name = await build_template()
    await run_on_template(snapshot_name)


if __name__ == "__main__":
    asyncio.run(main())
