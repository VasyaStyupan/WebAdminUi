
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

START_LOGOUT_MENU = "//*[text()=' Profile ']", "//*[text()=' Language ']", "//*[text()=' Logout ']"
START_MAIN_MENU = "//app-building-list-item"
BUILDING_ADDRESS_TAG = "//span[text()=' Building address ']"


class MainScreen:
    def __init__(self, driver, *search_word):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 10, 0.3)
        self.word = search_word

    def search_bar(self):
        locator = "//input[@placeholder='Search users and units']"
        search = self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))
        search.send_keys(self.word)
        return search.send_keys(Keys.RETURN)

    def search_user(self):
        return self.__wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                   "//div[@class='search-result-item']")))

    def press_sorting_button(self):
        locator = "//span[text()=' Building address ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def map_plus(self):
        locator = ".icon-app-plus"
        return self.__wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, locator)))

    def map_minus(self):
        locator = ".icon-app-minus"
        return self.__wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, locator)))

    def check_load_main_page(self):
        locator = "//div[@class='user-info-dropdown-mobile-button']"
        self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))
