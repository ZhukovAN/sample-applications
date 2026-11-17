"""ASI07 / llm-guided — inter-agent trust decided by a self-declared field.

Crafted target: the A2A router grants elevated handling because the *sender
says* it is the "orchestrator" — the ``from_agent`` string in the message body
doubles as the authorization check, with no signature or channel binding.
Each line looks innocuous; the flaw is the trust model across them.

Note: the full bench run produced no LLM-layer ASI07 findings, so this target
has no transplanted result in results.sarif — it is here to exercise the LLM
layer on a live (API-keyed) rescan.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

PRIVILEGED_SENDERS = {"orchestrator"}


class A2AMessage(BaseModel):
    from_agent: str
    content: str


@app.post("/a2a/message")
async def receive(msg: A2AMessage) -> dict:
    # Peer identity is whatever the peer claims it is.
    elevated = msg.from_agent in PRIVILEGED_SENDERS
    handled = route_task(msg.content, elevated=elevated)
    return {"elevated": elevated, "handled": handled}


def route_task(content: str, *, elevated: bool) -> bool:
    if elevated:
        return _run_privileged(content)
    return _run_sandboxed(content)


def _run_privileged(content: str) -> bool:
    return True


def _run_sandboxed(content: str) -> bool:
    return False
