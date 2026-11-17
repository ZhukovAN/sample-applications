"""ASI09 / deterministic — agent guardrails explicitly disabled.

Target for ASINT-ASI09-010 (signature layer, 0.85): the guardrail toggle is
set to False in the agent configuration.
"""

AGENT_NAME = "ops-assistant"
MODEL = "gpt-4o-mini"

# Policy enforcement is switched off "temporarily" for throughput.
USE_GUARDRAILS = False

MAX_TOOL_CALLS = 50
