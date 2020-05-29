from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, \
    TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

RETRY_COUNT = 3


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None) -> WebElement:
        try:
            return self.wait(timeout).until(
                EC.presence_of_element_located(locator))
        except TimeoutException:
            return None

    def click(self, locator, timeout=None):
        for i in range(RETRY_COUNT):
            try:
                self.find(locator)
                element = self.wait(timeout).until(
                    EC.element_to_be_clickable(locator))
                element.click()
                return

            except StaleElementReferenceException:
                if i < RETRY_COUNT - 1:
                    pass
        raise

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 7
        return WebDriverWait(self.driver, timeout=timeout)

    def input_data(self, data, locator):
        field = self.find(locator)
        self.click(locator)
        field.clear()
        field.send_keys(data)
