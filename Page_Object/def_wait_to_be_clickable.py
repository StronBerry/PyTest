class MyElement:
    def __init__(self, web_driver, locator):
        self._web_driver = web_driver
        self._locator = locator

    def wait_to_be_clickable(self):
        return WebDriverWait(self._web_driver, 10).until(
            EC.element_to_be_clickable(self._locator)
        )

# В тесте:
element = MyElement(driver, (By.ID, 'submit-button'))
element.click(hold_seconds=1, x_offset=5, y_offset=5)
