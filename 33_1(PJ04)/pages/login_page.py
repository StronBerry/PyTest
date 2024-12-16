from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """
    Класс для работы с формой авторизации.
    """
    # Локаторы вкладок
    TAB_PHONE = (By.ID, "t-btn-tab-phone")
    TAB_MAIL = (By.ID, "t-btn-tab-mail")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")
    TAB_LS = (By.ID, "t-btn-tab-ls")

    # Локатор текста подсказки в поле ввода
    INPUT_PLACEHOLDER = (By.CSS_SELECTOR, ".rt-input__placeholder")

    def click_tab(self, tab_locator):
        """
        Кликает по указанной вкладке.
        """
        self.click_element(tab_locator)

    def get_input_placeholder_text(self):
        """
        Возвращает текст подсказки из поля ввода.
        """
        return self.get_element_text(self.INPUT_PLACEHOLDER)

    # Локаторы для чекбокса "Запомнить меня"
    REMEMBER_ME_CHECKBOX = (By.CSS_SELECTOR, ".rt-checkbox")
    REMEMBER_ME_CHECKBOX_CHECKED = (By.CSS_SELECTOR, ".rt-checkbox--checked")

    def is_remember_me_checked(self):
        """
        Проверяет, установлена ли галочка в поле "Запомнить меня".
        :return: True, если галочка установлена, иначе False.
        """
        return self.is_element_present(self.REMEMBER_ME_CHECKBOX_CHECKED)

    def click_remember_me_checkbox(self):
        """
        Кликает по чекбоксу "Запомнить меня".
        """
        self.click_element(self.REMEMBER_ME_CHECKBOX)