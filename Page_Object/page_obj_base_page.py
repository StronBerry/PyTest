class BasePage:
    def __init__(self, web_driver, url=''):
        self._web_driver = web_driver
        self._url = url

    def open(self):
        """Открывает страницу по URL."""
        if self._url:
            self._web_driver.get(self._url)

    def get_title(self):
        """Возвращает заголовок страницы."""
        return self._web_driver.title


# Тест
class HomePage(BasePage):
    def __init__(self, web_driver):
        super().__init__(web_driver, url="https://example.com")


page = HomePage(driver)
page.open()
assert "Example" in page.get_title(), "Заголовок не содержит 'Example'"
