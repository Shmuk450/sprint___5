from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from urls import BASE_URL
from generators import gen_email, gen_password
from data import FIRST_NAME, EMAIL_FIRST, EMAIL_LAST, EMAIL_COHORT, PASSWORD_LEN


class TestRegistration:
    def test_success_registration(self, driver):
        """Успешная регистрация: имя не пустое, email валидный, пароль ≥ 6."""
        # Открыть форму регистрации
        driver.get(BASE_URL)
        driver.find_element(*LOGIN_BTN_ON_MAIN).click()
        driver.find_element(*REGISTER_LINK).click()

        # Заполнить поля
        driver.find_element(*REGISTER_NAME).send_keys(FIRST_NAME)
        email = gen_email(EMAIL_FIRST, EMAIL_LAST, EMAIL_COHORT)
        driver.find_element(*REGISTER_EMAIL).send_keys(email)
        pwd = gen_password(PASSWORD_LEN)
        driver.find_element(*REGISTER_PASSWORD).send_keys(pwd)
        driver.find_element(*REGISTER_SUBMIT).click()

        # Ожидание и проверка, что открылась форма логина
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LOGIN_SUBMIT))
        assert driver.find_element(*LOGIN_SUBMIT).is_displayed()

    def test_registration_password_error(self, driver):
        """Ошибка при коротком пароле (< 6)."""
        # Открыть форму регистрации
        driver.get(BASE_URL)
        driver.find_element(*LOGIN_BTN_ON_MAIN).click()
        driver.find_element(*REGISTER_LINK).click()

        # Заполнить поля с коротким паролем
        driver.find_element(*REGISTER_NAME).send_keys(FIRST_NAME)
        bad_email = gen_email(EMAIL_FIRST, EMAIL_LAST, EMAIL_COHORT)
        driver.find_element(*REGISTER_EMAIL).send_keys(bad_email)
        driver.find_element(*REGISTER_PASSWORD).send_keys("12345")  # 5 символов
        driver.find_element(*REGISTER_SUBMIT).click()

        # Ожидание и проверка текста ошибки
        err = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(REGISTER_ERROR))
        assert err.is_displayed()