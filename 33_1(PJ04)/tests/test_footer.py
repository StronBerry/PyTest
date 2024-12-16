import pytest
from pages.footer_page import FooterPage


def test_footer_contains_copyright(browser, logger):
    """
    Проверяет, что подвал страницы содержит текст "© 2024 ПАО «Ростелеком». 18+".
    """
    url = "https://b2c.passport.rt.ru/"
    logger.info(f"Открытие страницы: {url}")

    # Открываем страницу
    browser.get(url)

    # Проверяем текст в подвале
    footer_page = FooterPage(browser)
    copyright_text = footer_page.get_copyright_text()

    expected_text = "© 2024 ПАО «Ростелеком». 18+"
    assert expected_text in copyright_text, (
        f"Текст подвала не соответствует ожиданиям. Найдено: '{copyright_text}'"
    )
    logger.info(f"Текст подвала успешно проверен: '{copyright_text}'")
