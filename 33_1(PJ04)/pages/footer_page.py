from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class FooterPage(BasePage):
    """
    Класс для взаимодействия с подвалом страницы.
    """
    COPYRIGHT_TEXT = (By.CSS_SELECTOR, ".rt-footer-copyright")
    PRIVACY_POLICY_LINK = (By.XPATH,
        "//a[@class='rt-footer-agreement-link']//span[contains(text(), 'Политикой конфиденциальности')]"
    )


        # By.CSS_SELECTOR, "a.rt-footer-agreement-link[href='https://www.rt.ru/legal']")

    def get_copyright_text(self):
        """
        Возвращает текст элемента с авторскими правами.
        """
        return self.get_element_text(self.COPYRIGHT_TEXT)

    def click_privacy_policy_link(self):
        """
        Выполняет клик по ссылке "Политикой конфиденциальности".
        """
        self.click_element(self.PRIVACY_POLICY_LINK)

    COOKIES_BUTTON = (By.CSS_SELECTOR, "span#cookies-tip-open")
    COOKIES_TOOLTIP = (By.CSS_SELECTOR, "div.rt-tooltip")

    def click_cookies_button(self):
        """
        Кликает по кнопке "Cookies".
        """
        self.click_element(self.COOKIES_BUTTON)

    def is_cookies_tooltip_visible(self):
        """
        Проверяет, видим ли элемент всплывающей подсказки "Cookies".
        :return: True, если элемент отображается, иначе False.
        """
        return self.is_element_visible(self.COOKIES_TOOLTIP)

    SUPPORT_TEXT = (By.CSS_SELECTOR, "div.rt-footer-right.rt-footer-side-item")

    def get_support_text(self):
        """
        Возвращает текст элемента с информацией о службе поддержки.
        """
        return self.get_element_text(self.SUPPORT_TEXT)

    USER_AGREEMENT_LINK = (
        By.XPATH,
        "//a[@class='rt-footer-agreement-link']//span[contains(text(), 'Пользовательским соглашением')]"
    )

    def click_user_agreement_link(self, timeout=10):
        """
        Дожидается видимости ссылки "Пользовательским соглашением" и кликает по ней.
        Проверяет, что текст ссылки соответствует ожиданиям.
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.USER_AGREEMENT_LINK)
        )
        element.click()