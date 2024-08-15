import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)
s = str(math.ceil(math.pow(math.pi, math.e)*10000))
#224592
link_s = browser.find_element(By.PARTIAL_LINK_TEXT, s)
link_s.click()

try:
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Pet")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Orel")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Rus")
    #button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
