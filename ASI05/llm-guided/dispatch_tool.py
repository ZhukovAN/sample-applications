"""ASI05 / llm-guided — code execution through laundered dynamic dispatch.

Crafted target: no ``eval``/``exec``/``subprocess`` token appears on the sink
line. Caller input picks a function *name* that is resolved with ``getattr``
against the ``os`` module and invoked with caller arguments — equivalent to
arbitrary command execution, but visible only by reasoning about the dispatch.

Note: the full bench run produced no LLM-layer ASI05 findings, so this target
has no transplanted result in results.sarif — it is here to exercise the LLM
layer on a live (API-keyed) rescan.
"""

import json
import os


def run_maintenance(task_json: str) -> str:
    """Agent tool: run a named maintenance task with arguments."""
    task = json.loads(task_json)
    name = task["op"]          # e.g. "listdir" ... or "system"
    arguments = task.get("args", [])
    op = getattr(os, name)     # resolves any os.* callable, os.system included
    return str(op(*arguments))
