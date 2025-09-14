from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from helpers import register_new_user, login


class TestConstructorTabs:
    def test_constructor_tabs_switch(self, driver):
        # подготовка
        email, password = register_new_user(driver)
        login(driver, email, password)

        # по умолчанию должна быть видна секция конструктора и какая-то активная вкладка
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TAB_BUNS))
        # первоначально активной должна быть «Булки»
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(ACTIVE_TAB, "Булки"))
        assert driver.find_element(*ACTIVE_TAB).text == "Булки"

        # Соусы
        driver.find_element(*TAB_SAUCES).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(ACTIVE_TAB, "Соусы"))
        assert driver.find_element(*ACTIVE_TAB).text == "Соусы"

        # Начинки
        driver.find_element(*TAB_FILLINGS).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(ACTIVE_TAB, "Начинки"))
        assert driver.find_element(*ACTIVE_TAB).text == "Начинки"

        # обратно на Булки
        driver.find_element(*TAB_BUNS).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(ACTIVE_TAB, "Булки"))
        assert driver.find_element(*ACTIVE_TAB).text == "Булки"