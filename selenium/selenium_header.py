import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="session")
def selenium():
    # Создание экземпляра WebDriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
