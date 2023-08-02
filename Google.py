from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time

ser = Service(r"C:\Users\LastC\Downloads\chromedriver_win32")

driver = webdriver.Chrome(service=ser)

try:
    driver.get("https://www.google.in/")
    wait = WebDriverWait(driver, 10)
    element = driver.find_element(By.NAME, 'q')
    element.send_keys('selenium')
    time.sleep(1)

    element.submit()

    while True:
        user_input = input("Press 'q' and 'Enter' to quit the program: ")
        if user_input.lower() == "q":
            break
    

except NoSuchElementException:
    print("No such element found on the page!")


finally:
    # Close the web driver and exit the script
    driver.quit()
