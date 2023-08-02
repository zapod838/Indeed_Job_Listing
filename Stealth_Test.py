from selenium import webdriver
from selenium_stealth import stealth
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


import time

ser = Service(r"C:\Users\LastC\Downloads\chromedriver_win32")
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, service=ser)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
try:
    driver.get("https://ie.indeed.com/")
    wait = WebDriverWait(driver, 10)
    time.sleep(5)
    element = driver.find_element(By.NAME, 'q')
    element.send_keys('data analyst')
    element = driver.find_element(By.NAME, 'l')
    element.send_keys('Dublin')
    time.sleep(5)
    #button = driver.find_element(By.CLASS_NAME, 'yosegi-FilterPill-pillLabel')
    #button.click()
    element.submit()

    time.sleep(10)    
    while True:
        user_input = input("Press 'q' and 'Enter' to quit the program: ")
        if user_input.lower() == "q":
            break
except NoSuchElementException:
    print("No such element found on the page!")


finally:
    # Close the web driver and exit the script
    driver.quit()