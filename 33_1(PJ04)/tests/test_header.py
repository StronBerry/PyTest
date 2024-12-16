import pytest
from pages.header_page import HeaderPage

def test_logo_visibility(browser, logger):
    """
    Тест проверяет наличие логотипа в хэдере страницы.
    """
    url = "https://b2c.passport.rt.ru"
    logger.info(f"Открытие сайта: {url}")

    # Открываем сайт
    browser.get(url)

    # Проверяем видимость логотипа
    header_page = HeaderPage(browser)
    assert header_page.is_logo_visible(), "Логотип не отображается!"
    logger.info("Логотип успешно отображается.")
