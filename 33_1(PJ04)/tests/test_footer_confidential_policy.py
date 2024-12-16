import pytest
from pages.footer_page import FooterPage

def test_privacy_policy_link_opens_new_tab(browser, logger):
    """
    Проверяет, что клик по ссылке "Политикой конфиденциальности" открывает новую вкладку с URL https://www.rt.ru/legal.
    """
    url = "https://b2c.passport.rt.ru/"
    logger.info(f"Открытие страницы: {url}")

    # Открываем страницу
    browser.get(url)

    # Работаем с подвалом
    footer_page = FooterPage(browser)
    logger.info("Кликаем по ссылке 'Политикой конфиденциальности'.")
    footer_page.click_privacy_policy_link()

    # Переходим на новую вкладку
    browser.switch_to.window(browser.window_handles[-1])

    # Проверяем URL новой вкладки
    expected_url = "https://www.rt.ru/legal"
    actual_url = browser.current_url
    assert actual_url == expected_url, (
        f"Неверный URL в новой вкладке. Ожидалось: {expected_url}, найдено: {actual_url}"
    )
    logger.info(f"Ссылка открыла правильный URL: {actual_url}")
