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

driver.get('https://jobs.vishay.com/search/?q=&q2=&alertId=&locationsearch=&title=&department=&shifttype=united+states')

company_name = []
job_title = []
job_location = []
job_type = []
job_links = []
job_description = []

try:
    main = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'content'))
    )
    try:
        pages = main.find_elements_by_tag_name('b')
        total_pages = (int(pages[1].text) // 25) + 2
        if total_pages > 1:
            for x in range(2, total_pages + 1):
                try:
                    main = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'content'))
                    )
                    job_titles = main.find_elements_by_class_name('jobTitle-link')
                    job_titles = job_titles[0::2]
                    for job in job_titles:
                        company_name.append('Vishay Intertechnology')
                        title = job.text
                        job_title.append(title)
                    all_links = main.find_elements_by_class_name('jobTitle-link')
                    all_links = all_links[1::2]



                finally:
                    pass

                print(job_title)
                print(len(job_title))

                for link in all_links:
                    try:
                        wait_main_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'jobTitle-link')))
                        actual_link = link.get_attribute("href")
                        job_links.append(actual_link)

                    finally:
                        pass
                print(job_links)
                print(len(job_links))
                types = main.find_elements_by_class_name('jobDepartment')
                for type in types:
                    dept = type.text
                    job_type.append(dept)
                job_type.pop(0)
                print(job_type)
                print(len(job_type))

                location = main.find_elements_by_class_name('jobShifttype')
                for job in location:
                    new_job = job.text
                    job_location.append(new_job)
                job_location.pop(0)
                print(job_location)
                print(len(job_location))
                print('total page equals ' + str(total_pages))
                if x < total_pages:
                    more_jobs = driver.find_element_by_link_text(str(x))
                    print('clicking page ' + str(x))
                    more_jobs.click()
                    time.sleep(5)
                else:
                    pass

        else:
            job_titles = main.find_elements_by_class_name('jobTitle-link')
            print(job_titles)
            for job in job_titles:
                company_name.append('Vishay Intertechnology')
                title = job.text
                job_title.append(title)
            print(job_title)
            print(len(job_title))

            type = main.find_elements_by_class_name('jobDepartment')
            for job in type:
                job_type.append(job.text)
            print(job_type)
            print(len(job_title))

            location = main.find_elements_by_class_name('jobShifttype')
            for job in location:
                job_location.append(job.text)
            print(job_location)

            all_links = main.find_elements_by_tag_name('a')
            for link in all_links:
                link_list.append(link.get_attribute("href"))
            print(job_links)
            print(len(job_links))



    finally:
        pass
    for link in job_links:
        driver.get(link)
        try:
            wait_main_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'jobdescription')))
            desc = wait_main_2.text
            job_description.append(desc)
            time.sleep(5)
        finally:
            pass
    print('company name: ' + str(len(company_name)))
    print('job title: ' + str(len(job_title)))
    print('job location: ' + str(len(job_location)))
    print('job type: ' + str(len(job_type)))
    print('job link: ' + str(len(job_links)))
    print('job description: ' + str(len(job_description)))

    d = {'company_name': company_name, 'job_title': job_title, 'job_location': job_location, 'job_type': job_type, 'job_link': job_links, 'job_description': job_description}
    df = pd.DataFrame(data=d)
    df.to_csv('vishay_intertechnology_jobs.csv')

finally:
    driver.quit()
