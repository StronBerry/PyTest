from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HeaderPage(BasePage):
    """
    Класс для работы с хэдером страницы.
    """
    LOGO = (By.CSS_SELECTOR, ".main-header__logo-container .rt-logo")

    def is_logo_visible(self):
        """
        Проверяет, отображается ли логотип.
        """
        return self.is_element_visible(self.LOGO)
