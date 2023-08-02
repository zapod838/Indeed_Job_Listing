from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import random
import config

def rand_proxy():
    proxy = random.choice(config.ips)
    return proxy

def main():
    chrome_options = webdriver.ChromeOptions()
    proxy = rand_proxy()
    chrome_options.add_argument(f'--proxy-server={proxy}')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://ie.indeed.com/jobs?q=data+analyst&fromage=14&vjk=b7911c4e372a69ea")
    wait = WebDriverWait(driver, 30)
    next_page = driver.find_element(By.XPATH, '//*[@id="jobsearch-JapanPage"]/div/div/div[5]/div[1]/nav/div[2]/a')
    next_page.click()


    print(rand_proxy())    

    time.sleep(20)
main()    

  