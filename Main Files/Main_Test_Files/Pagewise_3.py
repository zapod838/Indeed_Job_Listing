from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


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
    
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(15)
    #wait = WebDriverWait(driver, 10)

    #def scroll_down_multiple_times():
        #scroll_pause_time = 10  # Adjust this value to control the scrolling speed
        #max_scroll_attempts = 10 
        #for _ in range(max_scroll_attempts):
            # Scroll down to the bottom of the page
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for a short pause to allow the page to load new elements
            #time.sleep(scroll_pause_time)

    button = driver.find_element(By.XPATH, '//*[@id="jobsearch-JapanPage"]/div/div/div[5]/div[1]/nav/div[2]/a')
    #time.sleep(10)

    driver.execute_script("arguments[0].scrollIntoView();", button)
    #driver.execute_script("arguments[0].click();", button)
    #wait = WebDriverWait(driver, 10)
    time.sleep(10)

    #driver.execute_script("arguments[0].click();", button)
    button.click()
    #wait = WebDriverWait(driver, 100)
    #driver.implicitly_wait(20)
    #scroll_down_multiple_times()

    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #driver.implicitly_wait(10)
    #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'companyLocation')))
    time.sleep(10)
    elements = driver.find_elements(By.CLASS_NAME, 'job_seen_beacon')#div Element
    for element in elements:
        title_value = element.find_element(By.TAG_NAME, 'h2')
        company_name = element.find_element(By.CSS_SELECTOR, '.companyName')
        company_location = element.find_element(By.CLASS_NAME, 'companyLocation') #div Element
        links = element.find_element(By.TAG_NAME, 'a')
        link = links.get_attribute('href')

        print("Job Title:", title_value.text)
        print("Company:",  company_name.text)
        print("Company_Location:", company_location.text)
        print("Job Link:", link)
        print("-----------------------")    

        #time.sleep(1)
    
    time.sleep(10)
    
except NoSuchElementException:
    print("No such element found on the page!")

finally:
    # Close the browser window and quit the driver.
    driver.quit()      