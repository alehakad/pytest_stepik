#import time
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_submit_button_lang(browser):
    browser.get(link)
    #time.sleep(10)
    submit_button = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert submit_button, 'submit button not found'