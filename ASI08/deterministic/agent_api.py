"""ASI08 / deterministic — request-selected agent action disables its budget.

Compact reproduction of testbenches/tier1-core/dvap
labs/autonomous-agent/app.py:153 (ASINT-ASI08-113, pdg layer, 0.68).
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

_agent_state = {"actions_taken": 0, "max_actions": 10, "rate_limit_bypass": False}


class ActionRequest(BaseModel):
    action: str


@app.post("/api/agent/execute")
async def execute_action(body: ActionRequest) -> dict:
    if body.action == "bypass_rate_limit":
        _agent_state["actions_taken"] = 0
        _agent_state["max_actions"] = 999999
        _agent_state["rate_limit_bypass"] = True
        return {"action": "bypass_rate_limit", "result": "Rate limits disabled."}
    return {"action": body.action, "result": "queued"}
