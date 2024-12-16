import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_oidc_yandex_redirect(browser, logger):
    """
    Проверяет редирект на Yandex после клика на ссылку.
    Если за 3 секунды переход не произошёл, выполняется повторный клик.
    """
    url = "https://b2c.passport.rt.ru/"
    logger.info(f"Открытие страницы: {url}")
    browser.get(url)

    link_locator = (By.ID, "oidc_ya")

    # Нахождение ссылки
    link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(link_locator)
    )
    logger.info("Ссылка Yandex найдена.")

    # Клик по ссылке
    logger.info("Кликаем по ссылке Yandex.")
    link.click()

    # Ожидание перехода в течение 3 секунд
    time.sleep(3)
    current_url = browser.current_url

    # Если переход не произошёл, выполняется повторный клик
    if not current_url.startswith("https://oauth.yandex.ru"):
        logger.info("Переход не произошёл, выполняем повторный клик.")
        link.click()

    # Проверка URL
    WebDriverWait(browser, 10).until(
        lambda driver: driver.current_url.startswith("https://oauth.yandex.ru")
    )

    actual_url = browser.current_url
    assert actual_url.startswith("https://oauth.yandex.ru"), (
        f"Неверный URL после редиректа. Найдено: {actual_url}"
    )
    logger.info(f"Редирект на Yandex успешно выполнен: {actual_url}")
