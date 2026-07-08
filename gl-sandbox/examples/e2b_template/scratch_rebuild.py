import os
from dotenv import load_dotenv
load_dotenv()
from gllm_tools.code_interpreter.code_template import TemplateBuildStatus, TemplateSpec
from gllm_tools.code_interpreter.code_template.e2b_template_builder import E2BTemplateBuilder
b=E2BTemplateBuilder(api_key=os.environ["E2B_API_KEY"])
spec=TemplateSpec(template_id="gllm-tools-pandas", image="e2bdev/code-interpreter:latest", packages=["pandas"], force_rebuild=True)
r=b.ensure(spec)
print("STATUS", r.status, "REF", r.template_ref.value if r.template_ref else None, "DETAIL", r.detail)
