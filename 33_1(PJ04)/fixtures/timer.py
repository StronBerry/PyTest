import pytest
import time

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_protocol(item):
    """
    Хук для замера времени выполнения теста.
    """
    start_time = time.time()
    outcome = yield
    end_time = time.time()

    # Сохраняем время выполнения как атрибут теста
    item.elapsed_time = end_time - start_time
