class VisibilityChecker:
    def __init__(self, web_driver, locator):
        self._web_driver = web_driver
        self._locator = locator

    def is_visible(self):
        """Проверяет, виден ли элемент."""
        try:
            element = WebDriverWait(self._web_driver, 10).until(
                EC.visibility_of_element_located(self._locator)
            )
            return element.is_displayed()
        except:
            return False


class DashboardPage(BasePage):
    def __init__(self, web_driver):
        super().__init__(web_driver, url="https://example.com/dashboard")
        self.logout_button = VisibilityChecker(web_driver, (By.ID, "logout"))

    def is_logged_in(self):
        """Проверяет, вошел ли пользователь."""
        return self.logout_button.is_visible()


dashboard = DashboardPage(driver)
dashboard.open()
assert dashboard.is_logged_in(), "Пользователь не вошел"
