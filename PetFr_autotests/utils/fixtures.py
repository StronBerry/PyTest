import pytest
from selenium import webdriver
import os
import csv
from datetime import datetime

@pytest.fixture(scope="session")
def selenium():
    """Фикстура для инициализации Selenium WebDriver."""
    driver = webdriver.Chrome()
    driver.set_window_size(1400, 1000)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def log():
    """Фикстура для создания лог-файла."""
    if not os.path.exists('LOG'):
        os.makedirs('LOG')
    log_file = "LOG/" + datetime.now().strftime("%d_%m_%y_%H_%M_%S") + ".csv"
    with open(log_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Step", "Result", "Description", "Duration (s)", "HTTP Status Code"])
    print(f"Log file created: {log_file}")
    return log_file
