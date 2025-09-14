from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from tests.helpers import register_new_user, login

def test_login_from_main_button(driver):
    email, password = register_new_user(driver)
    # вход с главной по кнопке «Войти в аккаунт»
    driver.get(BASE_URL)
    driver.find_element(*LOGIN_BTN_ON_MAIN).click()
    login(driver, email, password)

def test_login_from_personal_account(driver):
    email, password = register_new_user(driver)
    driver.get(BASE_URL)
    driver.find_element(*PERSONAL_ACCOUNT).click()
    login(driver, email, password)

def test_login_from_register_form(driver):
    email, password = register_new_user(driver)
    login(driver, email, password)

def test_login_from_forgot_password_form(driver):
    email, password = register_new_user(driver)
    driver.get(BASE_URL)
    driver.find_element(*PERSONAL_ACCOUNT).click()
    driver.find_element(*FORGOT_PASSWORD_LINK).click()
    driver.find_element(*LOGIN_LINK).click()
    login(driver, email, password)
    driver.quit()