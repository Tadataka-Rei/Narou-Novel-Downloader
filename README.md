# Narou Novel Downloader

A Python desktop application for downloading novels from Syosetu (Narou) with customizable settings and chapter management.

**Table of Contents**
- [Features](#features)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
  - [Getting Started](#getting-started)
  - [Field Descriptions](#field-descriptions)
  - [Settings Explained](#settings-explained)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)

---

## Features

✨ **Core Features:**
- Download complete novels or individual chapters from Narou
- Batch download multiple chapters with customizable delays
- Configurable chapter range (start from, maximum count)
- Ruby/Furigana text replacement support
- Real-time download progress tracking
- Detailed logging interface

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Internet connection

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Narou-Novel-Downloader
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

---

## Usage Guide

### Getting Started

Launch the application by running:
```bash
python main.py
```

The Narou Downloader window will open with the following interface:

![Application Interface](docs/images/app-interface-placeholder.png)
*Application main window with all input fields and controls*

### Field Descriptions

#### 1. **Novel or Chapter URL** (Required)
   - **What to enter:** The direct URL to a novel or chapter from Narou
   - **Format:** `https://ncode.syosetu.com/n12345/` (novel) or chapter URL
   - **Examples:**
     - Novel: `https://ncode.syosetu.com/n12345/`
     - Chapter: `https://ncode.syosetu.com/n12345/1/`
   - **Note:** You must provide a valid Narou URL to proceed

![URL Input Field](docs/images/url-field-placeholder.png)
*Enter the novel or chapter URL here*

---

#### 2. **Output Folder** (Required)
   - **What to enter:** The directory where downloaded files will be saved
   - **How to select:** Click the "Choose Output Folder" button to open a folder browser
   - **Default:** No folder selected until you choose one
   - **Note:** Downloaded chapters will be saved as individual files in this folder

![Folder Selection](docs/images/folder-selection-placeholder.png)
*Click "Choose Output Folder" to select your download destination*

---

### Settings Explained

All settings are optional and have sensible defaults.

#### **Sleep seconds between chapters** (Default: 5.0)
   - **What it does:** Adds a delay between downloading each chapter
   - **Why use it:** Prevents overwhelming the server with rapid requests
   - **Valid range:** Any positive number (decimal values allowed, e.g., 1.5)
   - **Recommendation:** 
     - `2-5 seconds` for normal downloading
     - `0.5-1 second` if you have a stable connection
     - `10+ seconds` to be extra respectful to the server
   - **Example:** Enter `3.0` to wait 3 seconds between chapters

![Sleep Seconds Setting](docs/images/sleep-seconds-placeholder.png)
*Configure delay between chapter downloads*

---

#### **Max chapters to scan** (Default: 0)
   - **What it does:** Limits the number of chapters to download when using a novel URL
   - **0 = Download all available chapters**
   - **Valid range:** 0 (unlimited) or any positive integer
   - **Examples:**
     - `0` → Download entire novel
     - `50` → Download first 50 chapters
     - `100` → Download first 100 chapters
   - **Use case:** Test a novel by downloading just the first few chapters

---

#### **Start from chapter** (Default: 1)
   - **What it does:** Specifies which chapter to begin downloading from
   - **Valid range:** Any positive integer ≥ 1
   - **Examples:**
     - `1` → Start from the first chapter
     - `50` → Start from chapter 50
     - `100` → Start from chapter 100
   - **Note:** This only applies when downloading a full novel. Single chapter downloads ignore this setting.
   - **Use case:** Resume downloads or skip already-downloaded chapters

![Chapter Range Settings](docs/images/chapter-range-placeholder.png)
*Set where to start and how many chapters to download*

---

#### **Enable ruby replacement** (Default: ✓ Enabled)
   - **What it does:** Enables or disables the conversion of ruby/furigana text
   - **Furigana:** Phonetic guides shown above or beside Japanese characters
   - **When to enable:** You want furigana included in the downloaded text
   - **When to disable:** You want the original HTML ruby tags preserved

---

#### **Ruby replacement format** (Default: `{base}[{furigana}]`)
   - **What it does:** Defines how furigana text will be formatted in the output
   - **Available variables:**
     - `{base}` → The main character(s)
     - `{furigana}` → The phonetic reading
   - **Examples:**
     - `{base}[{furigana}]` → Result: `漢字[かんじ]`
     - `{base}({furigana})` → Result: `漢字(かんじ)`
     - `{furigana}` → Result: `かんじ` (furigana only)
     - `{base}/{furigana}` → Result: `漢字/かんじ`
   - **Note:** Only applies if "Enable ruby replacement" is checked

![Ruby Settings](docs/images/ruby-settings-placeholder.png)
*Configure how furigana will appear in downloaded text*

---

### Download Controls

![Download Button](docs/images/download-button-placeholder.png)

- **Start Download Button:** Begins the download process with your current settings
- **Progress Bar:** Shows download progress (0-100%)
- **Log Output:** Displays real-time download activity and any messages/errors

![Progress and Logs](docs/images/progress-logs-placeholder.png)
*Monitor download progress and view activity logs*

---

## Examples

### Example 1: Download an entire novel

1. Find a novel on Narou, e.g., `https://ncode.syosetu.com/n12345/`
2. Paste the URL in the **Novel or Chapter URL** field
3. Click **Choose Output Folder** and select where to save
4. Leave all settings at defaults (or adjust as needed)
5. Click **Start Download**

**Result:** All chapters will download with 5-second delays between each

---

### Example 2: Download first 30 chapters only

1. Enter the novel URL
2. Select output folder
3. Set **Max chapters to scan** to `30`
4. Click **Start Download**

**Result:** Only the first 30 chapters will download

---

### Example 3: Resume downloading from chapter 50

1. Enter the novel URL
2. Select the same output folder (or different one)
3. Set **Start from chapter** to `50`
4. Set **Max chapters to scan** to `0` (or desired number)
5. Click **Start Download**

**Result:** Download will begin from chapter 50

---

### Example 4: Custom furigana format

1. Configure URL and folder as normal
2. Set **Enable ruby replacement** to ✓ (checked)
3. Change **Ruby replacement format** to `{base}({furigana})`
4. Click **Start Download**

**Result:** Furigana will appear as: `漢字(かんじ)` instead of `漢字[かんじ]`

---

## Troubleshooting

### "Invalid URL" error
- ✓ Ensure the URL is a valid Narou/Syosetu link
- ✓ Check that the URL is not behind a paywall or restricted
- ✓ Verify your internet connection

### No folder selected
- ✓ You must click "Choose Output Folder" to select a destination
- ✓ Ensure you have write permissions to the selected folder

### Download is slow
- ✓ The sleep delay between chapters is working as intended
- ✓ Try reducing **Sleep seconds between chapters** if you want faster downloads
- ✓ Check your internet speed

### Some chapters fail to download
- ✓ Some chapters may have access restrictions
- ✓ Check the log output for specific error messages
- ✓ Try downloading individual chapters first to test

---

## Configuration Files

The application uses the following files:
- `src/config/settings.py` - Default download settings
- `src/downloader/downloader.py` - Core download logic
- `src/downloader/narou_client.py` - Narou API client
- `src/downloader/html_parser.py` - HTML parsing utilities
- `src/ui/app.py` - GUI application
- `src/utils/fs.py` - File system utilities

---

## Support

For issues or questions:
1. Check the log output for error messages
2. Verify your URL is correct
3. Ensure you have internet connectivity
4. Check that you have write permissions to the output folder

---

## License

See [LICENSE](LICENSE) file for details.

---

## Disclaimer

This tool is for personal use only. Please respect copyright laws and the Narou terms of service when downloading content. 
