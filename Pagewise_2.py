from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Replace 'YOUR_CHROMEDRIVER_PATH' with the path where you saved the ChromeDriver executable.
options = ChromeOptions()
options.add_argument("--headless")  # Run the browser in headless mode (without GUI).
options.add_argument("--no-sandbox")  # Required for running Chrome in headless mode on some systems.
#Create a new instance of the Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
driver = Chrome(options=options)

try:
    driver.get("https://ie.indeed.com/")
    #driver.maximize_window()
    time.sleep(1)
    element = driver.find_element(By.NAME, 'q')
    element.send_keys('data analyst')
    element = driver.find_element(By.NAME, 'l')
    element.send_keys('cork')
    time.sleep(5)
    element.submit()
    time.sleep(10)

    #wait = WebDriverWait(driver, 10)

    button = driver.find_element(By.XPATH, '//*[@id="jobsearch-JapanPage"]/div/div/div[5]/div[1]/nav/div[6]/a')
    time.sleep(10)

    driver.execute_script("arguments[0].scrollIntoView();", button)
    driver.execute_script("arguments[0].click();", button)
    #wait = WebDriverWait(driver, 10)
    time.sleep(10)
    
    #driver.execute_script("arguments[0].click();", button)
    #button.click()
    #time.sleep(30)

    elements = driver.find_elements(By.CLASS_NAME, 'job_seen_beacon')#div Element
    for element in elements:
        title_value = element.find_element(By.TAG_NAME, 'h2')
        company_name = element.find_element(By.CSS_SELECTOR, '.companyName')
        print("Job Title:", title_value.text)
        print("Company:",  company_name.text)
        print("-----------------------")    

    time.sleep(1)
    while True:
        user_input = input("Press 'q' and 'Enter' to quit the program: ")
        if user_input.lower() == "q":
            break
except NoSuchElementException:
    print("No such element found on the page!")

finally:
    # Close the browser window and quit the driver.
    driver.quit()      

