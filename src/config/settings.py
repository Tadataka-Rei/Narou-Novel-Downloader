from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DownloaderSettings:
    sleep_seconds: float = 5.0


    max_chapters_scan: int = 0

    enable_ruby_replacement: bool = True
    replacement_format: str = "{base}[{furigana}]"

    start_from_chapter: int = 1


