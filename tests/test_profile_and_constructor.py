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


class TestProfileAndConstructor:

    def test_go_to_personal_account(self, driver, login_fast):
        """Переход в личный кабинет по клику «Личный Кабинет»."""
        driver.find_element(*PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PROFILE_EXIT_BUTTON))
        assert driver.find_element(*PROFILE_EXIT_BUTTON).is_displayed()

    def test_back_to_constructor_by_link_and_logo(self, driver, login_fast):
        """Возврат из ЛК в Конструктор: по ссылке и по клику на логотип."""
        # по ссылке «Конструктор»
        driver.find_element(*PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PROFILE_EXIT_BUTTON))
        driver.find_element(*CONSTRUCTOR_LINK).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TAB_BUNS))
        assert driver.find_element(*TAB_BUNS).is_displayed()

        # по клику на логотип
        driver.find_element(*PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PROFILE_EXIT_BUTTON))
        driver.find_element(*HEADER_LOGO).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TAB_BUNS))
        assert driver.find_element(*TAB_BUNS).is_displayed()

    def test_logout_from_profile(self, driver, login_fast):
        """Выход из аккаунта из ЛК."""
        driver.find_element(*PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PROFILE_EXIT_BUTTON))
        driver.find_element(*PROFILE_EXIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_SUBMIT))
        assert driver.find_element(*LOGIN_SUBMIT).is_displayed()