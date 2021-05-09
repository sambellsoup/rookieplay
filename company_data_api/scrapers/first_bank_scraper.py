import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

comps = pd.read_csv('sample_companies.csv', index_col=0)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)



driver.get('https://careers.firstrepublic.com/')
# print(driver.title)

# num_jobs  = driver.find_element_by_class_name("results-count")
# search.send_keys("data")
# search.send_keys(Keys.RETURN)
# num_jobs = re.search("\d+", num_jobs.text)
# print(num_jobs.text)

company_name = []
job_title = []
job_location = []
job_type = []
link_list = []
job_description = []

try:
    main = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'results-list'))
    )
    # links = main.find_elements_by_tag_name('a')
    # for link in links:
        # job_links.append(link.get_attribute("href"))
    # print(job_links)
    # print(len(job_links))
    try:
        while True:
            more_jobs = driver.find_element_by_link_text('Show more')
            more_jobs.click()
            time.sleep(5)
    except:
        job_titles = main.find_elements_by_class_name('flush')
        for job in job_titles:
            company_name.append('First Republic Bank')
            title = job.text
            job_title.append(title)
        print(job_title)
        print(len(job_title))
        job_details = main.find_elements_by_tag_name('h6')
        for detail in job_details:
            extras = detail.text
            details.append(extras)
        job_type = details[1::2]
        print(job_type)
        print(len(job_type))
        job_location = details[0::2]
        print(job_location)
        print(len(job_location))
        all_links = main.find_elements_by_tag_name('a')
        for link in all_links:
            link_list.append(link.get_attribute("href"))
            job_links = link_list[0::2]
        print(job_links)
        print(len(job_links))
        # link = driver.find_element_by_link_text('View Job')
        # link.click()
    # time.sleep(5)
    # driver.back()
    d = {'company_name': company_name, 'job_title': job_title, 'job_location': job_location, 'job_type': job_type, 'job_link': job_links}
    df = pd.DataFrame(data=d)
    df.to_csv('first_republic_bank.csv')

finally:
    driver.quit()


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
"""

frb = pd.read_csv('first_republic_bank.csv', index_col=0)

job_description = []
for link in frb['job_link']:
    driver.get(link)
    try:
        main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'job-description')))
        description = main.find_elements_by_tag_name('p')
        # job_description.append(description.text)
        print(len(description))
        temp_descriptions = []
        for x in range(len(description)):
            temp_descriptions.append(description[x].text)
        joined_description = ' '.join(temp_descriptions)
        job_description.append(joined_description)
        time.sleep(5)
        print(job_description)
    finally:
        pass
        # print(job_description)
        # print(len(job_description))
frb['job_description'] = job_description
frb.to_csv('first_republic_bank_jobs.csv')
driver.quit()
