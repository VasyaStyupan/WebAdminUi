
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CodePage:
    def __init__(self, driver, code):
        self.driver = driver

    def search_code_field(self, code):
        search_field = self.driver.find_element(By.XPATH,
                                                "/html/body/app-root/app-auth-host/div[2]/app-auth-second-step/div/"
                                                "form/div[1]/div/input")
        search_field.send_keys(code)
        search_field = self.driver.find_element(By.TAG_NAME, "button")

        return search_field.send_keys(Keys.RETURN)
