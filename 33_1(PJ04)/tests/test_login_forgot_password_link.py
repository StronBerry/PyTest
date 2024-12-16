import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_forgot_password_link(browser, logger):
    """
    Проверяет, что клик по ссылке "Забыл пароль" открывает страницу с правильным URL.
    """
    url = "https://b2c.passport.rt.ru/"
    logger.info(f"Открытие страницы: {url}")

    # Открываем страницу
    browser.get(url)

    # Локатор ссылки "Забыл пароль"
    forgot_password_locator = (By.ID, "forgot_password")

    # Убедиться, что ссылка присутствует
    try:
        forgot_password_link = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(forgot_password_locator)
        )
        logger.info("Ссылка 'Забыл пароль' найдена.")
    except TimeoutException:
        assert False, "Ссылка 'Забыл пароль' не найдена на странице."

    # Клик по ссылке
    logger.info("Кликаем по ссылке 'Забыл пароль'.")
    forgot_password_link.click()

    # Переход на новую страницу
    WebDriverWait(browser, 10).until(
        lambda driver: driver.current_url.startswith("https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials")
    )

    # Проверка URL новой страницы
    actual_url = browser.current_url
    expected_url_start = "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials"
    assert actual_url.startswith(expected_url_start), (
        f"Неверный URL. Ожидалось, что URL начнётся с '{expected_url_start}', найдено: '{actual_url}'"
    )
    logger.info(f"Ссылка открыла правильный URL: {actual_url}")
