import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
url="https://www.divan.ru/category/svet"

driver.get(url)
time.sleep(5)

# vacancies=driver.find_elements(By.CLASS_NAME,'vacancy-card--H8LvOiOGPll0jZvYpxIF')
products=driver.find_elements(By.CSS_SELECTOR,'div.LlPhw')
print(products)
parsed_data=[]

for product in products:
    try:
        name=product.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
        price=product.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        link = product.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    except:
        print("произошла ошибка при парсинге")
        continue
    parsed_data.append([name,price,link])

driver.quit()

with open('divan_svet.csv', 'w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название светильника', 'Цена', 'Ссылка на светильник'])
    writer.writerows(parsed_data)


