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
    driver.get('https://whatismyipaddress.com/')

    print(rand_proxy())
    time.sleep(10)

main()    

