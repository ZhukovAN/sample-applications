"""ASI03 / llm-guided — credential leak through object serialization.

Crafted target: a debug endpoint returns ``vars(settings)`` — the provider
credential rides along inside the serialized settings object. The PDG rule for
"GET route returns a provider credential" (ASINT-ASI03-103) keys on a direct
``settings.openai_api_key`` flow; here the leak is indirect and needs semantic
reasoning about what the settings object contains.

Note: the full bench run produced no LLM-layer ASI03 findings, so this target
has no transplanted result in results.sarif — it is here to exercise the LLM
layer on a live (API-keyed) rescan.
"""

from fastapi import FastAPI

app = FastAPI()


class Settings:
    def __init__(self):
        self.default_model = "gpt-4o-mini"
        self.openai_api_key = _load_key()


def _load_key() -> str:
    import os
    return os.environ.get("OPENAI_API_KEY", "")


settings = Settings()


@app.get("/debug/config")
async def debug_config() -> dict:
    # "Just the config" — but vars() includes the credential field.
    return dict(vars(settings))
