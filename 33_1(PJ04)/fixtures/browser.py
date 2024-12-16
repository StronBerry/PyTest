import pytest
from selenium import webdriver
from datetime import datetime
import os

@pytest.fixture(scope="function")
def browser(request):
    """
    Фикстура для настройки браузера.
    Закрывает браузер после завершения теста.
    Создает скриншот при падении теста.
    """
    driver = webdriver.Chrome()  # Убедитесь, что chromedriver установлен
    driver.maximize_window()

    # Действия после теста
    yield driver

    # Проверяем, упал ли тест
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        # Создаем папку для скриншотов, если её нет
        screenshots_dir = "./screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

        # Генерируем имя файла для скриншота
        test_name = request.node.name
        timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")

        # Сохраняем скриншот
        driver.save_screenshot(screenshot_path)
        print(f"Скриншот сохранен: {screenshot_path}")

    driver.quit()


# Хук для записи результатов теста
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для передачи результата выполнения теста в фикстуры.
    """
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
