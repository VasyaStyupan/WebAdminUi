import time
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from configuration import USERNAME_BA, SIMPLE_USER, UID, BUILDING, server


class Units:
    def __init__(self, driver, *word):
        self.driver = driver
        self.word = word
        self.__wait = WebDriverWait(driver, 5, 0.3)

    def accept_delete(self):
        locator = "//button[text()='Delete']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def access(self):
        locator = "//div[text()=' Access ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def always_allow(self):
        locator = "//div[@class='form-radio__label']/following::label[1]"
        return self.driver.find_element(By.XPATH, locator).click()

    def add_user(self):
        locator = "//button[@routerlink='user/create']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()

    def check_button_visibility(self):
        locator = "//div[text()=' Enable ']"
        self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator))).click()
        time.sleep(1)
        locator = "//div[text()=' Disable ']"
        return self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator))).click()

    def check_image_visibility(self):
        locator = "//div[@class='image-label__image']"
        return self.driver.find_element(By.XPATH, locator)

    def check_button_layouts(self):
        locator = "//div[text()=' Hidden ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()
        locator = "//div[text()=' Visible ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()
        locator = "//div[text()=' Hidden ']//following::div[6]"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()
        locator = "//div[text()=' Visible ']/following::div[6]"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()

    def choose_delete(self):
        locator = "//div[@class='image-label__image'] "
        return self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))

    def change_unit_name(self):
        unit = self.word
        locator = "//button[text()=' Edit Info ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        time.sleep(1)
        locator = "//input[@placeholder='Enter name']"
        unit_name = self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator)))
        unit_name.clear()
        unit_name.send_keys(unit)
        time.sleep(1)
        locator = "//button[text()=' Save ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def change_unit_owner_button(self):
        locator = "//button[text()=' Change unit owner ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def change_unit_owner(self):
        username = self.word[0]
        self.change_unit_owner_button()
        locator = f"//span[text()='{username}']/parent::div/parent::div/child::div[1]"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        locator = f"//span[text()='{username}']/parent::div/parent::div/child::div[5]"
        first_name = self.driver.find_element(By.XPATH, locator).text
        locator = f"//span[text()='{username}']/parent::div/parent::div/child::div[6]"
        last_name = self.driver.find_element(By.XPATH, locator).text
        locator = "//button[@class='save-btn']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        return first_name, last_name

    def change_unit_manager(self):
        locator = "//div[text()=' Add the role of unit manager to another user ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def doorbell_tab(self):
        locator = "//div[@routerlink='doorbells']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()

    def doorbell(self):
        locator = "//div[@class='table-list-item__coll']"
        return self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator))).click()

    def delete_img(self):
        locator = "//button[@class='image-preview__remove-btn']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def doorbell_button(self):
        locator = "//div[text()=' Doorbell ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()

    def doorbell_item(self):
        locator = "//div[@class='table-list-item']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def load_image(self):
        locator = "//input[@accept='image/jpeg']"
        return self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))

    def make_schedule(self):
        locator = "//div[text()=' Make your schedule ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def make_unit_manager(self):
        locator = "//div[text()=' Make this user a unit manager ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        time.sleep(1)
        self.save_button()

    def mark_doorbell_digital_keys(self):
        i = 0
        while i < 2:
            locator = "//div[text()=' Doorbell button ']"
            self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
            locator = "//div[text()=' Digital keys ']"
            self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
            i = i + 1
        self.save_button()

    def never_allow(self):
        locator = "//div[text()=' Never allow ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def press_icon(self):
        locator = "//div[@class='image-label']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def save_button(self):
        locator = "//button[@class='add-user-save-btn']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        time.sleep(1)

    def save_image(self):
        locator = "//button[text()='Save']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def schedule(self):
        locator = "//div[@class='form-radio__label']/following::label[2]"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def select_building(self):
        locator = f"//span[contains(text(), '{BUILDING}')]"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def select_unit(self):
        locator = f"//span[contains(text(), '{UID}')]"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def settings(self):
        locator = "//div[@routerlink='settings']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def fill_user_data_first_part(self):
        locator = "//input[@placeholder='Email']"
        email_field = self.driver.find_element(By.XPATH, locator)
        email_field.send_keys("JohnDoe@mail.com")

    def fill_user_data_phone(self):
        locator = "//div[@class='form-select-input-holder main-color']"
        self.driver.find_element(By.XPATH, locator).click()
        if server == 3:
            locator = "//span[text()='+1']"
        else:
            locator = "//span[text()='+46']"
        self.driver.find_element(By.XPATH, locator).click()
        locator = "//input[@placeholder='Phone']"
        phone_field = self.driver.find_element(By.XPATH, locator)
        phone_number = ''.join(random.sample(string.digits, 10))
        phone_field.send_keys(phone_number)

    def fill_user_data_phone_with_spaces(self):
        locator = "//div[@class='form-select-input-holder main-color']"
        self.driver.find_element(By.XPATH, locator).click()
        locator = "//span[text()='+46']"
        self.driver.find_element(By.XPATH, locator).click()
        locator = "//input[@placeholder='Phone']"
        phone_field = self.driver.find_element(By.XPATH, locator)
        phone_field.send_keys(" 01234567890 ")

    def fill_user_data_second_part(self):
        locator = "//div[text()=' Language ']/following::input[8]"
        self.driver.find_element(By.XPATH, locator).click()
        locator = "//span[text()='English']"
        self.driver.find_element(By.XPATH, locator).click()
        locator = "//input[@placeholder='First name']"
        firstname_field = self.driver.find_element(By.XPATH, locator)
        firstname_field.send_keys("John")
        locator = "//input[@placeholder='Last name']"
        lastname_field = self.driver.find_element(By.XPATH, locator)
        lastname_field.send_keys("Doe")

    def fill_email_data(self):
        locator = "//input[@placeholder='Email']"
        email_field = self.driver.find_element(By.XPATH, locator)
        email_field.send_keys("JohnDoe@mail.com")

    def fill_lang(self):
        locator = "//div[text()=' Language ']/following::input[8]"
        self.driver.find_element(By.XPATH, locator).click()
        locator = "//span[text()='English']"
        self.driver.find_element(By.XPATH, locator).click()

    def view_list_of_users(self):
        locator = "//button[@class='add-user-save-btn']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        time.sleep(1)
        locator = "//div[text()=' Users ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def use_schedule(self):
        locator = "//div[text()=' Use the schedule defined for this building ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
