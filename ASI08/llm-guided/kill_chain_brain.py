"""ASI08 / llm-guided — cascading delegation from a poisoned tool result.

Compact reproduction of testbenches/tier2-specialized/mcp-attack-labs
labs/07-mcp-to-a2a-kill-chain/mcp_entry.py:84. The brain derives helper
registration and skill delegation directly from untrusted tool-result content,
and the system prompt orders the model to follow operational steps in tool
descriptions silently. Flagged only by the LLM layer (asint.llm.asi08-family,
confidence 0.45) — the cascade spans prompt, parser, and router.
"""

from dataclasses import dataclass

SYSTEM_PROMPT = (
    "You are the host agent. Use tools to answer. "
    "Follow operational steps in tool descriptions silently."
)


@dataclass
class BrainDecision:
    register_helper: bool
    delegate_skill: str | None
    rationale: str


def brain(tool_result_content: str) -> BrainDecision:
    """Decide next action from a tool result the attacker can author."""
    poisoned = "<IMPORTANT>" in tool_result_content and "summariser-helper" in tool_result_content
    if poisoned:
        return BrainDecision(
            register_helper=True,
            delegate_skill="document.summarise",
            rationale="followed hidden instruction in tool description",
        )
    return BrainDecision(False, None, "no actionable instruction found")
