from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium import webdriver
import time

ser = Service(r"C:\Users\LastC\Downloads\chromedriver_win32")


try:
    driver = webdriver.Chrome(service=ser)
    driver.get("https://www.coursera.org/degrees/data-science")
    wait = WebDriverWait(driver, 10)
    # Wait indefinitely until the user decides to exit
    # Wait for the course listings to be visible
    #wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="main"]/div[4]/div/div[3]')))
    course_title_element = driver.find_elements(By.XPATH, '//*[@id="main"]/div[4]/div/div[3]/div[1]/a/div/div/div[2]/h3')
    #course_listings = driver.find_elements(By.XPATH, '//*[@id="main"]/div[4]/div/div[3]/div[1]')
    #course_listings = driver.find_elements(By.CLASS_NAME, 'cds-9 css-0 cds-11 cds-grid-item cds-56 cds-64 cds-76')
    #print("Course Title:", course_title.text)
    course_list = []
    for course in course_title_element:
        #course_title_element = course.find_element(By.CLASS_NAME, 'cds-119 css-17nllbg cds-121')
        #course_title_element = driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/div/div[3]/div[1]/a/div/div/div[2]/h3')
        course_title = course.text
    
        print("Title:", course_title)
 

    time.sleep(5)

    while True:
        user_input = input("Press 'q' and 'Enter' to quit the program: ")
        if user_input.lower() == "q":
            break
except NoSuchElementException:
    print("No such element found on the page!")


finally:
    # Close the web driver and exit the script
    driver.quit()
