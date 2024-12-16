import pytest
from pages.footer_page import FooterPage

def test_cookies_tooltip_displayed(browser, logger):
    """
    Проверяет, что клик по кнопке "Cookies" отображает всплывающую подсказку.
    """
    url = "https://b2c.passport.rt.ru/"
    logger.info(f"Открытие страницы: {url}")

    # Открываем страницу
    browser.get(url)

    # Работаем с подвалом
    footer_page = FooterPage(browser)

    # Клик по кнопке "Cookies"
    logger.info("Кликаем по кнопке 'Cookies'.")
    footer_page.click_cookies_button()

    # Проверяем отображение всплывающей подсказки
    assert footer_page.is_cookies_tooltip_visible(), "Всплывающая подсказка 'Cookies' не отображается!"
    logger.info("Всплывающая подсказка 'Cookies' успешно отображается.")
