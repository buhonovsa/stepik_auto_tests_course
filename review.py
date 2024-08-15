from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    elements = []
    elements.append(browser.find_element(By.CSS_SELECTOR, "input.first:required"))
    elements.append(browser.find_element(By.CSS_SELECTOR, "input.second:required"))
    elements.append(browser.find_element(By.CSS_SELECTOR, "input.third:required"))
    for ele in elements:
        ele.send_keys("Текст")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(2)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

