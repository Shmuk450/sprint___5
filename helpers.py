from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from urls import BASE_URL
from generators import gen_email, gen_password
from data import FIRST_NAME, EMAIL_FIRST, EMAIL_LAST, EMAIL_COHORT, PASSWORD_LEN


def register_new_user(driver):
    """Регистрация нового пользователя и возврат email/пароля."""
    driver.get(BASE_URL)
    driver.find_element(*LOGIN_BTN_ON_MAIN).click()
    driver.find_element(*REGISTER_LINK).click()

    email = gen_email(EMAIL_FIRST, EMAIL_LAST, EMAIL_COHORT)
    password = gen_password(PASSWORD_LEN)

    driver.find_element(*REGISTER_NAME).send_keys(FIRST_NAME)
    driver.find_element(*REGISTER_EMAIL).send_keys(email)
    driver.find_element(*REGISTER_PASSWORD).send_keys(password)
    driver.find_element(*REGISTER_SUBMIT).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LOGIN_SUBMIT))
    return email, password


def login(driver, email, password):
    """Авторизация по email и паролю."""
    driver.find_element(*LOGIN_EMAIL).send_keys(email)
    driver.find_element(*LOGIN_PASSWORD).send_keys(password)
    driver.find_element(*LOGIN_SUBMIT).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(CONSTRUCTOR_LINK))