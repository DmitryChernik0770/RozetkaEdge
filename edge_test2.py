import os
from selenium import webdriver
import time

# Путь к драйверу Edge WebDriver
edge_driver_path = r'D:\VSCode\Edge\msedgedriver.exe'

driver = webdriver.Edge(executable_path=edge_driver_path)

driver.get("https://rozetka.com.ua/")

time.sleep(2)

try:
    button = driver.find_element_by_xpath('//li[3]//*[@class="header__button ng-star-inserted"]')
    print("Кнопка пользователя найдена на сайте.")
except Exception as e:
    print("Кнопка пользователя не найдена на сайте. Ошибка:", str(e))


driver.quit()
