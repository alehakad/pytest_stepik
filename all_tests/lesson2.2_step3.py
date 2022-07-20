from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 

import math



link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим числа
    x1 = browser.find_element_by_id("num1")
    x2 = browser.find_element_by_id("num2")

    # складываем числа
    res = str(int(x1.text)+int(x2.text))

    # находим список, выбираем нужный пункт
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(res)

    


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла