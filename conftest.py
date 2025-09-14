import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    """Каждый тест автономен: отдельный браузер и корректное закрытие."""
    d = webdriver.Chrome()   
    d.maximize_window()
    yield d
    d.quit()