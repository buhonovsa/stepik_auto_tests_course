from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("I")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("P")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("IP")
    file1 = browser.find_element(By.ID, "file")
    curent_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(curent_dir, 'test.txt')
    file1.send_keys(file_path)
    
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
