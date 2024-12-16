import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_oidc_ok_redirect(browser, logger):
    """
    Проверяет редирект на OK.ru после клика на ссылку.
    """
    url = "https://b2c.passport.rt.ru/"
    logger.info(f"Открытие страницы: {url}")
    browser.get(url)

    link_locator = (By.ID, "oidc_ok")

    # Нахождение и клик по ссылке
    link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(link_locator)
    )
    logger.info("Ссылка OK.ru найдена.")
    link.click()

    # Проверка URL
    WebDriverWait(browser, 10).until(
        lambda driver: driver.current_url.startswith("https://connect.ok.ru/")
    )
    actual_url = browser.current_url
    assert actual_url.startswith("https://connect.ok.ru/"), (
        f"Неверный URL после редиректа. Найдено: {actual_url}"
    )
    logger.info(f"Редирект на OK.ru успешно выполнен: {actual_url}")
