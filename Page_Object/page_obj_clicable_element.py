class ClickableElement:
    def __init__(self, web_driver, locator):
        self._web_driver = web_driver
        self._locator = locator

    def click(self):
        """Ждет и кликает по элементу."""
        element = WebDriverWait(self._web_driver, 10).until(
            EC.element_to_be_clickable(self._locator)
        )
        element.click()


class ProfilePage(BasePage):
    def __init__(self, web_driver):
        super().__init__(web_driver, url="https://example.com/profile")
        self.edit_button = ClickableElement(web_driver, (By.ID, "edit-profile"))


profile = ProfilePage(driver)
profile.open()
profile.edit_button.click()
