from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_submit = browser.find_element_by_css_selector('button[type=submit]')
    button_submit.click()
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(y)
    button_submit = browser.find_element_by_css_selector('button[type=submit]')
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
