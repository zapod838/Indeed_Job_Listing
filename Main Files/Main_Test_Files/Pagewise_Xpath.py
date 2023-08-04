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

def scroll_down_multiple_times():
    scroll_pause_time = 10  # Adjust this value to control the scrolling speed
    max_scroll_attempts = 10 
    for _ in range(max_scroll_attempts):
        #Scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #Wait for a short pause to allow the page to load new elements
        time.sleep(scroll_pause_time)

driver.get("https://ie.indeed.com/")
driver.maximize_window()
time.sleep(1)
element = driver.find_element(By.NAME, 'q')
element.send_keys('data analyst')
element = driver.find_element(By.NAME, 'l')
element.send_keys('cork')
time.sleep(5)
element.submit()
time.sleep(15)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

scroll_down_multiple_times()

button = driver.find_element(By.XPATH, "//a[@data-testid='pagination-page-next']")
#driver.execute_script("arguments[0].scrollIntoView();", button)
#driver.execute_script("arguments[0].click();", button)
#time.sleep(10)

button.click()
driver.maximize_window()
#scroll_down_multiple_times()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, './/div[contains(@class, "companyLocation")]')))
time.sleep(10)

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

time.sleep(10)

