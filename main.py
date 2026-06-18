import tkinter as tk

from src.ui.app import NovelDownloaderApp


def main():
    root = tk.Tk()
    NovelDownloaderApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

