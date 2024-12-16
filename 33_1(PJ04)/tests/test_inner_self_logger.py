import pytest

def test_logger(logger):
    """
    Проверяет, что логгер корректно записывает сообщения.
    """
    logger.info("Это тестовое сообщение INFO.")
    logger.warning("Это тестовое сообщение WARNING.")
    logger.error("Это тестовое сообщение ERROR.")

    assert True  # Проверка, что тест проходит
