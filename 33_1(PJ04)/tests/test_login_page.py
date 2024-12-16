import pytest
from pages.login_page import LoginPage

def test_login_form_is_present(browser, logger):
    """
    Проверяет, что элемент с классом "card-container login-form-container login-form-container" находится на странице.
    """
    url = "https://b2c.passport.rt.ru/"
    logger.info(f"Открытие страницы: {url}")

    # Открываем страницу
    browser.get(url)

    # Проверяем наличие элемента
    login_page = LoginPage(browser)
    assert login_page.is_login_form_present(), (
        "Элемент с классом 'card-container login-form-container login-form-container' отсутствует на странице."
    )
    logger.info("Элемент с классом 'card-container login-form-container login-form-container' успешно найден.")
