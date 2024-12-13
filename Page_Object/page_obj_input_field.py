class InputField:
    def __init__(self, web_driver, locator):
        self._web_driver = web_driver
        self._locator = locator

    def enter_text(self, text):
        """Ввод текста в поле."""
        field = WebDriverWait(self._web_driver, 10).until(
            EC.element_to_be_clickable(self._locator)
        )
        field.clear()
        field.send_keys(text)


class LoginPage(BasePage):
    def __init__(self, web_driver):
        super().__init__(web_driver, url="https://example.com/login")
        self.username_field = InputField(web_driver, (By.ID, "username"))
        self.password_field = InputField(web_driver, (By.ID, "password"))
        self.login_button = InputField(web_driver, (By.ID, "login"))

    def login(self, username, password):
        """Выполнить логин."""
        self.username_field.enter_text(username)
        self.password_field.enter_text(password)
        self.login_button.enter_text(Keys.RETURN)
