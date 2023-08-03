import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


options = ChromeOptions()
options.add_argument("--headless")  # Run the browser in headless mode (without GUI).
options.add_argument("--no-sandbox")  # Required for running Chrome in headless mode on some systems.
#Create a new instance of the Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
driver = Chrome(options=options)


driver.get("https://ie.indeed.com/jobs?q=data+analyst&fromage=14&vjk=b7911c4e372a69ea")
time.sleep(20)
#elements = driver.find_elements(By.CLASS_NAME, 'job_seen_beacon')
#driver.get("https://ie.indeed.com/jobs?q=data+analyst&fromage=14&vjk=b7911c4e372a69ea")
#time.sleep(20)

# Use find_elements to get all elements that match the XPath
job_cards = driver.find_elements(By.XPATH, '//div[contains(@class, "job_seen_beacon")]')

for card in job_cards:
    # Extract job title, company, and location using relative XPath expressions
    title_value = card.find_element(By.XPATH, './/h2').text
    company_name = card.find_element(By.XPATH, './/span[contains(@class, "companyName")]').text
    company_location = card.find_element(By.XPATH, './/div[contains(@class, "companyLocation")]').text

    # Print the extracted information
    print("Job Title:", title_value)
    print("Company:", company_name)
    print("Company_Location:", company_location)

    # Extract and print the job link
    link_element = card.find_element(By.TAG_NAME, 'a')
    link = link_element.get_attribute('href')
    print("Job Link:", link)
    print("-----------------------")
