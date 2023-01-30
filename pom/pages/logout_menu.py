import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from configuration import UNIT

LOGOUT_MENU = '//div[@class="user-info-dropdown-mobile-button"]'
START_LOGOUT_MENU = "//*[text()=' Profile ']", "//*[text()=' Language ']", "//*[text()=' Logout ']"
NORWEGIAN = "//div[text()=' Norsk ']"
SWEDISH = "//div[text()=' Svenska ']"
PERSONAL_INFO = "//div[text()=' Personal Info ']"
UNITS = "//div[text()=' Units ']"
LOGOUT = "//div[text()=' Logout ']"
ACCESS = "//div[text()=' Access ']"
ACCESS_CARDS = '//div[text()=" Access Cards "]'
ENTER_PIN_FIELD = "//input[@class='form-input ng-pristine ng-valid ng-star-inserted ng-touched']"
PIN_SAVE_BUTTON = "//button[@class='form-button-save']"


class Logout:
    def __init__(self, driver, *param):
        self.driver = driver
        self.param = param
        self.__wait = WebDriverWait(driver, 5, 0.2)

    def access_cards(self):
        locator = '//div[text()=" Access Cards "]'
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def access_tag(self):
        locator = "//div[text()=' Access ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def add_card_button(self):
        locator = "//button[text()=' Add card ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def add_pin_code(self):
        locator = "//button[text()=' Add or change card PIN code ']"
        return self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))

    def add_units_button(self):
        locator = "//button[text()=' Add units ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def approve_remove(self):
        locator = "button.remove-dialog-accept-btn"
        return self.__wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, locator)))

    def button_remove_user(self):
        locator = "button.remove-user-btn"
        return self.__wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, locator)))

    def card_name(self):
        locator = '//input[@placeholder="Enter card name"]'
        return self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator)))

    def card_number(self):
        locator = '//input[@placeholder="Enter card number"]'
        return self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))

    def checkbox_unit_manager(self):
        locator = f"//span[contains(text(), '{UNIT}')]/following::div[3]/child::input/following::i[1]"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def checkbox_doorbell_button(self):
        locator = f"//span[contains(text(), '{UNIT}')]/following::div[7]"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def checkbox_digital_key(self):
        locator = f"//span[contains(text(), '{UNIT}')]/following::div[12]"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def delete(self):
        locator = "//div[@class='profile-cards-coll__rfid-name__text']/parent::div/following::div[15]"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def edit(self):
        locator = "//*[text()=' Edit ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    # def edit_personal_info(self):
    #     firstname = self.param
    #     locator = "//span[text()='Edit Info']"
    #     self.__wait.until(ec.presence_of_element_located((By.XPATH, locator))).click()
    #     time.sleep(1)
    #     locator = "//input[@placeholder='Enter name']"
    #     search_field = self.driver.find_element(By.XPATH, locator)
    #     search_field.clear()
    #     search_field.send_keys(firstname)
    #     locator = "//button[@class='form-button-save']"
    #     return self.driver.find_element(By.XPATH, locator).click()

    def edit_info(self):
        locator = "//span[text()='Edit Info']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def mark_status_card(self):
        locator = "i.icon-app-ok-1"
        element = self.__wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        time.sleep(1)
        element.click()
        time.sleep(1)

    def mark_unit(self):
        locator = "//div[@class='form-checkbox']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        locator = "//div[@class='form-checkbox']/following::i"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def pin_code(self):
        locator = "//input[@type='password']"
        return self.driver.find_element(By.XPATH, locator)

    def remove_button(self):
        locator = "//button[@class='remove-dialog-accept-btn']"
        return self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator)))

    def remove_unit(self):
        locator = "//button[@class='remove-unit-btn ng-star-inserted']"
        return self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator)))

    def return_to_unit(self):
        locator = f"//div[text()='{UNIT}']"
        locator = f"//div[contains(text(), '{UNIT}')]"
        print(UNIT)
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def save_button(self):
        locator = "button.form-button-save"
        return self.__wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, locator)))

    def save_unit_button(self):
        locator = "//button[@class='save-btn']"
        return self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))

    def switch_to_norwegian(self):
        locator = "//div[@class='form-radio__label']/following::label[1]"
        return self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))

    def switch_to_swedish(self):
        locator = "//div[@class='form-radio__label']/following::label[2]"
        return self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))

    def switch_to_deutsch(self):
        locator = "//div[@class='form-radio__label']/following::label[3]"
        return self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))

    def tips_doorbell_button(self):
        locator = "//div[@class='question-mark']"
        return self.driver.find_element(By.XPATH, locator)

    def tips_digital_keys(self):
        locator = "//div[@class='question-mark']/following::div[2]"
        return self.driver.find_element(By.XPATH, locator)

    def unit(self):
        locator = "//div[@class='form-checkbox']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def units_tag(self):
        locator = "//div[text()=' Units ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
