import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from configuration import USERNAME_HA, PASSWORD_HA, CODE


class Units:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3)

    def doorbell_tab(self):
        locator = "//div[@routerlink='doorbells']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def doorbell(self):
        locator = "//div[@class='table-list-item__coll']"
        return self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator))).click()

    def press_icon(self):
        locator = "//div[@class='image-label']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def load_image(self):
        locator = "//input[@accept='image/jpeg']"
        return self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))

    def save_image(self):
        locator = "//button[text()='Save']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def delete_img(self):
        locator = "//button[@class='image-preview__remove-btn']"
        return self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))

    def access(self):
        locator = "//div[text()=' Access ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def never_allow(self):
        locator = "//div[text()=' Never allow ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def use_schedule(self):
        locator = "//div[text()=' Use the schedule defined for this building ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def make_schedule(self):
        locator = "//div[text()=' Make your schedule ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def select_building(self):
        locator = "//div[@class='table-list-item__coll']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def settings(self):
        locator = "//div[@routerlink='settings']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def change_unit_name(self):
        locator = "//div[text()=' Change unit name ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def change_unit_manager(self):
        locator = "//div[text()=' Add the role of unit manager to another user ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def select_unit(self):
        locator = "//div[@class='table-list-item__coll']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def add_user(self):
        locator = "//button[@routerlink='user/create']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def fill_user_data(self):
        locator = "//input[@placeholder='Email']"
        email_field = self.driver.find_element(By.XPATH, locator)
        email_field.send_keys("JohnDoe@mail.com")
        locator = "//div[@class='form-select-input-holder main-color']"
        self.driver.find_element(By.XPATH, locator).click()
        locator = "//span[text()='+47']"
        self.driver.find_element(By.XPATH, locator).click()
        locator = "//input[@placeholder='Phone']"
        email_field = self.driver.find_element(By.XPATH, locator)
        email_field.send_keys("0123456789")
        locator = "//input[@placeholder='First name']"
        email_field = self.driver.find_element(By.XPATH, locator)
        email_field.send_keys("John")
        locator = "//input[@placeholder='Last name']"
        email_field = self.driver.find_element(By.XPATH, locator)
        email_field.send_keys("Doe")
        locator = "//div[text()=' Make this user a unit manager ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        locator = "//button[@class='add-user-save-btn']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def signin_hwa(self):
        locator = "//input[@placeholder='Email']"
        user_name = self.driver.find_element(By.XPATH, locator)
        user_name.send_keys(USERNAME_HA)
        locator = "//input[@placeholder='Password']"
        password = self.driver.find_element(By.XPATH, locator)
        password.send_keys(PASSWORD_HA)
        locator = "//button[text()='Sign in']"
        self.driver.find_element(By.XPATH, locator).click()
        locator = "//input[@placeholder='Enter your code']"
        code = self.driver.find_element(By.XPATH, locator)
        code.send_keys("1111")

    def delete_user_hwa(self):
        locator = "//button[@class='btn form-btn']"
        self.driver.find_element(By.XPATH, locator).click()
        locator = "//div[text()='Manage users']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        locator = "//input[@type='text']"
        search = self.driver.find_element(By.XPATH, locator)
        search.send_keys("JohnDoe@mail.com")
        locator = "//button[text()='Edit']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        locator = "//button[text()=' Delete user ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        locator = "//button[@class='delete']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()


