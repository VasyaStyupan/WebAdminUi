import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from configuration import USERNAME_BA, PASSWORD_BA, CODE


class Buildings:
    def __init__(self, driver, *word):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3)

    def settings_tab(self):
        locator = "//div[text()=' Settings ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def unit_manager_functions(self):
        locator = "//div[text()=' Add a user ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        time.sleep(1)
        locator = "//div[text()=' Change unit name ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        time.sleep(1)
        locator = "//div[text()=' Add the role of unit manager to another user ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        time.sleep(1)
        locator = "//div[text()=' Administrate users RFID cards ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
