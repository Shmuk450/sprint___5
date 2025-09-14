from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from tests.helpers import register_new_user, login

def test_constructor_tabs_switch(driver):
    email, password = register_new_user(driver)
    login(driver, email, password)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TAB_BUNS))

    driver.find_element(*TAB_SAUCES).click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(ACTIVE_TAB, "Соусы"))

    driver.find_element(*TAB_FILLINGS).click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(ACTIVE_TAB, "Начинки"))

    driver.find_element(*TAB_BUNS).click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(ACTIVE_TAB, "Булки"))
    driver.quit()