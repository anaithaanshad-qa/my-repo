from selenium.common import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def enter_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def is_element_displayed(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def scroll_to_element(self, locator, max_swipes=5):
        for _ in range(max_swipes):
            try:
                element = self.driver.find_element(*locator)
                if element.is_displayed():
                    return element
            except:
                pass

            size = self.driver.get_window_size()
            start_y = size['height'] * 0.8
            end_y = size['height'] * 0.3
            start_x = size['width'] / 2

            self.driver.swipe(start_x, start_y, start_x, end_y, 500)

        raise Exception(f"Element {locator} not found after {max_swipes} swipes")