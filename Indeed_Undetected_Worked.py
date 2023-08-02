from undetected_chromedriver import Chrome, ChromeOptions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

options = ChromeOptions()
options.add_argument("--headless")  # Run the browser in headless mode (without GUI).
options.add_argument("--no-sandbox")  # Required for running Chrome in headless mode on some systems.

# Create the undetected_chromedriver instance
driver = Chrome(options=options)

try:
    driver.get("https://ie.indeed.com/")
    wait = WebDriverWait(driver, 10)
    element = driver.find_element(By.NAME, 'q')
    element.send_keys('data analyst')
    element = driver.find_element(By.NAME, 'l')
    element.send_keys('cork')
    time.sleep(5)
    element.submit()

    time.sleep(15)

    elements = driver.find_elements(By.CLASS_NAME, 'job_seen_beacon')#div Element
    for element in elements:
        title_value = element.find_element(By.TAG_NAME, 'h2')
        #company_names = element.find_element(By.CLASS_NAME, 'heading6 company_location tapItem-gutter companyInfo')
        company_name = element.find_element(By.CSS_SELECTOR, '.companyName') #Span Element
        company_location = element.find_element(By.CLASS_NAME, 'companyLocation') #div Element
        links = element.find_element(By.TAG_NAME, 'a')
        link = links.get_attribute('href') #Link attribute

        print("Job Title:", title_value.text)
        print("Company:",  company_name.text)
        print("Company_Location:", company_location.text)
        print("Job Link:", link)


        print("-----------------------")

    time.sleep(10)
except NoSuchElementException:
    print("No such element found on the page!")

finally:
    # Close the browser window and quit the driver.
    driver.quit()    

