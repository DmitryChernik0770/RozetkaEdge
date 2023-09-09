import os
from selenium import webdriver
import time

# Путь к драйверу Edge WebDriver
edge_driver_path = r'D:\VSCode\Edge\msedgedriver.exe'

driver = webdriver.Edge(executable_path=edge_driver_path)

driver.get("https://rozetka.com.ua/")

time.sleep(2)

try:
    button = driver.find_element_by_xpath('//*[@class="header__button ng-tns-c60-1"]')
    print("Кнопка меню найдена.")
except Exception as e:
    print("Кнопка меню не найдена. Ошибка:", str(e))

driver.quit()
