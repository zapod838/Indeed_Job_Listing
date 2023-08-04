from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

#options = ChromeOptions()
#options.add_argument("--headless")  # Run the browser in headless mode (without GUI).
#options.add_argument("--no-sandbox")  # Required for running Chrome in headless mode on some systems.
ser = Service(r"C:\Users\LastC\Downloads\chromedriver_win32")

def scrape_data_from_multiple_pages(url):

    driver = webdriver.Chrome(service=ser)

    try:
        # List to store scraped data
        scraped_data = []
        # Loop through the pages
        current_page = 1
        while True:
            # Navigate to the current page
            driver.get(f'{url}?page={current_page}')
            time.sleep(10)
            # Scrape data from the current page
            page_data = scrape_data_from_current_page(driver)
            time.sleep(10)
            # If no data found on the current page, stop the loop
            if not page_data:
                break

            # Add the scraped data from the current page to the main list
            scraped_data.extend(page_data)
            time.sleep(10)

            # Move to the next page
            current_page += 1
            time.sleep(10)

        return scraped_data

    finally:
        # Close the browser window and quit the driver
        driver.quit()

def scrape_data_from_current_page(driver):
    # Function to scrape data from the current page
    # Replace the following code with your specific scraping logic
    # For example, find elements and extract data using find_element_* and get_attribute() methods.
    # Example:
    driver = webdriver.Chrome(service=ser)
    elements = driver.find_elements(By.CLASS_NAME, 'job_seen_beacon')
    scraped_data = []
    for element in elements:
        title_value = element.find_element(By.TAG_NAME, 'h2')
        company_name = element.find_element(By.CSS_SELECTOR, '.companyName')
        time.sleep(10)
        scraped_data.append({
            'title': title_value.text,
            'company': company_name.text,
            # Add other data fields...
        })
    return scraped_data

base_url = 'https://ie.indeed.com/jobs?q=data+analyst&fromage=14&vjk=b7911c4e372a69ea'  # Replace this with the actual base URL of the webpage
data = scrape_data_from_multiple_pages(base_url)
print(data)
