from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    sum = int(num1) + int(num2)
    print(sum)
    select = Select(browser.find_element_by_css_selector("select"))
    select.select_by_value(str(sum))
    button = browser.find_element_by_css_selector('button[type=submit]')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
