from selenium import webdriver
import time 

import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
# отправка файла
try:

    browser.get(link)

    # заполнение полей
    f_name_element = browser.find_element_by_name("firstname")
    f_name_element.send_keys("Tim")

    l_name_element = browser.find_element_by_name("lastname")
    l_name_element.send_keys("Brooks")

    email_element = browser.find_element_by_name("email")
    email_element.send_keys("myemail@gmail.com")

    # загрузка файла
    file_element = browser.find_element_by_css_selector("[type='file']")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.py')           # добавляем к этому пути имя файла 
    file_element.send_keys(file_path)
    
    # нажатие кнопки
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла