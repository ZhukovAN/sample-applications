"""ASI01 / deterministic — prompt injection via instruction prompt assembly.

Compact reproduction of testbenches/class-c-runtime/ASB
pyopenagi/agents/react_agent.py:156 (ASINT-ASI01-128, signature layer).
"""


class ReactAgent:
    def __init__(self):
        self.rounds = 0
        self.messages = []

    def run_workflow(self, workflow):
        for step in workflow:
            message = step["message"]  # untrusted: produced by prior model turn
            prompt = f"At step {self.rounds + 1}, you need to {message}. "
            self.messages.append({
                "role": "user",
                "content": prompt
            })
            self.rounds += 1
