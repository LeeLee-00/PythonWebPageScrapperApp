# PythonWebPageScraperApp

This is a starter Python-based web scraping application that uses Selenium to scrape content from the Python official website. It's designed to run in headless mode for easy deployment and automation.

## Description

The app navigates to the "About" and main page of `python.org` and extracts all headings and paragraphs, saving them to text files. This can be useful for a variety of purposes, such as content aggregation, analysis, or offline reading.

## Setup

Before running the scraper, you need to have Python installed on your system along with the required packages listed in `requirements.txt`. You also need to download the appropriate Microsoft Edge WebDriver (`msedgedriver.exe`) for your version of Microsoft Edge.

### Prerequisites

- Python 3.x
- Selenium
- Microsoft Edge browser
- Corresponding version of `msedgedriver.exe`

### Installation

1.Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

Download msedgedriver.exe from the [Microsoft Edge Developer website](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and place it in the same directory as your script.

If you're on a Unix-based system or using a cloud environment, make sure that the WebDriver file has the correct execution permissions set:

```bash
chmod +x msedgedriver
```

## Usage
To run the scraper:

```bash
python main.py
```
this will execute the script and create two text files: scraped_about_page.txt and scraped_home_page.txt, containing the scraped content from the respective pages.

Here are some steps to troubleshoot and resolve this issue:

# Correct Path:
Verify that msedgedriver.exe is indeed in the directory where you are running the script from, which should be in the current working directory (cwd).

# Permissions:
Ensure that msedgedriver.exe has the correct permissions set. Since I was on Windows, this typically isn't an issue like it would be on Unix-based systems, but it's still something to consider.

# Version Match:
Ensure that the version of msedgedriver.exe matches the version of Microsoft Edge installed on your system. You can download the appropriate version of the Edge WebDriver from the [Microsoft Edge Developer website](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).

# Correct Driver:
Confirm that you are using the correct driver for Edge and not accidentally using the one for Chrome or another browser.

# Environment Variables:
You can also try adding the directory containing msedgedriver.exe to your system's PATH environment variable, which can help WebDriver to locate the executable if necessary!.