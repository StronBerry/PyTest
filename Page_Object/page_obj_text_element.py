class TextElement:
    def __init__(self, web_driver, locator):
        self._web_driver = web_driver
        self._locator = locator

    def get_text(self):
        """Возвращает текст элемента."""
        element = WebDriverWait(self._web_driver, 10).until(
            EC.presence_of_element_located(self._locator)
        )
        return element.text


class NotificationPage(BasePage):
    def __init__(self, web_driver):
        super().__init__(web_driver, url="https://example.com/notifications")
        self.notification_message = TextElement(web_driver, (By.CLASS_NAME, "notification"))


page = NotificationPage(driver)
page.open()
message = page.notification_message.get_text()
assert "Success" in message, "Оповещение не содержит 'Success'"
