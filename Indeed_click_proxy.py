from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random
import config
from selenium import webdriver
import time

def rand_proxy():
    proxy = random.choice(config.ips)
    return proxy

#ser = Service(r"C:\Users\LastC\Downloads\chromedriver_win32")
#driver = webdriver.Chrome(service=ser)
try:
    chrome_options = webdriver.ChromeOptions()
    proxy = rand_proxy()
    chrome_options.add_argument(f'--proxy-server={proxy}')
    driver = webdriver.Chrome(options=chrome_options)
    #driver.get('https://whatismyipaddress.com/')

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

    print(rand_proxy())

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
