import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_oidc_tinkoff_redirect(browser, logger):
    """
    Проверяет редирект на Tinkoff после клика на ссылку.
    """
    url = "https://b2c.passport.rt.ru/"
    logger.info(f"Открытие страницы: {url}")
    browser.get(url)

    link_locator = (By.ID, "oidc_tinkoff")

    # Нахождение и клик по ссылке
    link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(link_locator)
    )
    logger.info("Ссылка Tinkoff найдена.")
    link.click()

    # Проверка URL
    WebDriverWait(browser, 10).until(
        lambda driver: driver.current_url.startswith("https://id.tinkoff.ru/auth/")
    )
    actual_url = browser.current_url
    assert actual_url.startswith("https://id.tinkoff.ru/auth/"), (
        f"Неверный URL после редиректа. Найдено: {actual_url}"
    )
    logger.info(f"Редирект на Tinkoff успешно выполнен: {actual_url}")
