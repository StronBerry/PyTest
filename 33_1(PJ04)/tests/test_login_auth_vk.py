import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_oidc_vk_redirect(browser, logger):
    """
    Проверяет редирект на VK после клика на ссылку.
    """
    url = "https://b2c.passport.rt.ru/"
    logger.info(f"Открытие страницы: {url}")
    browser.get(url)

    link_locator = (By.ID, "oidc_vk")

    # Нахождение и клик по ссылке
    link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(link_locator)
    )
    logger.info("Ссылка VK найдена.")
    link.click()

    # Проверка URL
    WebDriverWait(browser, 10).until(
        lambda driver: driver.current_url.startswith("https://id.vk.com/auth")
    )
    actual_url = browser.current_url
    assert actual_url.startswith("https://id.vk.com/auth"), (
        f"Неверный URL после редиректа. Найдено: {actual_url}"
    )
    logger.info(f"Редирект на VK успешно выполнен: {actual_url}")
