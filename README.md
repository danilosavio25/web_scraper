# Python Web Scraper

A robust and user-friendly Python web scraper with a visual progress bar and subpage discovery capabilities.

## Features

- Scrapes HTML content from a given URL and converts it to Markdown.
- Optional recursive scraping of subpages within the same domain.
- Command-line interface with clear arguments.
- Visual status and progress tracking using `rich`.
- Saves scraped pages as `.md` files in the `scraped_data/` directory.

## Installation

1.  **Clone the repository** (if applicable) or navigate to the project directory.
2.  **Create a virtual environment:**
    ```bash
    python3 -m venv .venv
    ```
3.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the scraper using the following command format:

```bash
python3 scraper.py <URL> [FLAGS]
```

### Examples

- **Scrape a single page:**
  ```bash
  python3 scraper.py https://example.com
  ```
  - Output: `scraped_data/example.com/index.md`

- **Scrape a page and its subpages:**
  ```bash
  python3 scraper.py https://example.com --subpages
  ```

- **Specify a custom output directory:**
  ```bash
  python3 scraper.py https://example.com --output my_data
  ```

### Arguments

- `url`: The base URL to start scraping from.
- `--subpages`: (Optional) Flag to enable recursive scraping of subpages within the same domain.
- `--output`: (Optional) The directory where scraped Markdown files will be saved (default: `scraped_data`).

## Project Structure

- `scraper.py`: Main logic for fetching, parsing, converting to Markdown, and saving pages into site-specific folders.
- `requirements.txt`: List of Python dependencies.
- `.gitignore`: Files and directories to be ignored by Git.
- `.venv/`: Virtual environment directory.
- `scraped_data/`: Default directory for scraped Markdown content, organized by site name.
