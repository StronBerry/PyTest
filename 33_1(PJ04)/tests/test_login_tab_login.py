import pytest
from pages.login_page import LoginPage

def test_tab_login_placeholder(browser, logger):
    """
    Проверяет, что текст подсказки в поле ввода соответствует вкладке "Логин".
    """
    url = "https://b2c.passport.rt.ru/"
    logger.info(f"Открытие страницы: {url}")

    # Открываем страницу
    browser.get(url)

    # Работаем с формой авторизации
    login_page = LoginPage(browser)
    logger.info("Кликаем по вкладке 'Логин'.")

    # Кликаем по вкладке "Логин"
    login_page.click_tab(LoginPage.TAB_LOGIN)

    # Проверяем текст подсказки
    actual_placeholder = login_page.get_input_placeholder_text()
    expected_placeholder = "Логин"

    assert actual_placeholder == expected_placeholder, (
        f"Текст подсказки не соответствует ожиданиям. Ожидалось: '{expected_placeholder}', найдено: '{actual_placeholder}'"
    )
    logger.info(f"Текст подсказки соответствует ожиданиям: {actual_placeholder}")
