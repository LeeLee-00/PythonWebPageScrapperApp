# PythonWebPageScraperApp

This Python-based web scraping application uses Selenium with Microsoft Edge WebDriver to scrape content from the official Python website. It runs in headless mode for efficiency and ease of use in various environments, including cloud platforms.

## Description

The app navigates to the "About" and main page of [`python.org`](https://www.python.org/) and extracts all headings and paragraphs, saving them to text files. This can be useful for a variety of purposes, such as content aggregation, analysis, or offline reading.

## Setup

To run the scraper, ensure Python is installed on your system along with the required packages. The application uses the Edge WebDriver, managed automatically through `webdriver-manager`, simplifying the setup process.

### Prerequisites

- Python 3
- Selenium
- Microsoft Edge browser
- [`webdriver-manager`](https://pypi.org/project/webdriver-manager/) for handling the Edge WebDriver

### Installation

1.Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

## Usage
To run the scraper:

```bash
python main.py
```
this will execute the script and create 3 text files: scraped_about_page.txt and scraped_home_page.txt, and scraped_conduct_page.txt, containing the scraped content from the respective pages.

Please ignore error:
```
[24364:16552:1218/192301.989:ERROR:policy_logger.cc(156)] :components\enterprise\browser\controller\chrome_browser_cloud_management_controller.cc(161) Cloud management controller initialization aborted as CBCM is not enabled. Please use the --enable-chrome-browser-cloud-management` command line flag to enable it if you are not using the official Google Chrome build.

DevTools listening on ws://127.0.0.1:3768/devtools/browser/3cbbd6b3-b6d1-4ca3-889d-1d60c70e1b28
```

as they are more warnings than critical errors and are related to enterprise policy management features which are likely not relevant to the use case of this project sample.
