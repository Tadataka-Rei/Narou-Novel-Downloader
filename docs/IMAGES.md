# Image Placeholders Guide

This document describes the image placeholders used in the README. Replace these placeholder paths with actual screenshots.

## Image List

### 1. **app-interface-placeholder.png**
- **Location:** `docs/images/app-interface-placeholder.png`
- **Description:** Full screenshot of the application window showing:
  - URL input field
  - "Choose Output Folder" button
  - Settings frame with all options visible
  - Progress bar
  - Log output area
  - "Start Download" button
- **Size:** ~900x600px (matches application window)
- **Purpose:** Show users the complete interface on startup

### 2. **url-field-placeholder.png**
- **Location:** `docs/images/url-field-placeholder.png`
- **Description:** Close-up screenshot of the URL input field with:
  - "Novel or Chapter URL" label
  - Example URL in the text field (e.g., `https://ncode.syosetu.com/n12345/`)
- **Purpose:** Help users understand where to paste the Narou novel URL

### 3. **folder-selection-placeholder.png**
- **Location:** `docs/images/folder-selection-placeholder.png`
- **Description:** Screenshot showing:
  - "Choose Output Folder" button
  - The folder path display label (showing selected folder or "No folder selected")
- **Purpose:** Show how to select the output directory

### 4. **sleep-seconds-placeholder.png**
- **Location:** `docs/images/sleep-seconds-placeholder.png`
- **Description:** Settings frame focus showing:
  - "Sleep seconds between chapters:" label
  - Input field with a value (e.g., `5.0`)
  - Example values highlighted
- **Purpose:** Explain the sleep delay setting

### 5. **chapter-range-placeholder.png**
- **Location:** `docs/images/chapter-range-placeholder.png`
- **Description:** Settings frame showing:
  - "Max chapters to scan (0 = no cap):" field with value
  - "Start from chapter:" field with value
- **Purpose:** Demonstrate chapter range configuration

### 6. **ruby-settings-placeholder.png**
- **Location:** `docs/images/ruby-settings-placeholder.png`
- **Description:** Settings frame showing:
  - "Enable ruby replacement" checkbox (checked/unchecked state)
  - "Ruby replacement format:" field with example format
- **Purpose:** Show furigana replacement options

### 7. **download-button-placeholder.png**
- **Location:** `docs/images/download-button-placeholder.png`
- **Description:** Close-up of the "Start Download" button
- **Purpose:** Clearly identify the button to start the download

### 8. **progress-logs-placeholder.png**
- **Location:** `docs/images/progress-logs-placeholder.png`
- **Description:** Screenshot showing:
  - Progress bar (partially or fully filled)
  - Log output area with sample messages/activity
- **Purpose:** Show real-time download feedback

## How to Add Screenshots

1. Run the application: `python main.py`
2. Use a screenshot tool (e.g., Snipping Tool, ShareX, or Python PIL)
3. Capture each area mentioned above
4. Save as PNG files in the `docs/images/` folder
5. Use the filenames specified above

## Tools for Screenshots

- **Windows Snipping Tool:** Built-in tool for quick screenshots
- **ShareX:** Advanced screenshot/screen recording tool
- **Python PIL:** Programmatic screenshot capture
- **VSCode Screenshot Extension:** One-click screenshot integration

## Example Screenshot Command (Python)

```python
from PIL import ImageGrab

# Capture full screen
screenshot = ImageGrab.grab()
screenshot.save('docs/images/app-interface-placeholder.png')

# Capture specific region (x, y, x+width, y+height)
screenshot = ImageGrab.grab(bbox=(100, 100, 1000, 700))
screenshot.save('docs/images/url-field-placeholder.png')
```

---

**Note:** The README will display properly even without these images. However, adding actual screenshots will greatly improve the documentation and user experience.
