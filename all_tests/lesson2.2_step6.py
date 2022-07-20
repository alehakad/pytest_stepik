from selenium import webdriver
import time 

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    


    input1 = browser.find_element_by_id("answer")
    # проскроллить страницу вниз, так как футер перекрывает элемент

    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(str(y))
    
    checkbox1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox1.click()

    radiobutton1 = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobutton1.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла