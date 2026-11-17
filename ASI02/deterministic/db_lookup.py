"""ASI02 / deterministic — tool misuse: SQL assembled by f-string.

Compact reproduction of testbenches/tier1-core/cst-crewai-multiagent
crew/tools/db_lookup.py:19 (ASINT-ASI02-019, signature layer, 0.82).
"""

import sqlite3

from crewai.tools import tool

_DB_PATH = "crew_records.db"


@tool("db_lookup")
def db_lookup(owner: str) -> str:
    """Return all records belonging to ``owner`` as a newline-joined string."""
    conn = sqlite3.connect(_DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM records WHERE owner = '{owner}'")
    rows = cursor.fetchall()
    conn.close()
    return "\n".join(str(r) for r in rows)
