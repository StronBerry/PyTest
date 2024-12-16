import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_button(browser, logger):
    """
    Проверяет вход с корректными данными и переход на страницу с ожидаемым URL.
    """
    url = "https://b2c.passport.rt.ru/"
    logger.info(f"Открытие страницы: {url}")

    # Открываем страницу
    browser.get(url)

    # Локаторы
    email_locator = (By.ID, "username")
    password_locator = (By.ID, "password")
    login_button_locator = (By.ID, "kc-login")

    # Ввод e-mail
    logger.info("Вводим e-mail: testdata@internet.ru")
    email_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(email_locator)
    )
    email_field.send_keys("testdata@internet.ru")

    # Ввод пароля
    logger.info("Вводим пароль.")
    password_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(password_locator)
    )
    password_field.send_keys("TestData2024")

    # Клик по кнопке "Войти"
    logger.info("Кликаем по кнопке 'Войти'.")
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(login_button_locator)
    )
    login_button.click()

    # Проверяем URL после входа
    WebDriverWait(browser, 10).until(
        lambda driver: driver.current_url.startswith("https://b2c.passport.rt.ru/account_b2c/page")
    )

    actual_url = browser.current_url
    expected_url_start = "https://b2c.passport.rt.ru/account_b2c/page"
    assert actual_url.startswith(expected_url_start), (
        f"Неверный URL после входа. Ожидалось, что URL начнётся с '{expected_url_start}', найдено: '{actual_url}'"
    )
    logger.info(f"Успешный вход. Перешли на страницу: {actual_url}")
