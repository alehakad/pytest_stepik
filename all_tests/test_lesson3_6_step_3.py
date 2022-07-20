import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_answer(page):
    return math.log(int(time.time()+3600))


link = "http://selenium1py.pythonanywhere.com/"

pages = ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"] 

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('page', pages)
class TestMainPage1():
    answer = ''
    @pytest.mark.regression
    def test_alien_feedback(self,browser,page):
        browser.get(page)
        browser.implicitly_wait(10)
        textarea =browser.find_element(By.CSS_SELECTOR, ".textarea")
        ans = get_answer(page)
        print(ans)
        textarea.send_keys(str(ans))
        
        button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.submit-submission")))
        button.click()
        text = WebDriverWait(browser,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"p.smart-hints__hint"))).text
        if text!="Correct!":
           self.answer+=text
        assert text=="Correct!"

print(TestMainPage1.answer)
# вызов тестов с маркировкой
# pytest -s -v -m smoke test_fixture8.py
# регистрация меток в файле pytest.ini 
# @pytest.mark.skip - пропуск теста
# @pytest.mark.xfail(reason="fixing this bug right now") - если тест не должен проходить