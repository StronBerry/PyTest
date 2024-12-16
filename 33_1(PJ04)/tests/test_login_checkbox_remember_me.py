import pytest
from pages.login_page import LoginPage

def test_remember_me_checkbox(browser, logger):
    """
    Проверяет состояние чекбокса "Запомнить меня":
    1. Галочка установлена при загрузке страницы.
    2. Галочка пропадает при клике по чекбоксу.
    """
    url = "https://b2c.passport.rt.ru/"
    logger.info(f"Открытие страницы: {url}")

    # Открываем страницу
    browser.get(url)

    # Работаем с формой авторизации
    login_page = LoginPage(browser)

    # Проверяем, что галочка установлена при загрузке страницы
    assert login_page.is_remember_me_checked(), "Галочка 'Запомнить меня' не установлена при загрузке страницы."
    logger.info("Галочка 'Запомнить меня' установлена при загрузке страницы.")

    # Кликаем по чекбоксу
    login_page.click_remember_me_checkbox()
    logger.info("Клик по чекбоксу 'Запомнить меня'.")

    # Проверяем, что галочка пропала
    assert not login_page.is_remember_me_checked(), "Галочка 'Запомнить меня' не пропала после клика."
    logger.info("Галочка 'Запомнить меня' пропала после клика.")
