from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

ser = Service(r"C:\Users\LastC\Downloads\chromedriver_win32")

driver = webdriver.Chrome(service=ser)

try:
    driver.get("https://ie.indeed.com/jobs?q=data+analyst&fromage=14&vjk=b7911c4e372a69ea")
    wait = WebDriverWait(driver, 10)

    elements = driver.find_elements(By.CLASS_NAME, 'job_seen_beacon')
    for element in elements:
        posted_at = element.find_element(By.CLASS_NAME, 'date')
        links = element.find_element(By.TAG_NAME, 'a')
        link = links.get_attribute('href')

        print("Posted at:", posted_at.text)
        print("Links:", link) 
        print("-----------------------")


    time.sleep(5)
except NoSuchElementException:
    print("No such element found on the page!")

finally:
    # Close the browser window and quit the driver.
    driver.quit()            
