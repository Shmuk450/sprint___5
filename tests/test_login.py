from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from urls import BASE_URL
from helpers import register_new_user, login


class TestLogin:
    def test_login_from_main_button(self, driver):
        """Вход с главной страницы по кнопке 'Войти в аккаунт'"""
        email, password = register_new_user(driver)

        driver.get(BASE_URL)
        driver.find_element(*LOGIN_BTN_ON_MAIN).click()
        login(driver, email, password)

        # проверяем, что оказались в конструкторе (видна ссылка/кнопка «Конструктор» или активная область)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CONSTRUCTOR_LINK))
        assert driver.find_element(*CONSTRUCTOR_LINK).is_displayed()

    def test_login_from_personal_account(self, driver):
        """Вход через кнопку 'Личный кабинет' в хедере"""
        email, password = register_new_user(driver)

        driver.get(BASE_URL)
        driver.find_element(*PERSONAL_ACCOUNT).click()
        login(driver, email, password)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CONSTRUCTOR_LINK))
        assert driver.find_element(*CONSTRUCTOR_LINK).is_displayed()

    def test_login_from_register_form(self, driver):
        """Вход через форму регистрации (после регистрации мы на логине)"""
        email, password = register_new_user(driver)
        # мы уже на форме логина благодаря register_new_user
        login(driver, email, password)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CONSTRUCTOR_LINK))
        assert driver.find_element(*CONSTRUCTOR_LINK).is_displayed()

    def test_login_from_forgot_password_form(self, driver):
        """Вход через форму восстановления пароля → по ссылке 'Войти'"""
        email, password = register_new_user(driver)

        driver.get(BASE_URL)
        driver.find_element(*PERSONAL_ACCOUNT).click()
        driver.find_element(*FORGOT_PASSWORD_LINK).click()
        driver.find_element(*LOGIN_LINK).click()
        login(driver, email, password)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CONSTRUCTOR_LINK))
        assert driver.find_element(*CONSTRUCTOR_LINK).is_displayed()