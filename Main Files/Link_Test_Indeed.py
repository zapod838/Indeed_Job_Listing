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
    driver.get("https://ie.indeed.com/jobs?q=data+analyst&l=ireland&start=10")
    #wait = WebDriverWait(driver, 10)
    #element = driver.find_element(By.NAME, 'q')
    #element.send_keys('data analyst')
    #element = driver.find_element(By.NAME, 'l')
    #element.send_keys('cork')
    time.sleep(20)
    #element.submit()

    #time.sleep(15)

    job_cards = driver.find_elements(By.XPATH, '//div[contains(@class, "job_seen_beacon")]')

    # Wait for all job cards to be visible before extracting information
    #wait = WebDriverWait(driver, 10)

    #wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//div[contains(@class, "job_seen_beacon")]')))
    #wait.until(lambda driver: driver.find_element(By.XPATH, './/h2'))
    #wait = WebDriverWait(driver, 250)

    #wait.until(EC.visibility_of_all_elements_located((By.XPATH, './/h2')))
    #time.sleep(10)

    for card in job_cards:
        try:
            # Check if the job card has all the required elements
            title_element = card.find_element(By.XPATH, './/h2')
            company_element = card.find_element(By.XPATH, './/span[contains(@class, "companyName")]')
            #location_element = card.find_element(By.XPATH, './/div[contains(@class, "companyLocation")]')

            # Extract job title, company, and location
            title_value = title_element.text
            company_name = company_element.text
            #company_location = location_element.text

            # Print the extracted information
            print("Job Title:", title_value)
            print("Company:", company_name)
            #print("Company_Location:", company_location)

            # Extract and print the job link
            link_element = card.find_element(By.TAG_NAME, 'a')
            link = link_element.get_attribute('href')
            print("Job Link:", link)
            print("-----------------------")

        except NoSuchElementException:
            # If any of the elements are not found, skip this job card and continue with the next one.
            print("Skipping job card without complete information.")
            print("-----------------------")
            continue

    time.sleep(10)


        
except NoSuchElementException:
    print("No such element found on the page!")

finally:
    # Close the browser window and quit the driver.
    driver.quit()      