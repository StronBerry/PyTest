from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """
    Базовый класс для всех страниц. Содержит общие методы для работы с элементами.
    """
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"Элемент {locator} не найден за {timeout} секунд.")
            raise

    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_present(self, locator, timeout=10):
        """
        Проверяет, присутствует ли элемент в DOM в течение указанного времени.
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def get_element_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text
