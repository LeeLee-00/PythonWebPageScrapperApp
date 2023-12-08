from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
import os

# Configure Selenium to run headless
options = Options()
options.headless = True
options.add_argument("--no-sandbox")  # This can be required in a cloud environment
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Get the current working directory
cwd = os.getcwd()

# Set the path to the WebDriver (ensure this path is correct and permissions are set)
webdriver_path = os.path.join(cwd, 'msedgedriver.exe')  # 'msedgedriver' if using Edge

# Setup WebDriver

service = Service(webdriver_path)
driver = webdriver.Edge(service=service, options=options)

# Navigate to the Python "About" page
driver.get("https://www.python.org/about/")

# Scrape heading and paragraph text and save to a file
with open('scraped_about_page.txt', 'w') as file:
    # Assuming you want to scrape all the <p> and <h1>, <h2> tags etc.
    headings = driver.find_elements("css selector",'p, h1, h2, h3, h4, h5, h6')
    paragraphs = driver.find_elements("css selector",'p')
    
    # Write headings to file
    for heading in headings:
        file.write(heading.text + '\n\n')
    
    # Write paragraphs to file
    for paragraph in paragraphs:
        file.write(paragraph.text + '\n\n')

driver.get("https://www.python.org/")

with open('scraped_home_page.txt', 'w') as file:
    # Assuming you want to scrape all the <p> and <h1>, <h2> tags etc.
    headings = driver.find_elements("css selector",'p, h1, h2, h3, h4, h5, h6')
    paragraphs = driver.find_elements("css selector",'p')
    
    # Write headings to file
    for heading in headings:
        file.write(heading.text + '\n\n')
    
    # Write paragraphs to file
    for paragraph in paragraphs:
        file.write(paragraph.text + '\n\n')   

# regarding the permision error, ensure that WebDrier file ('msedgedriver') has the execution permmision set:
# Navigate to the directory containing the WebDriver - cd /path/to/your/project/drivers  
# Set the WebDriver as executable via in your bash terminal: chmod +x msedgedriver  

# add your timeout
driver.quit()
