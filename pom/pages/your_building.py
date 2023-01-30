import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from configuration import BUILDING, DOORBELL
import random
import string

FIRST_LINE = ["//app-units-list-item", "//app-users-list-item", "//app-access-list-item", "//app-doorbells-list-item"]
TAGS = ("//div[text()=' Units ']", "//div[text()=' Users ']", "//div[text()=' Access ']", "//div[text()=' Doorbell ']")
SUB_TAGS = [
    ("//span[text()=' GID ']", "//span[text()=' UID ']", "//span[text()=' Unit name ']", "//span[text()=' Floor ']",
     "//span[text()=' Number of users ']"),
    ("", "//span[text()=' Username ']", "//span[text()=' First Name ']", "//span[text()=' Last Name ']",
     "//span[text()=' Email ']",),
    ("//span[text()=' Door Name ']",), ("//span[text()=' Doorbell Name ']",)]
REMOVE_BUTTON_FROM_DOORBELL = "//div[@class='form-checkbox__label']"
ADD_USER = "//div[@class='form-checkbox__label']"
UNIT_USERS = "//app-unit-users-list-item"


class Buildings:
    def __init__(self, driver, *param):
        self.driver = driver
        self.param = param
        self.__wait = WebDriverWait(driver, 15, 0.3)

    def always_allow(self):
        locator = "//div[text()=' Always allow ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def access_cards_tag(self):
        locator = '//div[text()=" Access Cards "]'
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def add_role_unit_manager_function(self):
        locator = "//div[text()=' Add the role of unit manager to another user ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def add_user_function(self):
        locator = "//div[text()=' Add a user ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def allow_um_enable_ao(self):
        locator = "//div[text()=' Allow unit manager to enable automatic opening ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def ao_on(self):
        locator = "//div[text()=' On ']"
        element = self.driver.find_elements(By.XPATH, locator)[1]
        if element.value_of_css_property('background-color') == 'rgba(196, 196, 196, 1)':
            element.click()

    def ao_on_unit_level(self):
        locator = "//div[text()=' On ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        if element.value_of_css_property('background-color') == 'rgba(196, 196, 196, 1)':
            element.click()

    def assign_ao_to_specific_users(self):
        locator = "//div[text()=' Assign automatic opening to specific users ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def building_address(self):
        locator = "//div[@class='breadcrumbs__btn']"
        address = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        locator = "//div[@class='section-entity-name']"
        unit = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        return address.text[8:], unit.text

    def block_adding_RFID_cards(self):
        locator = "//div[text()=' Block adding RFID cards ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def brightness_thumb(self):
        locator = "//div[@class='mat-slider-thumb']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def cancel(self):
        locator = "//span[text()='Cancel']"
        return self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator)))

    def change_unit_name_function(self):
        locator = "//div[text()=' Change unit name ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def edit_info_button(self):
        locator = "//button[text()=' Edit Info ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def check_family_mode(self):
        locator = "//div[text()=' Off ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def close_custom_days(self):
        locator = "span[text()='Close']"
        return self.driver.find_element(By.XPATH, locator)

    def close_button(self):
        locator = "//span[text()='Close']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def choose_day(self):
        locator = "//div[@class='calendar-day__time-range']/following::div[1]"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def choose_another_day(self):
        locator = "//div[@class='calendar-day doorbell-disabled-day ng-star-inserted']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def done_button(self):
        locator = "//button[@class='save-btn']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def doorbell_button(self):
        locator = "//div[text()=' Doorbell ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def doorbell_name(self):
        locator = "//input[@placeholder='Doorbell name']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def enable_search(self):
        locator = "//div[text()=' Enable search field ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def enable_ao_for_all_users(self):
        locator = "//div[text()=' Enable automatic opening for all users ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def floor_abbreviation(self):
        locator = "//input[@placeholder='Abbr.']"
        return self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))

    def floor_number(self):
        locator = "//input[@placeholder='Enter number']"
        return self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))

    def forbid_upload_unit_image(self):
        locator = "//div[text()=' Upload unit image ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()

    def generate_random_string(self):
        length = self.param[0]
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string

    def list_of_floors_button(self):
        locator = "//button[text()=' List of floors ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def list_of_floors_item(self):
        locator = "//div[@class='list-of-floors-item__number']"
        return len(self.__wait.until(ec.visibility_of_all_elements_located((By.XPATH, locator))))

    def make_unit_image_visible(self):
        locator = "//div[text()=' Make unit image visible ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def make_user_image_visible(self):
        locator = "//div[text()=' Make user image visible ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def make_your_schedule(self):
        locator = "//div[text()=' Make your schedule ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def never_allow(self):
        locator = "//div[text()=' Never allow ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def pin_code_is_mandatory(self):
        locator = "//div[text()=' PIN code is mandatory when entering with RFID card ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def RFID_cards_function(self):
        locator = "//div[text()=' Administrate users RFID cards ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def remove_buttons_from_doorbell(self):
        locator = "//div[text()=' Remove all buttons from the doorbell ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def remove_user(self):
        locator = "//button[@class='remove-user-btn ng-star-inserted']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def save_changes_button(self):
        locator = "//button[text()=' Save changes ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def save_button(self):
        locator = "//button[text()=' Save ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def save_day_button(self):
        locator = "//button[text()='Save']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def search_units(self):
        locator = "//div[@class='search-field']/following::input[5]"
        return self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator)))

    def select_any_doorbell(self):
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@class='table-list-item']")))

    def select_any_building(self):
        locator = "//div[@class='table-list-item__coll']/child::span"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def select_building(self):
        # address = self.param[0]
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{BUILDING}')]")))

    def select_doorbell(self):
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{DOORBELL}')]")))

    def select_floor(self):
        floor = self.param[0]
        return self.__wait.until(ec.element_to_be_clickable(
            (By.XPATH, f"//span[contains(text(), '{floor}')]")))

    def select_tag(self):
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, self.param[0])))

    def settings_tab(self):
        locator = "//div[text()=' Settings ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def select_user(self):
        user = self.param[0]
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{user}')]"))).click()

    def schedule(self):
        locator = "//div[text()=' Schedule ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def set_up_custom_days(self):
        locator = "//button[text()=' Set Up Custom Days ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def start_time(self):
        locator = "//input[@class='form-input ng-pristine ng-valid ng-star-inserted ng-touched']"
        return self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator)))

    def your_units_button(self):
        locator = "//button[text()=' Your units ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def your_buildings_button(self):
        locator = "//button[text()=' Your buildings ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def volume_thumb(self):
        locator = "//div[@class='mat-slider-thumb']/following::mat-slider"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def unit_id(self):
        locator = "//input[@placeholder='Enter name']"
        return self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator)))

    def unit_name(self):
        locator = "//input[@placeholder='Enter name']/following::input"
        return self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator)))

    def unit_floor(self):
        locator = "//i[@class='icon-app-down-open form-select-input-icon']"
        return self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator)))

    def uncheck_show_user_image(self):
        locator = "//div[text()=' Show user image ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def uncheck_show_unit_image(self):
        locator = "//div[text()=' Show unit image ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def unit_image_disabled(self):
        locator = "//div[text()=' Visible ']/following::label[1]"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def units_tag(self):
        locator = "//div[text()=' Units ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def upload_unit_image(self):
        locator = "//div[text()=' Upload unit image ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def use_schedule_defined_for_this_building(self):
        locator = "//div[text()=' Use the schedule defined for this building ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def user_image_disabled(self):
        locator = "//div[text()=' Visible ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def users_tag(self):
        locator = "//div[text()=' Users ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
