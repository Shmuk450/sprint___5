imimport pytest
from selenium import webdriver
from helpers import register_new_user, login


@pytest.fixture
def driver():
    """Каждый тест автономен: отдельный браузер и корректное закрытие."""
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()


@pytest.fixture
def login_fast(driver):
    """Регистрация и авторизация пользователя (фикстура для тестов)."""
    email, password = register_new_user(driver)
    login(driver, email, password)
    return email, password