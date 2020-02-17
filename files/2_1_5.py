from selenium import webdriver
import time
import math


def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(y)
    checkbox_robot = browser.find_element_by_id('robotCheckbox')
    checkbox_robot.click()
    radio_robot = browser.find_element_by_id('robotsRule')
    radio_robot.click()
    button_submit = browser.find_element_by_css_selector('button[type=submit]')
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
