from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

def summa(x1,x2):
    return str(x1+x2)

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    x1_element = browser.find_element(By.ID, "num1")
    x2_element = browser.find_element(By.ID, "num2")
    x1 = x1_element.text
    x2 = x2_element.text
    x = str(int(x1)+int(x2))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(x))
    
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
