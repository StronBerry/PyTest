import pytest
from pages.login_page import LoginPage

def test_tab_mail_placeholder(browser, logger):
    """
    Проверяет, что текст подсказки в поле ввода соответствует вкладке "Почта".
    """
    url = "https://b2c.passport.rt.ru/"
    logger.info(f"Открытие страницы: {url}")

    # Открываем страницу
    browser.get(url)

    # Работаем с формой авторизации
    login_page = LoginPage(browser)
    logger.info("Кликаем по вкладке 'Почта'.")

    # Кликаем по вкладке "Почта"
    login_page.click_tab(LoginPage.TAB_MAIL)

    # Проверяем текст подсказки
    actual_placeholder = login_page.get_input_placeholder_text()
    expected_placeholder = "Электронная почта"

    assert actual_placeholder == expected_placeholder, (
        f"Текст подсказки не соответствует ожиданиям. Ожидалось: '{expected_placeholder}', найдено: '{actual_placeholder}'"
    )
    logger.info(f"Текст подсказки соответствует ожиданиям: {actual_placeholder}")
