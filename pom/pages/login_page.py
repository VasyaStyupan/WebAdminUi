from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

SELECT_SERVER_US = "//div[text()='US']"
CHANGE_LANG_TO_NORSK = "//div[text()='Norsk']"
CHANGE_LANG_TO_SVENSKA = "//div[text()='Svenska']"
CHANGE_LANG_TO_ENGLISH = "//div[text()='English']"


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3)

    def search_login_field(self, username):
        locator = "//*[@placeholder='Username']"
        return self.driver.find_element(By.XPATH, locator).send_keys(username)

    def search_password_field(self, password):
        locator = "//*[@placeholder='Password']"
        search_field = self.driver.find_element(By.XPATH, locator)
        search_field.send_keys(password)
        return search_field.send_keys(Keys.RETURN)

    def search_privacy(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Privacy, ']")

    def search_privacy_nor(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Personvern, ']")

    def search_terms(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Terms of use ']")

    def search_terms_nor(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Vilkår ']")

    def search_contact(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Contact us']")

    def search_contact_nor(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Kontakt oss']")

    def change_server_No_Us(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Europe']")

    def search_lang(self):
        return self.driver.find_element(By.XPATH, "//i[@class='icon-app-down-open']")
