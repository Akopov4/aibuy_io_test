from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class BasePage:

    def wait_until_element_is_present(self, locator: tuple, timeout: float, attempts: int = 3):
        for i in range(attempts):
            try:
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
                break
            except (TimeoutException, StaleElementReferenceException):
                raise NoSuchElementException(
                    f'Element "{locator}" not present in DOM after {timeout * attempts} seconds or it has been changed')

    def wait_until_element_is_visible(self, locator: tuple, timeout: float = 5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(f'Element "{locator}" not visible after {timeout} seconds')

    def find_element(self, locator: tuple, timeout: float = 5) -> WebElement:
        self.wait_until_element_is_present(locator, timeout)
        element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator))

        return element

    def find_elements(self, locator: tuple, timeout: float = 5, wait: bool = True) -> List[WebElement]:
        if wait:
            self.wait_until_element_is_present(locator, timeout)
        elements = self.driver.find_elements(*locator)
        return elements

    def get_text_of_element(self, element: WebElement):
        return element.text

    def click(self, locator: tuple):
        element = self.find_element(*locator)
        element.click()

    def is_element_visible(self, locator: tuple, timeout: float = 5) -> bool:
        try:
            self.wait_until_element_is_visible(locator, timeout=timeout)
        except NoSuchElementException:
            return False
        return True

    def get_parametrized_locator(self, locator: tuple, parameters: list):
        return locator[0], locator[1].format(*parameters)

    def get_css_property(self, locator: tuple, css_property: str):
        element = self.find_element(*locator)
        property_value = element.value_of_css_property(css_property)
        return property_value

    def is_dropdown_visible(self, locator:str) -> bool:
        self.is_element_visible(*locator)

    def get_text_from_drop_down(self, locator:tuple):
        items = self.find_elements(*locator)
        item_text = []
        for item in items:
            item_text.append(item.text)
        return item_text