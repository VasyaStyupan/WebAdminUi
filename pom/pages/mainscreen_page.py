import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pom.pages.logout_menu import LOGOUT_MENU
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

START_LOGOUT_MENU = "//*[text()=' Profile ']", "//*[text()=' Language ']", "//*[text()=' Logout ']"
START_MAIN_MENU = "//app-building-list-item/div[@class='table-list-item']"


class MainScreen:
    def __init__(self, driver, *search_word):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.5)
        self.word = search_word

    def search_bar(self):
        locator = "//input[@placeholder='Search users and units']"
        search = self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))
        search.send_keys(self.word)
        return search.send_keys(Keys.RETURN)

    def search_user(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='search-result-item']")

    def find_popup(self):
        xpath = LOGOUT_MENU
        return self.__wait.until(ec.presence_of_element_located((By.XPATH, xpath)))

    def press_sorting_button(self):
        locator = "//span[text()=' Building address ']"
        self.__wait.until(ec.presence_of_element_located((By.XPATH, locator))).click()

    def map_plus(self):
        locator = ".icon-app-plus"
        self.__wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, locator))).click()

    def map_minus(self):
        locator = ".icon-app-minus"
        self.__wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, locator))).click()

    def check_load_main_page(self):
        locator = "//div[@class='user-info-dropdown-mobile-button']"
        self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))
