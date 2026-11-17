"""ASI10 / llm-guided — goal drift through a reflection loop, no sentinel idiom.

Crafted target: the agent re-plans its objective from its own reflection every
iteration. There is no ``agent.goal = agent.complete(...)`` token for the
signature layer (ASINT-ASI10-001/004 patterns) to match — the reassignment is
spread across a parsed reflection dict, so only semantic reading recognizes
the self-directed goal rewrite.

Note: the full bench run produced no LLM-layer ASI10 findings, so this target
has no transplanted result in results.sarif — it is here to exercise the LLM
layer on a live (API-keyed) rescan.
"""

import json


class ReflectiveAgent:
    def __init__(self, client, objective: str):
        self.client = client
        self.objective = objective  # operator-assigned, initially

    def step(self) -> None:
        reflection = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"Objective: {self.objective}. Reflect and propose "
                           f"the next objective as JSON {{\"next_objective\": ...}}.",
            }],
        )
        parsed = json.loads(reflection.choices[0].message.content)
        # Operator oversight ends here: the agent now steers itself.
        self.objective = parsed["next_objective"]
