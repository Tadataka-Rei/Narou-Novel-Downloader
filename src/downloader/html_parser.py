from __future__ import annotations

import re
from bs4 import BeautifulSoup

from src.config.settings import DownloaderSettings


class HtmlParser:
    def __init__(self, settings: DownloaderSettings):
        self.settings = settings

    def extract_title_and_content(self, html: str) -> tuple[str, str]:
        soup = BeautifulSoup(html, "html.parser")

        title_tag = soup.find("h1", class_="p-novel__title")
        title = title_tag.get_text(strip=True) if title_tag else "Untitled"

        paragraphs: list[str] = []

        for body_div in soup.select("div.js-novel-text"):
            if self.settings.enable_ruby_replacement:
                self._replace_ruby_elements(body_div)

            for p in body_div.find_all("p"):
                text = p.get_text("", strip=False).rstrip()
                if text.strip():
                    paragraphs.append(text)

        return title, "\n".join(paragraphs)

    def _replace_ruby_elements(self, body_div):
        # Convert ruby elements to {base}[{furigana]}
        for ruby in body_div.find_all("ruby"):
            base = ""
            for child in ruby.contents:
                if getattr(child, "name", None) not in ("rt", "rp"):
                    if hasattr(child, "get_text"):
                        base += child.get_text()
                    else:
                        base += str(child)

            rt = ruby.find("rt")
            furigana = rt.get_text(strip=True) if rt else ""

            try:
                replacement = self.settings.replacement_format.format(base=base, furigana=furigana)
            except Exception:
                # Fail safe to old behavior format
                replacement = f"{base}[{furigana}]"

            ruby.replace_with(replacement)

    def extract_total_chapters_from_novel_index_html(self, html: str) -> int:
        soup = BeautifulSoup(html, "html.parser")
        number_div = soup.find("div", class_="p-novel__number")
        if not number_div:
            raise Exception("Could not find chapter count.")

        text = number_div.get_text(strip=True)
        m = re.search(r"(\d+)\s*/\s*(\d+)", text)
        if not m:
            raise Exception("Could not parse chapter count.")
        return int(m.group(2))

