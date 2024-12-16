import pytest
from pages.footer_page import FooterPage

def test_user_agreement_link_opens_new_tab(browser, logger):
    """
    Проверяет, что клик по ссылке "Пользовательским соглашением" открывает новую вкладку с URL
    https://b2c.passport.rt.ru/sso-static/agreement/agreement.html или https://id-test.rt.ru/sso-static/agreement/agreement.html.
    """
    url = "https://b2c.passport.rt.ru/"
    logger.info(f"Открытие страницы: {url}")

    # Открываем страницу
    browser.get(url)

    # Работаем с подвалом
    footer_page = FooterPage(browser)
    logger.info("Кликаем по ссылке 'Пользовательским соглашением'.")
    footer_page.click_user_agreement_link()

    # Переходим на новую вкладку
    browser.switch_to.window(browser.window_handles[-1])

    # Проверяем URL новой вкладки
    expected_urls = [
        "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html",
        "https://id-test.rt.ru/sso-static/agreement/agreement.html"
    ]
    actual_url = browser.current_url

    assert actual_url in expected_urls, (
        f"Неверный URL в новой вкладке. Ожидалось один из: {expected_urls}, найдено: {actual_url}"
    )
    logger.info(f"Ссылка открыла правильный URL: {actual_url}")
