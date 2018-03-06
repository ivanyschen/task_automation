from selenium.webdriver.support.ui import WebDriverWait
# Elements represent DOM elements which can be manipulated.


class BasePageElement(object):
    """Base page class that is initialized on every page object class"""
    def __init__(self):


    def __set__(self, obj, value):
        driver - obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(self.locator))
        driver.find_element(self.locator).clear()
        driver.find_element(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(self.locator))
        element = driver.find_element(self.locator)
        return element.get_attribute("value")


class EmailInputElement(BasePageElement):
    def __init__(self):
        self.locator =
    pass


class PasswordInputElement(BasePageElement)
