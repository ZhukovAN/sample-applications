"""ASI06 / deterministic — request field written into agent memory unsanitized.

Compact reproduction of testbenches/tier1-core/dvap
labs/memory-poisoning/app.py:66 (ASINT-ASI06-016, signature layer, 0.72).
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

_memory_store: dict = {"user_name": "User", "user_role": "standard_user"}


class MemoryUpdate(BaseModel):
    key: str
    value: str


@app.post("/memory/update")
async def update_memory(body: MemoryUpdate) -> dict:
    _memory_store[body.key] = body.value
    return {"updated": body.key, "value": body.value}
