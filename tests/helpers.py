from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from generators import gen_email, gen_password

def register_new_user(driver):
    """Регистрация нового пользователя и возврат email/пароля."""
    driver.get(BASE_URL)
    driver.find_element(*LOGIN_BTN_ON_MAIN).click()
    driver.find_element(*REGISTER_LINK).click()

    email = gen_email("sofia", "student", "1999")
    password = gen_password(8)

    driver.find_element(*REGISTER_NAME).send_keys("Софья")
    driver.find_element(*REGISTER_EMAIL).send_keys(email)
    driver.find_element(*REGISTER_PASSWORD).send_keys(password)
    driver.find_element(*REGISTER_SUBMIT).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LOGIN_SUBMIT))
    return email, password

def login(driver, email, password):
    driver.find_element(*LOGIN_EMAIL).send_keys(email)
    driver.find_element(*LOGIN_PASSWORD).send_keys(password)
    driver.find_element(*LOGIN_SUBMIT).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(CONSTRUCTOR_LINK))