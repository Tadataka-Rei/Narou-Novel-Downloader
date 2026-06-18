from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DownloaderSettings:
    # Sleep between chapter downloads when doing a full novel scan
    sleep_seconds: float = 5.0

    # Maximum chapters to scan/download when using a novel URL.
    # 0 means "no cap".
    max_chapters_scan: int = 0

    # Ruby/tag replacement behavior for furigana.
    # When enabled, ruby elements will be converted as:
    #   replacement_format.format(base=..., furigana=...)
    enable_ruby_replacement: bool = True
    replacement_format: str = "{base}[{furigana}]"

