import pytest
from pages.footer_page import FooterPage

def test_footer_support_text(browser, logger):
    """
    Проверяет, что подвал содержит текст "Служба поддержки 8 800 100 0 800".
    """
    url = "https://b2c.passport.rt.ru/"
    logger.info(f"Открытие страницы: {url}")

    # Открываем страницу
    browser.get(url)

    # Работаем с подвалом
    footer_page = FooterPage(browser)
    support_text = footer_page.get_support_text()

    # Удаляем лишние пробелы и переносы строк из текста
    cleaned_support_text = support_text.replace("\n", " ").strip()

    # Ожидаемый текст
    expected_text = "Служба поддержки 8 800 100 0 800"

    assert expected_text in cleaned_support_text, (
        f"Текст службы поддержки в подвале не соответствует ожиданиям. Найдено: '{cleaned_support_text}'"
    )
    logger.info(f"Текст службы поддержки в подвале успешно проверен: '{cleaned_support_text}'")