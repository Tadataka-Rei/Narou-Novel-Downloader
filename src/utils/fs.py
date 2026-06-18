from __future__ import annotations

import os


def sanitize_filename(name: str) -> str:
    # remove invalid filename characters on Windows
    return "".join(c for c in name if c not in r'<>:"/\\|?*')


def save_chapter_txt(
    output_folder: str,
    chapter_num: int,
    title: str,
    content: str,
) -> str:
    filename = f"{chapter_num:04d}_{sanitize_filename(title)}.txt"
    path = os.path.join(output_folder, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(title + "\n\n")
        f.write(content)

    return path

