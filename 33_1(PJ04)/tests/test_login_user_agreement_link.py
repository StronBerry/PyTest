import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_register_link(browser, logger):
    """
    Проверяет, что клик по ссылке "Зарегистрироваться" открывает страницу с правильным URL.
    """
    url = "https://b2c.passport.rt.ru/"
    logger.info(f"Открытие страницы: {url}")

    # Открываем страницу
    browser.get(url)

    # Локатор ссылки "Зарегистрироваться"
    register_link_locator = (By.ID, "kc-register")

    # Убедиться, что ссылка присутствует
    try:
        register_link = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(register_link_locator)
        )
        logger.info("Ссылка 'Зарегистрироваться' найдена.")
    except TimeoutException:
        assert False, "Ссылка 'Зарегистрироваться' не найдена на странице."

    # Клик по ссылке
    logger.info("Кликаем по ссылке 'Зарегистрироваться'.")
    register_link.click()

    # Проверяем URL новой страницы
    WebDriverWait(browser, 10).until(
        lambda driver: driver.current_url.startswith(
            "https://id-test.rt.ru/auth/realms/b2c/login-actions/registration"
        ) or driver.current_url.startswith(
            "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration"
        )
    )

    actual_url = browser.current_url
    expected_url_starts = [
        "https://id-test.rt.ru/auth/realms/b2c/login-actions/registration",
        "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration"
    ]
    assert any(actual_url.startswith(expected_url) for expected_url in expected_url_starts), (
        f"Неверный URL. Ожидалось, что URL начнётся с одного из {expected_url_starts}, найдено: '{actual_url}'"
    )
    logger.info(f"Ссылка открыла правильный URL: {actual_url}")
