import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
url="https://tomsk.hh.ru/vacancies/programmist"

driver.get(url)
time.sleep(5)

# vacancies=driver.find_elements(By.CLASS_NAME,'vacancy-card--H8LvOiOGPll0jZvYpxIF')
vacancies=driver.find_elements(By.CLASS_NAME,'vacancy-info--I4f9shQE53f9Luf5lkMw')
print(vacancies)
parsed_data=[]

for vacancy in vacancies:
    try:
        title=vacancy.find_element(By.CSS_SELECTOR, 'span[data-qa="serp-item__title-text"]').text
        company=vacancy.find_element(By.CSS_SELECTOR, 'span[data-qa="vacancy-serp__vacancy-employer-text"]').text



        link = vacancy.find_element(By.CSS_SELECTOR, 'a[data-qa="serp-item__title"]').get_attribute('href')
        salary=vacancy.find_element(By.CSS_SELECTOR, 'div.wide-container-magritte--MZDT2K1sum_GdjUzT50m div span').text
        # link = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-2-10 magritte-link_style_neutral___iqoW0_4-2-10 magritte-link_enable-visited___Biyib_4-2-10').get_attribute('href')
    except:
        print("произошла ошибка при парсинге")
        continue
    parsed_data.append([title,company,salary,link])

driver.quit()

with open('hh.csv', 'w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)



