import asyncio
import aiohttp
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager as EdgeDriver
from selenium.webdriver.common.by import By
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


# Get the current working directory
cwd = os.getcwd()

# Setup WebDriver
driver = webdriver.Edge(service=EdgeService(EdgeDriver().install()))

def scrape_page_selenium(driver, url, file_name):
    """
    Navigates to a page using the provided WebDriver, scrapes headings and paragraphs, 
    and saves them to the specified file.
    
    :param driver: Selenium WebDriver instance
    :param url: URL of the page to scrape
    :param file_name: Name of the file to save the scraped content
    """
    # Navigate to the specified page
    driver.get(url)

    # Scrape heading and paragraph text and save to a file
    with open(file_name, 'w') as file:
        # Find all the elements in the container class in the python site.
        containers = driver.find_elements(By.CLASS_NAME, "container")
        # Write headings to file
        for container in containers:
            file.write(container.text + '\n\n')

async def fetch_page(session, url):
    """
    Fetches the page content using aiohttp and returns the response.
    
    :param session: aiohttp ClientSession instance
    :param url: URL of the page to fetch
    :return: Response from the page
    """
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

async def scrape_page_async(url, file_name):
    """
    Using aitohtp and beutfiul soul to scrape static pages.
    """
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            #Xample: find all elements of class 'container
            containers = soup.find_all(class_='container')
            with open(file_name, 'w') as file:
                for container in containers:
                    file.write(container.text + '\n\n')

# def run_async_scraper(url, file_name):
#     """
#     Runs the asynchronous scraper to fetch the page content using aiohttp,
#     """
#     asyncio.run(fet)page

# Example usage:
# Decide which fuction to use based on the page page's requiremnets (how would I decide that?)
# For dynmaic pages with heavy Javacsripts - Probably best to use Selenium
# For static pages - Probably best to use aiohttp
# Make sure to initialize the driver before calling the function

scrape_page_selenium(driver, "https://www.python.org/about/", "scraped_about_page.txt")

scrape_page_selenium(driver, "https://www.python.org/", "scraped_home_page.txt")
scrape_page_selenium(driver,"https://www.python.org/psf/conduct/", "scraped_conduct_page.txt")

# add your timeout
driver.quit()