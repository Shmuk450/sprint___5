from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    PERSONAL_ACCOUNT,
    PROFILE_EXIT_BUTTON,
    CONSTRUCTOR_LINK,
    HEADER_LOGO,
    TAB_BUNS,
    LOGIN_SUBMIT,
)
from tests.helpers import register_new_user, login


def login_fast(driver):
    """Быстрая авторизация: регистрируем нового юзера и логинимся."""
    email, password = register_new_user(driver)
    login(driver, email, password)


def test_go_to_personal_account(driver):
    """Переход в личный кабинет по клику «Личный Кабинет»."""
    login_fast(driver)
    driver.find_element(*PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(PROFILE_EXIT_BUTTON)
    )


def test_back_to_constructor_by_link_and_logo(driver):
    """
    Возврат из личного кабинета в конструктор:
    1) по ссылке «Конструктор»;
    2) по клику на логотип Stellar Burgers.
    """
    login_fast(driver)

    # Открыть ЛК
    driver.find_element(*PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(PROFILE_EXIT_BUTTON)
    )

    # Назад по ссылке «Конструктор»
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(CONSTRUCTOR_LINK)
    ).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(TAB_BUNS)
    )

    # Снова зайти в ЛК
    driver.find_element(*PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(PROFILE_EXIT_BUTTON)
    )

    # Назад по клику на логотип
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(HEADER_LOGO)
    ).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(TAB_BUNS)
    )


def test_logout_from_profile(driver):
    """Выход из аккаунта по кнопке «Выход» в ЛК."""
    login_fast(driver)
    driver.find_element(*PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(PROFILE_EXIT_BUTTON)
    )
    driver.find_element(*PROFILE_EXIT_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LOGIN_SUBMIT)
    )
    driver.quit()