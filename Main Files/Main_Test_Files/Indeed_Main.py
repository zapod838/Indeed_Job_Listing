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
    #element = driver.find_element(By.NAME, 'q')
    #element.send_keys('data analyst')
    #element = driver.find_element(By.NAME, 'l')
    #element.send_keys('Dublin')
    elements = driver.find_elements(By.CLASS_NAME, 'job_seen_beacon')
    for element in elements:
        title_value = element.find_element(By.TAG_NAME, 'h2')
        #company_names = element.find_element(By.CLASS_NAME, 'heading6 company_location tapItem-gutter companyInfo')
        company_name = element.find_element(By.CSS_SELECTOR, '.companyName')
        company_location = element.find_element(By.CLASS_NAME, 'companyLocation')
        links = element.find_element(By.TAG_NAME, 'a')
        link = links.get_attribute('href')



        print("Job Title:", title_value.text)
        print("Company:",  company_name.text)
        print("Company_Location:",  company_location.text)
        print("Job Link:", link)


        print("-----------------------")


    #company_names = driver.find_elements(By.CLASS_NAME, 'heading6 company_location tapItem-gutter companyInfo')
    #for company in company_names:
        #company_names = driver.find_elements(By.XPATH, '//*[@id="mosaic-provider-jobcards"]/ul/li[2]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[2]/span')
    #for company in company_names:
        #company_name = company.find_element(By.TAG_NAME, 'span')
        #print(company_name.text)

    time.sleep(20)    
except NoSuchElementException:
    print("No such element found on the page!")

finally:
    # Close the browser window and quit the driver.
    driver.quit()
