from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_cart_button_is_exist(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert button.is_displayed(), "The button doesn't exist"

