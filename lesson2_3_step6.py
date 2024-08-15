from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    #browser.execute_script("return.arguments[0].scrollIntoView(true);", button)
    button.click()
    first_win = browser.window_handles[0]
    new_win = browser.window_handles[1]
    browser.switch_to.window(new_win)
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button1 = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
