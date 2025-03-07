import asyncio
import aiohttp
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import os
import pdb
from logger import logging

# Set up logging
log = logging.getLogger(__name__)

# Configure Selenium to run headless
options = Options()
options.headless = True
options.add_argument("--no-sandbox")  # This can be required in a cloud environment
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

log.info("Setting up WebDriver")
# pdb.set_trace()
# Get the current working directory
cwd = os.getcwd()

# Setup WebDriver
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

def scrape_page_selenium(driver, url, file_name):
    log.info(f"Scraping page: {url} - using Selenium")
    driver.get(url)
    # Wait until the document is fully loaded
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
    log.info(f"Page title: {driver.title}")
    # Get the complete HTML of the page
    html = driver.page_source
    with open(file_name, 'w') as file:
        file.write(html)

# scrape_page_selenium(driver,"https://www.python.org/psf/conduct/", "scraped_conduct_page.txt")

# add your timeout
# driver.quit()

async def fetch_page(session, url):
    try:
        log.info(f"Fetching page: {url}")
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
            response.raise_for_status()
            return await response.text()
    except Exception as e:
        log.error(f"Error fetching {url}: {e}")
        return None

async def scrape_page_async(session, url, file_name):
    html = await fetch_page(session, url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        containers = soup.find_all(class_='container')
        # If no container is found, you can fallback to saving full text
        text = '\n\n'.join(container.get_text(strip=True) for container in containers) or soup.get_text(strip=True)
        with open(file_name, 'w') as file:
            file.write(text)
    else:
        log.error(f"No content fetched from {url}")

async def run_async_scrapers(url_file_list):
    async with aiohttp.ClientSession() as session:
        tasks = [
            scrape_page_async(session, url, file_name)
            for url, file_name in url_file_list
        ]
        await asyncio.gather(*tasks)

# scraping multiple pages concurrently
if __name__ == "__main__":
    url_file_list = [
        ("https://www.python.org/", "scraped_home_page.txt"),
        ("https://www.python.org/about/", "scraped_about_page.txt"),
        ("https://www.python.org/psf/conduct/", "scraped_conduct_page.txt")
    ]
    asyncio.run(run_async_scrapers(url_file_list))