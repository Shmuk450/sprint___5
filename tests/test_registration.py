from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from generators import gen_email, gen_password

def open_login(driver):
    driver.get(BASE_URL)
    driver.find_element(*LOGIN_BTN_ON_MAIN).click()

def go_to_register(driver):
    open_login(driver)
    driver.find_element(*REGISTER_LINK).click()

def test_success_registration(driver):
    """Успешная регистрация: имя не пустое, email валидный, пароль ≥ 6"""
    go_to_register(driver)

    driver.find_element(*REGISTER_NAME).send_keys("Софья")
    email = gen_email(first="sofia", last="student", cohort="1999")
    driver.find_element(*REGISTER_EMAIL).send_keys(email)
    pwd = gen_password(8)
    driver.find_element(*REGISTER_PASSWORD).send_keys(pwd)
    driver.find_element(*REGISTER_SUBMIT).click()

    # После успешной регистрации должна открыться форма логина (кнопка Войти видна)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LOGIN_SUBMIT))

def test_registration_password_error(driver):
    """Ошибка для некорректного (короткого) пароля"""
    go_to_register(driver)

    driver.find_element(*REGISTER_NAME).send_keys("Софья")
    driver.find_element(*REGISTER_EMAIL).send_keys(gen_email("sofia", "student", "1999"))
    driver.find_element(*REGISTER_PASSWORD).send_keys("12345")   # 5 символов
    driver.find_element(*REGISTER_SUBMIT).click()

    # Отображается текст ошибки под полем
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(REGISTER_ERROR))
    
    driver.quit()