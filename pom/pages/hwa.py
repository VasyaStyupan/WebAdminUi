import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from configuration import USERNAME_HA, PASSWORD_HA, HYPER_ADMIN_URL, USERNAME_BA


class Hwa:
    def __init__(self, driver, *username):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3)
        self.username = username

    def add_existing_user(self):
        locator = "//span[text()=' Add an existing user here ']"
        self.driver.find_elements(By.XPATH, locator)[0].click()
        locator = "//div[@class='existing-user-container visible']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        locator = "//div[@class='ng-input']/following::input[11]"
        search = self.driver.find_element(By.XPATH, locator)
        search.send_keys(USERNAME_BA)
        time.sleep(1)
        search.send_keys(Keys.RETURN)
        locator = "//button[text()=' Add ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def apartment_management(self):
        locator = "//div[text()=' Apartment management ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def building_address_ba(self):
        locator = "//span[@tabindex='0']"
        return self.driver.find_elements(By.XPATH, locator)

    def building_address_um(self):
        locator = "//div[@class='data-item-column__link']"
        return self.driver.find_elements(By.XPATH, locator)[0]

    def change_rfid_status(self):
        locator = "//span[text()='Disabled']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        element.click()

    def delete_rfid_hwa(self):
        locator = "//div[text()=' Delete ']//following::div[28]"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        locator = "//button[@class='delete-confirmation-delete-btn']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def delete_user_hwa(self):
        locator = "//button[text()=' Delete user ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        time.sleep(1)
        locator = "//button[@class='delete']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def find_by_uid(self):
        locator = "//input[@name='uid']"
        return self.driver.find_elements(By.XPATH, locator)

    def logout_hwa(self):
        locator = "//div[@class='admin_name']"
        self.driver.find_element(By.XPATH, locator).click()
        self.driver.find_element(By.CLASS_NAME, 'logout').click()

    def manage_customers(self):
        locator = "//div[text()='Manage customers']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def signin_hwa(self):
        self.driver.get(HYPER_ADMIN_URL)
        locator = "//input[@placeholder='Email']"
        user_name = self.driver.find_element(By.XPATH, locator)
        user_name.send_keys(USERNAME_HA)
        time.sleep(1)
        locator = "//input[@placeholder='Password']"
        password = self.driver.find_element(By.XPATH, locator)
        password.send_keys(PASSWORD_HA)
        locator = "//button[text()='Sign in']"
        self.driver.find_element(By.XPATH, locator).click()
        locator = "//input[@placeholder='Enter your code']"
        code = self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator)))
        code.send_keys("1111")
        locator = "//button[@class='btn form-btn']"
        self.driver.find_element(By.XPATH, locator).click()

    def search_hwa(self):
        locator = "//div[text()='Manage users']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()
        if self.username[0] == USERNAME_BA:
            locator = "//div[text()=' Admin management ']"
            self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        locator = "//input[@type='text']"
        search = self.driver.find_element(By.XPATH, locator)
        search.send_keys(self.username)
        time.sleep(2)
        locator = "//button[text()='Edit']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        element.click()
        time.sleep(1)

    def unit_uid(self):
        locator = "//div[@class='data-item-column__text']/following::div[6]"
        return self.driver.find_element(By.XPATH, locator)




