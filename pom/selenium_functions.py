import time
from pom.pages.login_page import LoginPage
from pom.pages.code_page import CodePage
from pom.pages.mainscreen_page import MainScreen
from configuration import CODE_URL, MAIN_URL, LOGIN_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import allure


class Auth(LoginPage, CodePage):
    def __init__(self, driver, username, password, code, scenario):
        super().__init__(driver)
        self.driver = driver
        self.__wait = WebDriverWait(driver, 2, 0.3)
        self.username = username
        self.password = password
        self.scenario = scenario
        self.code = code

    def log_in(self):
        self.search_login_fields(self.username, self.password)
        try:
            self.__wait.until(EC.url_to_be(CODE_URL))
        except Exception:
            pass

        current_url = self.driver.current_url
        if self.scenario == 0:
            with allure.step("Step 1. Username and password entry"):
                assert CODE_URL == current_url, "Wrong username or password"
            self.search_code_field(self.code)
            self.__wait.until(EC.url_changes(CODE_URL))
            current_url = self.driver.current_url
            with allure.step("Step 2. Code entry"):
                assert MAIN_URL[:40] == current_url[:40], "Wrong Code"
        else:
            with allure.step("Step 1. Username and password entry"):
                assert LOGIN_URL == current_url, "Access error"
            return

    def hover_building(self):
        xpath = MainScreen(self.driver).search_building_address()
        xpath3 ="/html/body/app-root/app-building-host/main/app-unit-host/div/div[2]/app-unit-users-list/div/div/app-unit-users-list-item[3]/div/div[3]/span"
        xpath3 = self.driver.find_element(By.XPATH, xpath3)

        # xpath3 = self.driver.find_element(By.TAG_NAME, "app-unit-users-list-item")
        xpath2 = "/html/body/app-root/app-building-host/main/app-unit-host/div/div[2]/app-unit-users-list/div/div/app-unit-users-list-item[2]/div"
        xpath1 = self.driver.find_element(By.XPATH, xpath)
        xpath2 = self.driver.find_element(By.XPATH, xpath2)
        ActionChains(self.driver).move_to_element(xpath1).perform()
        ActionChains(self.driver).move_to_element(xpath2).perform()
        ActionChains(self.driver).move_to_element(xpath3).perform()

class Base(LoginPage):
    def __init__(self, driver, xpath):
        super().__init__(driver)
        self.driver = driver
        self.xpath = xpath
        self.xpath1 = xpath

    def select_popup_lang(self):
        LoginPage(self.driver).search_lang().click()
        hidden_menu = self.driver.find_element(By.XPATH, self.xpath)
        ActionChains(self.driver).move_to_element(hidden_menu).click(hidden_menu).perform()
        return self.driver.find_element(By.XPATH, self.xpath1)

    def popup_server(self):
        xpath1 = LoginPage(self.driver).set_server_US()
        LoginPage(self.driver).change_server_No_Us().click()
        hidden_menu = self.driver.find_element(By.XPATH, self.xpath)
        ActionChains(self.driver).move_to_element(hidden_menu).click(hidden_menu).perform()
        return self.driver.find_element(By.XPATH, xpath1)
