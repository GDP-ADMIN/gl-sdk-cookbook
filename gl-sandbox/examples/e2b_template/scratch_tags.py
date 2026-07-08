import os
from dotenv import load_dotenv
load_dotenv()
from e2b import Template
opts=dict(api_key=os.environ["E2B_API_KEY"])
print("exists:", Template.exists("gllm-tools-pandas", **opts))
try:
    print("tags:", Template.get_tags("gllm-tools-pandas", **opts))
except Exception as e:
    print("tags err:", repr(e))
