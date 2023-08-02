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
    driver.get("https://ie.indeed.com/jobs?q=data+analyst&fromage=14&vjk=b7911c4e372a69ea")
    time.sleep(20)
    elements = driver.find_elements(By.CLASS_NAME, 'job_seen_beacon')
    #for element in elements:
    title_value = driver.find_elements(By.XPATH, './/*[@id="mosaic-provider-jobcards"]/ul/li[1]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2')
    company_name = driver.find_elements(By.XPATH, './/*[@id="mosaic-provider-jobcards"]/ul/li[1]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[2]/span')
    company_location = driver.find_elements(By.XPATH, './/*[@id="mosaic-provider-jobcards"]/ul/li[1]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[2]/div') #div Element

    for job in title_value:
        print("Job Title:", job.text)
    for company in company_name:    
        print("Company:", company.text)  
    for location in company_location:
        print("Company_Location:", location.text)
    for element in elements:
        links = element.find_element(By.TAG_NAME, 'a')
        link = links.get_attribute('href')
        print("Job Link:", link)
        print("-----------------------")    

        #time.sleep(1)
    
    time.sleep(10)
    
except NoSuchElementException:
    print("No such element found on the page!")

finally:
    # Close the browser window and quit the driver.
    driver.quit()      