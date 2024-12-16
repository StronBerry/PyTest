import pytest
from fixtures.logger import logger
from fixtures.browser import browser  # Импорт фикстуры browser
import time
import logging
import os

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_call(item):
    """
    Хук для замера времени выполнения теста.
    """
    start_time = time.perf_counter()  # Засекаем точное время начала теста
    outcome = yield  # Выполняем тест
    end_time = time.perf_counter()  # Засекаем точное время окончания теста

    # Рассчитываем время выполнения и сохраняем как атрибут теста
    elapsed_time = end_time - start_time
    item.elapsed_time = elapsed_time  # Сохраняем время выполнения


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для записи результата теста в лог и сохранения снимка экрана при падении.
    """
    outcome = yield
    report = outcome.get_result()
    logger = logging.getLogger("test_logger")

    if report.when == "call":  # Проверяем, что тест завершён (этап выполнения)
        test_status = "PASS" if report.passed else "FAIL"

        # Получаем время выполнения из атрибута item
        elapsed_time = getattr(item, "elapsed_time", 0.0)

        logger.info(f"Результат теста '{item.name}': {test_status}")
        logger.info(f"Время выполнения: {elapsed_time:.2f} секунд")

        # Если тест провалился, делаем снимок экрана
        if report.failed:
            driver = item.funcargs.get("browser")
            if driver:
                screenshot_dir = "./screenshots"
                os.makedirs(screenshot_dir, exist_ok=True)  # Создаём папку, если её нет

                # Генерация имени файла
                timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
                test_name = item.name.replace("/", "_")
                screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")

                # Сохраняем снимок экрана
                driver.save_screenshot(screenshot_path)
                logger.info(f"Снимок экрана сохранён: {screenshot_path}")
