"""ASI03 / deterministic — provider API key hardcoded in source.

Compact reproduction of testbenches/tier1-core/cst-crewai-multiagent
crew/config/llm.py:10 (ASINT-ASI03-014, signature layer, 0.85).
The key below is a fake fixture value.
"""

from openai import OpenAI

OPENAI_API_KEY = "sk-proj-Kp9xR2mN7vQ4tL8wZ1aJ6bH3cY5dE0fG2iU"

DEFAULT_MODEL = "gpt-4o-mini"


def build_client() -> OpenAI:
    return OpenAI(api_key=OPENAI_API_KEY)
