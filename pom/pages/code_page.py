
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CodePage:
    def __init__(self, driver):
        self.driver = driver

    def search_code_field(self, code):
        search_field = self.driver.find_element(By.XPATH,
                                                "//input[@placeholder='Enter your code']")
        search_field.send_keys(code)
        search_field = self.driver.find_element(By.TAG_NAME, "button")

        return search_field.send_keys(Keys.RETURN)
