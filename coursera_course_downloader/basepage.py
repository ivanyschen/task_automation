from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver, page_url):
        self.driver = driver
        self.page_url = page_url
        self.open()

    def open(self):
        self.driver.get(self.page_url)

    def find_element(self, *locator):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(locator))
        return element

    def find_elements(self, *locator):
        elements = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(locator))
        return elements