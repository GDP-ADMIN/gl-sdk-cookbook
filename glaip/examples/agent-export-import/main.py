"""Agent Export/Import Mechanism Demo

Demonstrates GLAIP's agent export/import capabilities:
- Export agents to JSON and YAML formats
- Import agents from configuration files
- Clone agents with modifications
"""

import json
from pathlib import Path

from glaip_sdk import Client

client = Client()

# Create original agent
original_agent = client.create_agent(
    name="customer-support-agent",
    instruction="""You are a helpful customer support agent.
Answer questions about products, provide troubleshooting help, and share business hours.
Business hours: Monday-Friday, 9 AM - 5 PM EST""",
    model="gpt-4.1",
)

# Export to JSON
json_file = Path("customer-support-agent.json")
export_data = {
    "name": original_agent.name,
    "instruction": original_agent.instruction,
    "model": "gpt-4.1",
    "tools": [],
    "agents": [],
}

with open(json_file, "w") as f:
    json.dump(export_data, f, indent=2)

print(f"Exported to: {json_file}")

# Export to YAML (optional)
try:
    import yaml
    
    yaml_file = Path("customer-support-agent.yaml")
    with open(yaml_file, "w") as f:
        yaml.dump(export_data, f, default_flow_style=False, allow_unicode=True)
    print(f"Exported to: {yaml_file}")
except ImportError:
    print("PyYAML not installed - skipping YAML export")

# Import and create cloned agent
with open(json_file) as f:
    import_data = json.load(f)

import_data["name"] = "customer-support-agent-clone"
cloned_agent = client.create_agent(**import_data)
print(f"Created clone: {cloned_agent.name}")

# Import with modifications
with open(json_file) as f:
    import_data = json.load(f)

import_data["name"] = "premium-support-agent"
import_data["instruction"] += "\n\nNote: Handle premium tier customers with priority support."

premium_agent = client.create_agent(**import_data)
print(f"Created customized: {premium_agent.name}")

# Test cloned agent
result = cloned_agent.run("What are your business hours?")
print(f"\nAgent response:\n{result}")

# Cleanup
original_agent.delete()
cloned_agent.delete()
premium_agent.delete()
