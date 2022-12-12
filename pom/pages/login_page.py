from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

SELECT_SERVER_US = "//div[text()='US']"
SELECT_SERVER_EU = "//div[text()='Europe']"
CHANGE_LANG_TO_NORSK = "//div[text()='Norsk']"
CHANGE_LANG_TO_SVENSKA = "//div[text()='Svenska']"
CHANGE_LANG_TO_ENGLISH = "//div[text()='English']"
CHANGE_LANG_TO_DEUTSCH = "//div[text()='Deutsch']"


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3)

    def search_contact(self):
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Contact us']")))

    def search_contact_nor(self):
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Kontakt oss']")))

    def change_server_No_Us(self):
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, "//span[text()='Europe']")))

    def change_server_Us_No(self):
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, "//span[text()='US']")))

    def search_login_field(self, username):
        locator = "//*[@placeholder='Username']"
        self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator))).send_keys(username)

    def search_password_field(self, password):
        locator = "//*[@placeholder='Password']"
        search_field = self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator)))
        search_field.send_keys(password)
        return search_field.send_keys(Keys.RETURN)

    def search_privacy(self):
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()=' Privacy, ']")))

    def search_privacy_nor(self):
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()=' Personvern, ']")))

    def search_terms(self):
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()=' Terms of use ']")))

    def search_terms_nor(self):
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()=' Vilkår ']")))

    def search_lang(self):
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, "//i[@class='icon-app-down-open']")))
