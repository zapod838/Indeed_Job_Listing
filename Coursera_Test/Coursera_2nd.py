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
    driver.get("https://www.coursera.org/degrees/data-science")
    wait = WebDriverWait(driver, 10)
    elements_with_class_content = driver.find_elements(By.CLASS_NAME, 'css-1foy7y2')

    for element in elements_with_class_content:
        heading = element.find_element(By.TAG_NAME, 'h3').text

        print(heading)

    time.sleep(10)    
finally:
    # Close the browser window and quit the driver.
    driver.quit()
