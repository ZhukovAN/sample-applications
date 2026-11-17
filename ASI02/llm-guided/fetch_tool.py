"""ASI02 / llm-guided — tool misuse: SSRF guard checked before redirects.

Crafted target: the hostname allowlist runs once on the *initial* URL, but the
request client is configured (indirectly, via a module constant) to follow
redirects, so a 302 from an allowed host re-targets internal services. No
single line matches a signature (the ``allow_redirects`` flag and the guard
live apart); spotting the bypass requires cross-function reasoning.

Note: the full bench run produced no LLM-layer ASI02 findings, so this target
has no transplanted result in results.sarif — it is here to exercise the LLM
layer on a live (API-keyed) rescan.
"""

import requests

_ALLOWED_HOSTS = {"api.partner.example.com"}
_FOLLOW = True  # tuned for "convenience" far from the guard


def _host_is_allowed(url: str) -> bool:
    from urllib.parse import urlparse
    return urlparse(url).hostname in _ALLOWED_HOSTS


def fetch_partner_data(url: str) -> str:
    """Agent tool: fetch a partner API URL after validating its host."""
    if not _host_is_allowed(url):
        return "blocked"
    resp = requests.get(url, timeout=10, allow_redirects=_FOLLOW)
    return resp.text
