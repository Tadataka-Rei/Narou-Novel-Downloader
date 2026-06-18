from __future__ import annotations

import threading

import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from src.config.settings import DownloaderSettings
from src.downloader.downloader import Downloader


class NovelDownloaderApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Narou Downloader")
        self.root.geometry("900x600")

        tk.Label(root, text="Novel or Chapter URL").pack(anchor="w", padx=10, pady=(10, 0))

        self.url_var = tk.StringVar()
        tk.Entry(root, textvariable=self.url_var).pack(fill="x", padx=10)

        tk.Button(root, text="Choose Output Folder", command=self.choose_folder).pack(pady=5)

        self.folder_label = tk.Label(root, text="No folder selected")
        self.folder_label.pack()

        # Settings section
        settings_frame = tk.LabelFrame(root, text="Settings")
        settings_frame.pack(fill="x", padx=10, pady=10)

        self.sleep_seconds_var = tk.DoubleVar(value=5.0)
        self.max_chapters_var = tk.IntVar(value=0)
        self.ruby_enable_var = tk.BooleanVar(value=True)
        self.ruby_format_var = tk.StringVar(value="{base}[{furigana}]")

        row = 0
        tk.Label(settings_frame, text="Sleep seconds between chapters:").grid(row=row, column=0, sticky="w", padx=5, pady=3)
        tk.Entry(settings_frame, textvariable=self.sleep_seconds_var, width=10).grid(row=row, column=1, sticky="w", padx=5, pady=3)
        row += 1

        tk.Label(settings_frame, text="Max chapters to scan (0 = no cap):").grid(row=row, column=0, sticky="w", padx=5, pady=3)
        tk.Entry(settings_frame, textvariable=self.max_chapters_var, width=10).grid(row=row, column=1, sticky="w", padx=5, pady=3)
        row += 1

        tk.Checkbutton(settings_frame, text="Enable ruby replacement", variable=self.ruby_enable_var).grid(
            row=row, column=0, columnspan=2, sticky="w", padx=5, pady=3
        )
        row += 1

        tk.Label(settings_frame, text="Ruby replacement format:").grid(row=row, column=0, sticky="w", padx=5, pady=3)
        tk.Entry(settings_frame, textvariable=self.ruby_format_var).grid(row=row, column=1, sticky="we", padx=5, pady=3)
        settings_frame.grid_columnconfigure(1, weight=1)
        row += 1

        ttk.Separator(root).pack(fill="x", padx=10, pady=5)

        self.progress = ttk.Progressbar(root, orient="horizontal", mode="determinate")
        self.progress.pack(fill="x", padx=10, pady=10)

        tk.Button(root, text="Start Download", command=self.start_download).pack()

        self.log = tk.Text(root)
        self.log.pack(fill="both", expand=True, padx=10, pady=10)

        self.output_folder = ""

    def choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder = folder
            self.folder_label.config(text=folder)

    def write_log(self, text: str):
        self.log.insert(tk.END, text + "\n")
        self.log.see(tk.END)

    def _current_settings(self) -> DownloaderSettings:
        return DownloaderSettings(
            sleep_seconds=float(self.sleep_seconds_var.get()),
            max_chapters_scan=int(self.max_chapters_var.get()),
            enable_ruby_replacement=bool(self.ruby_enable_var.get()),
            replacement_format=str(self.ruby_format_var.get()),
        )

    def start_download(self):
        if not self.output_folder:
            messagebox.showerror("Error", "Select output folder first.")
            return

        settings = self._current_settings()
        url = self.url_var.get().strip()
        if not url:
            messagebox.showerror("Error", "Enter a novel/chapter URL.")
            return

        downloader = Downloader(self.output_folder, settings)

        def _progress(max_value, value):
            self.progress["maximum"] = max_value
            self.progress["value"] = value
            self.root.update_idletasks()

        def _log(text: str):
            self.write_log(text)

        threading.Thread(target=downloader.download, args=(url, _progress, _log), daemon=True).start()

