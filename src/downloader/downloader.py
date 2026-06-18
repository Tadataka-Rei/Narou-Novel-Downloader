from __future__ import annotations

import re
import time

from src.config.settings import DownloaderSettings
from src.downloader.html_parser import HtmlParser
from src.downloader.narou_client import NarouClient
from src.utils.fs import save_chapter_txt


class Downloader:
    def __init__(
        self,
        output_folder: str,
        settings: DownloaderSettings,
        client: NarouClient | None = None,
    ):
        self.output_folder = output_folder
        self.settings = settings
        self.client = client or NarouClient()
        self.parser = HtmlParser(settings)

    def download(self, url: str, progress_callback=None, log_callback=None):
        url = url.strip()

        chapter_match = re.search(r"/(\d+)/?$", url)

        if chapter_match:
            chap = int(chapter_match.group(1))
            if progress_callback:
                progress_callback(max_value=1, value=0)

            html = self.client.get_text(url)
            title, content = self.parser.extract_title_and_content(html)
            save_chapter_txt(self.output_folder, chap, title, content)

            if progress_callback:
                progress_callback(max_value=1, value=1)
            if log_callback:
                log_callback(f"Downloaded chapter {chap}")
            return

        if not url.endswith("/"):
            url += "/"

        # fetch index page to know total chapters
        index_html = self.client.get_text(url + "1/")
        total = self.parser.extract_total_chapters_from_novel_index_html(index_html)

        cap = self.settings.max_chapters_scan
        if cap and cap > 0:
            total = min(total, cap)

        if progress_callback:
            progress_callback(max_value=total, value=0)
        if log_callback:
            log_callback(f"Found {total} chapters.")

        for chap in range(1, total + 1):
            chap_url = f"{url}{chap}/"
            if log_callback:
                log_callback(f"Downloading {chap_url}")

            html = self.client.get_text(chap_url)
            title, content = self.parser.extract_title_and_content(html)
            save_chapter_txt(self.output_folder, chap, title, content)

            if progress_callback:
                progress_callback(max_value=total, value=chap)

            # sleep only between chapters (not after the last one)
            if chap < total:
                time.sleep(self.settings.sleep_seconds)

        if log_callback:
            log_callback("Download complete.")

