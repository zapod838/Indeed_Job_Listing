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
    time.sleep(15)
    button = driver.find_element(By.XPATH, '//*[@id="jobsearch-JapanPage"]/div/div/div[5]/div[1]/nav/div[2]/a')
    #time.sleep(10)

    driver.execute_script("arguments[0].scrollIntoView();", button)
    #driver.execute_script("arguments[0].click();", button)
    time.sleep(10)

    button.click()
    time.sleep(10)
    elements = driver.find_elements(By.XPATH, '//*[@id="mosaic-provider-jobcards"]/ul/li[1]/div/div[1]/div/div[1]/div')#div Element
    for element in elements:
        title_value = element.find_element(By.XPATH, '//*[@id="mosaic-provider-jobcards"]/ul/li[1]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2')
        company_name = element.find_element(By.XPATH, '//*[@id="mosaic-provider-jobcards"]/ul/li[1]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[2]/span')
        company_location = element.find_element(By.XPATH, '//*[@id="mosaic-provider-jobcards"]/ul/li[1]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[2]/div') #div Element
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