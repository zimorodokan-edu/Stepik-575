from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_id("book")
    button.click()

    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(y)
    button_submit = browser.find_element_by_css_selector('button[type=submit]')
    button_submit.click()
finally:
    time.sleep(10)
    browser.quit()
