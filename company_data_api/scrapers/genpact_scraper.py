import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re



options = Options()
options.binary = FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")
options.set_preference('browser.download.folderList', 2)
options.set_preference('browser.download.manager.showWhenStarting', False)
options.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/octet-stream,application/vnd.ms-excel')
PATH = r"C:\Program Files (x86)\geckodriver.exe"
driver = webdriver.Firefox(executable_path=PATH, options=options)
actions = ActionChains(driver)

"""
driver.get('https://www.genpact.com/careers/job-search?query=')

company_name = []
job_title = []
job_location = []
job_type = []
job_links = []
job_description = []

try:
    main = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'app-careers'))
    )
    driver.maximize_window();
    time.sleep(3)
    select_us = driver.find_element_by_tag_name('select')
    select_us.send_keys('U')
    select_us.send_keys(Keys.DOWN)
    select_us.send_keys(Keys.RETURN)
    time.sleep(3)
    pagination = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'job-pagination-bottom')))
    pages = pagination.find_elements_by_tag_name('a')
    pages_to_click = []
    test_pages_to_click = []
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    for page in pages:
        pages_to_click.append(page.text)
    print(pages_to_click[-1])
    for x in range(2, int(pages_to_click[-1])+2):
        print(x)
        job_link_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'job-description-wrapper-url')))
        link_box = driver.find_elements_by_class_name('job-description-wrapper-url')
        for link in link_box:
            link_to_add = link.get_attribute('href')
            job_links.append(link_to_add)
            company_name.append('Genpact')
            print(link_to_add)
        print(len(job_links))
        if x <= int(pages_to_click[-1]):
            ignored_exceptions = (NoSuchElementException,StaleElementReferenceException,)
            time.sleep(5)
            print('waiting for element ' + str(x))
            pagination = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'job-pagination-bottom')))
            test_pages = pagination.find_elements_by_tag_name('a')
            test_pages_to_click = []
            last_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            for test_page in test_pages:
                test_pages_to_click.append(test_page.text)
                print(test_page.text)
            time.sleep(10)
            main = WebDriverWait(driver, 30, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.LINK_TEXT, str(x))))
            # more_jobs = driver.find_element_by_link_text(str(x))
            print('moving to page ' + str(x))
            ActionChains(driver).move_to_element(driver.find_element_by_link_text(str(x))).perform()
            time.sleep(3)
            driver.execute_script("window.scrollBy(0, -50);")
            driver.execute_script("window.scrollBy(0, 40);")
            driver.execute_script("window.scrollBy(0, -30);")
            time.sleep(2)
            print('clicking page ' + str(x))
            ActionChains(driver).click(driver.find_element_by_link_text(str(x))).perform()
            time.sleep(5)
        else:
            pass


    d = {'company_name': company_name, 'job_link': job_links}
    df = pd.DataFrame(data=d)
    df.to_csv('genpact_jobs.csv')
    # job_link_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'job-description-wrapper-url')))
    # link_box = driver.find_elements_by_class_name('job-description-wrapper-url')
    # for link in link_box:
    #     link_to_add = link.get_attribute('href')
    #     print(link_to_add)

finally:
    driver.quit()



"""
genpact_jobs = pd.read_csv('genpact_jobs.csv', index_col=0)


job_title = []
job_location = []
job_type = []
job_description = []
posted_date = []
scraped_date = []

sample = genpact_jobs[:10]

for link in sample['job_link']:
    driver.get(link)
    time.sleep(3)
    try:
        main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'job-description'))
        )
        time.sleep(5)
        new_job_description = driver.find_elements_by_id('p')
        for element in new_job_description:
            print(element.text)
            # job_title.append(new_job_title.text)
    finally:
        pass
driver.quit()





"""
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


"""
