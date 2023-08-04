from undetected_chromedriver import Chrome, ChromeOptions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import csv

options = ChromeOptions()
options.add_argument("--headless")  # Run the browser in headless mode (without GUI).
options.add_argument("--no-sandbox")  # Required for running Chrome in headless mode on some systems.

# Create the undetected_chromedriver instance
driver = Chrome(options=options)

def scrape_data(num_pages_to_scrape):
    
    try:
        start_url = "https://ie.indeed.com/jobs?q=data+analyst&l=cork&start={}"
        page_number = 0
        with open('Indeed_cork_jobs.csv', mode='w', newline='', encoding='UTF-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Job Title", "Company", "Location", "Link"])

            for _ in range(num_pages_to_scrape):
                url = start_url.format(page_number)
                driver.get(url)
                time.sleep(10)

                job_cards = driver.find_elements(By.XPATH, '//div[contains(@class, "job_seen_beacon")]')

                for card in job_cards:
                    try:
                        # Check if the job card has all the required elements
                        title_element = card.find_element(By.XPATH, './/h2')
                        company_element = card.find_element(By.XPATH, './/span[contains(@class, "companyName")]')
                        location_element = card.find_element(By.XPATH, './/div[contains(@class, "companyLocation")]')
                        link_element = card.find_element(By.TAG_NAME, 'a')
                        
                        # Extract job title, company, and location
                        title_value = title_element.text
                        company_name = company_element.text
                        company_location = location_element.text
                        link = link_element.get_attribute('href')

                        # Write the scraped data to the CSV file
                        writer.writerow([title_value, company_name, company_location, link])

                    except NoSuchElementException:
                        # If any of the elements are not found, skip this job card and continue with the next one.
                        continue

                # Increment the page number by 10 for the next page
                page_number += 10

                # Check if there are any more job cards on the next page
                if len(job_cards) == 0:
                    # If there are no more job cards, it indicates we have reached the last page
                    break

                time.sleep(10)

    except NoSuchElementException:
        print("No such element found on the page!")

    finally:
        # Close the browser window and quit the driver.
        driver.quit()

    print(f"Data from {num_pages_to_scrape} pages has been successfully scraped and saved to 'Indeed-jobs.csv'.")

scrape_data(num_pages_to_scrape=3)
