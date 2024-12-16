import pytest
import requests

def test_page_status_code(logger):
    """
    Проверяет, что страница https://b2c.passport.rt.ru/ возвращает код 200.
    """
    url = "https://b2c.passport.rt.ru/"
    logger.info(f"Проверка статуса страницы: {url}")

    # Отправляем GET-запрос
    response = requests.get(url)

    # Проверяем, что код ответа 200
    assert response.status_code == 200, f"Страница {url} вернула код {response.status_code}, ожидался 200"
    logger.info(f"Страница {url} успешно открыта. Код ответа: {response.status_code}")
