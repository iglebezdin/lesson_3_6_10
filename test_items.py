import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# Функция для проверки наличия элемента на странице
def is_element_present(browser, how, what):
    try:
        browser.find_element(how, what)
    except NoSuchElementException:
        return False
    return True


def test_button_add_in_basket_is_present(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    assert is_element_present(browser, By.XPATH, '//form[@id="add_to_basket_form"]/button'), \
        'Button "Add in basket" is not present'
