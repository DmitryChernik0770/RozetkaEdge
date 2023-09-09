import os
from selenium import webdriver
import time

# Путь к драйверу Edge WebDriver
edge_driver_path = r'D:\VSCode\Edge\msedgedriver.exe'

driver = webdriver.Edge(executable_path=edge_driver_path)

driver.get("https://rozetka.com.ua/")

time.sleep(2)

try:
    element = driver.find_element_by_xpath('//*[@class="search-form__microphone ng-star-inserted"]')
    print("Кнопка 'Голосового ввода' найден на сайте.")
except Exception as e:
    print("Кнопка 'Голосового ввода' не найден на сайте. Ошибка:", str(e))

driver.quit()
