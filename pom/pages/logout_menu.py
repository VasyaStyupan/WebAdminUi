import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

LOGOUT_MENU = '//div[@class="user-info-dropdown-mobile-button"]'
START_LOGOUT_MENU = "//*[text()=' Profile ']", "//*[text()=' Language ']", "//*[text()=' Logout ']"
NORWEGIAN = "//div[text()=' Norsk ']"
SWEDISH = "//div[text()=' Svenska ']"
PERSONAL_INFO = "//div[text()=' Personal Info ']"
UNITS = "//div[text()=' Units ']"
ACCESS = "//div[text()=' Access ']"
ADD_CARD = "//button[text()=' Add card ']"
ACCESS_CARDS = '//div[text()=" Access Cards "]'
# STATUS_DISABLED = '//i[@class="icon-app-ok-1"]'
# STATUS_ACTIVE = "//i[@class='icon-app-ok-1 ng-star-inserted']"
ADD_PIN_CODE = "//button[text()=' Add or change card PIN code ']"
ENTER_PIN_FIELD = "//input[@class='form-input ng-pristine ng-valid ng-star-inserted ng-touched']"
PIN_SAVE_BUTTON = "//button[@class='form-button-save']"


class Logout:
    def __init__(self, driver, *search_word):
        self.driver = driver
        self.word = search_word
        self.__wait = WebDriverWait(driver, 15, 0.5)

    def find_popup(self):
        xpath = LOGOUT_MENU
        return self.driver.find_element(By.XPATH, xpath)

    def input_card_number(self):
        locator = '//input[@placeholder="Enter card number"]'
        return self.__wait.until(ec.presence_of_element_located((By.XPATH, locator))).send_keys("86987707097")

    def input_card_name(self):
        locator = '//input[@placeholder="Enter card name"]'
        input_field = self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))
        input_field.send_keys("CardName")
        locator = "button.form-button-save"
        return self.__wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, locator))).click()

    def edit_card_name(self):
        locator = '//input[@placeholder="Enter card name"]'
        input_field = self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator)))
        input_field.send_keys(Keys.COMMAND, "a")
        input_field.send_keys("MyCard")
        locator = "button.form-button-save"
        return self.__wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, locator))).click()

    def enter_pin_code(self):
        locator = "//input[@type='password']"
        self.driver.find_element(By.XPATH, locator).send_keys("222222")
        locator = "//button[text()=' Save ']"
        return self.driver.find_element(By.XPATH, locator).click()

    def delete(self):
        locator = "//*[text()=' Delete ']"
        return self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator))).click()

    def remove_button(self):
        locator = "//button[@class='remove-dialog-accept-btn']"
        return self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator)))

    def edit(self):
        locator = "//*[text()=' Edit ']"
        return self.driver.find_element(By.XPATH, locator).click()

    def mark_digital_key(self):
        locator = "//label[@class='form-checkbox-holder']//following::i[3]"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def mark_doorbell_button(self):
        locator = "//label[@class='form-checkbox-holder']//following::i[2]"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def mark_unit_manager(self):
        locator = "//label[@class='form-checkbox-holder']//following::i[1]"
        return self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator))).click()

    def mark_status_card(self):
        locator = "i.icon-app-ok-1"
        return self.__wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator))).click()

    def button_remove_user(self):
        locator = "button.remove-user-btn"
        return self.__wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, locator))).click()

    def approve_remove(self):
        locator = "button.remove-dialog-accept-btn"
        return self.__wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, locator))).click()

    def edit_personal_info(self, firstname):
        locator = "//span[text()='Edit Info']"
        self.driver.find_element(By.XPATH, locator).click()
        time.sleep(1)
        locator = "//input[@placeholder='Enter name']"
        search_field = self.driver.find_element(By.XPATH, locator)
        search_field.clear()
        search_field.send_keys(firstname)
        locator = "//button[@class='form-button-save']"
        return self.driver.find_element(By.XPATH, locator).click()

    def edit_info(self):
        locator = "//span[text()='Edit Info']"
        return self.driver.find_element(By.XPATH, locator).click()

    def units_tag(self):
        locator = "//div[text()=' Units ']"
        return self.driver.find_element(By.XPATH, locator).click()

    def access_tag(self):
        locator = "//div[text()=' Access ']"
        return self.driver.find_element(By.XPATH, locator).click()

    def tips_doorbell_button(self):
        locator = "div.question-mark"
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def tips_digital_keys(self):
        locator = "body > app-root > app-building-host > main > app-profile > app-user-profile > div > " \
                  "div.user-profile-wrapper > div.user-profile-tabs-content > app-profile-ownership > " \
                  "div.profile-ownership.profile-ownership--hide-building-colum > " \
                  "div.profile-ownership-header.ownership-grid > div:nth-child(5) > span > div > svg > path"
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def add_card_button(self):
        locator = "//button[text()=' Add card ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def add_units_button(self):
        locator = "//button[text()=' Add units ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def mark_unit(self):
        locator = "//div[@class='form-checkbox']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        locator = "//div[@class='form-checkbox']/following::i"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def save_unit_button(self):
        locator = "//button[@class='save-btn']"
        return self.__wait.until(ec.presence_of_element_located((By.XPATH, locator))).click()

    def switch_to_norwegian(self):
        locator = "//div[@class='form-radio__label']/following::label[1]"
        return self.__wait.until(ec.presence_of_element_located((By.XPATH, locator))).click()

    def switch_to_swedish(self):
        locator = "//div[@class='form-radio__label']/following::label[2]"
        return self.__wait.until(ec.presence_of_element_located((By.XPATH, locator))).click()


