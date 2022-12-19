from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CodePage:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3)

    def search_code_field(self, code):
        search_field = self.__wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                           "//input[@placeholder='Enter your code']")))
        search_field.send_keys(code)
        search_field = self.__wait.until(ec.visibility_of_element_located((By.TAG_NAME, "button")))

        return search_field.send_keys(Keys.RETURN)
