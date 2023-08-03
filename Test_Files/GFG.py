from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time


try:
    driver = webdriver.Chrome()
    driver.get("https://practice.geeksforgeeks.org/")

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, "search-bar")))
    time.sleep(5)
    option = element.find_element(By.XPATH, '//*[@id="search-bar"]') 
    option.click()
    time.sleep(5)
    option.clear()  # Clear existing text (optional but useful)
    option.send_keys("Arrays")


except NoSuchElementException:
    print("No such element found on the page!")
finally:
    driver.quit()


