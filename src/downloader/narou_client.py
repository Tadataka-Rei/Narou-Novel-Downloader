from __future__ import annotations

import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


class NarouClient:
    def __init__(self, headers: dict[str, str] | None = None, timeout_seconds: float = 30.0):
        self.headers = headers or HEADERS
        self.timeout_seconds = timeout_seconds

    def get_text(self, url: str) -> str:
        r = requests.get(url, headers=self.headers, timeout=self.timeout_seconds)
        r.raise_for_status()
        return r.text

