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
    driver = webdriver.Chrome(service=ser)
    driver.get("https://ie.indeed.com/")
    wait = WebDriverWait(driver, 10)
    element = driver.find_element(By.NAME, 'q')
    element.send_keys('data analyst')
    element = driver.find_element(By.NAME, 'l')
    element.send_keys('Dublin')
    time.sleep(5)
    
except NoSuchElementException:
    print("No such element found on the page!")

finally:
    # Close the browser window and quit the driver.
    driver.quit()    