import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from configuration import BUILDING, BROWSER, DOORBELL

FIRST_LINE = ["//app-units-list-item", "//app-users-list-item", "//app-access-list-item", "//app-doorbells-list-item"]
TAGS = ("//div[text()=' Units ']", "//div[text()=' Users ']", "//div[text()=' Access ']", "//div[text()=' Doorbell ']")
SUB_TAGS = [
    ("//span[text()=' GID ']", "//span[text()=' UID ']", "//span[text()=' Unit name ']", "//span[text()=' Floor ']",
     "//span[text()=' Number of users ']"),
    ("", "//span[text()=' Username ']", "//span[text()=' First Name ']", "//span[text()=' Last Name ']",
     "//span[text()=' Email ']",),
    ("//span[text()=' Door Name ']",), ("//span[text()=' Doorbell Name ']",)]


class Buildings:
    def __init__(self, driver, *param):
        self.driver = driver
        self.param = param
        self.__wait = WebDriverWait(driver, 15, 0.3)

    def always_allow(self):
        locator = "//div[text()=' Always allow ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def add_role_unit_manager_function(self):
        locator = "//div[text()=' Add the role of unit manager to another user ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def add_user_function(self):
        locator = "//div[text()=' Add a user ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def access_cards(self):
        locator = '//div[text()=" Access Cards "]'
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def allow_um_enable_ao(self):
        locator = "//div[text()=' Allow unit manager to enable automatic opening ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

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
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()

    def building_address(self):
        locator = "//div[@class='breadcrumbs__btn']"
        address = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        locator = "//div[@class='section-entity-name']"
        unit = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        return address.text[8:], unit.text

    def block_adding_RFID_cards(self):
        locator = "//div[text()=' Block adding RFID cards ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def cancel(self):
        locator = "//span[text()='Cancel']"
        return self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator))).click()

    def change_unit_name_function(self):
        locator = "//div[text()=' Change unit name ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def change_list_of_floors(self):
        floors_number = self.param
        locator = "//input[@placeholder='Enter number']"
        input_floors = self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))
        input_floors.send_keys(Keys.COMMAND, "a")
        input_floors.send_keys(Keys.DELETE)
        input_floors.send_keys(floors_number)
        input_floors.send_keys(Keys.RETURN)

    def change_time(self):
        locator = "//div[@class='time-picker']/following::input[39]"
        start_time = self.driver.find_element(By.XPATH, locator)
        start_time.clear()
        start_time.send_keys('01:00')

    def change_unit_name(self):
        unit = self.param
        locator = "//button[text()=' Edit Info ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        time.sleep(1)
        locator = "//input[@placeholder='Enter name']/following::input"
        unit_name = self.__wait.until(ec.visibility_of_element_located((By.XPATH, locator)))
        unit_name.clear()
        unit_name.send_keys(unit)
        time.sleep(1)
        locator = "//button[text()=' Save ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def check_family_mode(self):
        locator = "//div[text()=' Off ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def checkbox_recovery_after_selection(self):
        locator = "//i[@class='icon-app-ok-1']"  # remove all buttons from doorbell
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        if element.value_of_css_property('color') == 'rgba(255, 255, 255, 1)':
            time.sleep(1)
            element.click()
        locator = "//i[@class='icon-app-ok-1']/following::i[1]"  # enable search field
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        if element.value_of_css_property('color') == 'rgba(255, 255, 255, 1)':
            time.sleep(1)
            element.click()
        locator = "//i[@class='icon-app-ok-1']/following::i[2]"  # show user image
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        if element.value_of_css_property('color') == 'rgba(0, 0, 0, 0)':
            time.sleep(1)
            element.click()
        locator = "//i[@class='icon-app-ok-1']/following::i[3]"  # show unit image
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        if element.value_of_css_property('color') == 'rgba(0, 0, 0, 0)':
            time.sleep(1)
            element.click()
        locator = "//i[@class='icon-app-ok-1']/following::i[6]"  # upload unit image
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        if element.value_of_css_property('color') == 'rgba(0, 0, 0, 0)':
            time.sleep(1)
            element.click()
        locator = "//i[@class='icon-app-ok-1']/following::i[7]"  # mark unit image visible
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        if element.value_of_css_property('color') == 'rgba(0, 0, 0, 0)':
            time.sleep(1)
            element.click()
        locator = "//i[@class='icon-app-ok-1']/following::i[8]"  # make user image visible
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        if element.value_of_css_property('color') == 'rgba(0, 0, 0, 0)':
            time.sleep(1)
            element.click()
        locator = "//i[@class='icon-app-ok-1']/following::i[9]"  # allow um ao
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        if element.value_of_css_property('color') == 'rgba(0, 0, 0, 0)':
            time.sleep(1)
            element.click()
            time.sleep(1)

    def close_custom_days(self):
        locator = "span[text()='Close']"
        return self.driver.find_element(By.XPATH, locator)

    def choose_day(self):
        locator = "//div[@class='calendar-day__time-range']/following::div[1]"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def choose_another_day(self):
        locator = "//div[@class='calendar-day doorbell-disabled-day ng-star-inserted']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def doorbell_button(self):
        locator = "//div[text()=' Doorbell ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()

    def enable_search(self):
        locator = "//div[text()=' Enable search field ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def enable_ao_for_all_users(self):
        locator = "//div[text()=' Enable automatic opening for all users ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()

    def enter_doorbell_unit_level(self):
        self.your_units_button()
        self.doorbell_button()
        self.select_doorbell()

    def forbid_upload_unit_image(self):
        locator = "//div[text()=' Upload unit image ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()

    def delete_user_from_unit(self):
        xpath = "//app-unit-users-list-item"
        item_list = self.__wait.until(ec.visibility_of_all_elements_located((By.XPATH, xpath)))
        for i in range(1, len(item_list)):
            element = self.__wait.until(ec.visibility_of_element_located((By.XPATH, f"{xpath}[{i}]/child::div/child::div[2]")))
            if element.text == "JohnDoe@mail.com":
                self.__wait.until(ec.element_to_be_clickable((By.XPATH, f"{xpath}[{i}]/child::div/child::div[10]"))).click()
                self.__wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Yes, remove']"))).click()

    def get_doorbell_name(self):
        locator = "//div[text()=' Doorbell ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        locator = "//div[@class='table-list-item__coll']"
        doorbell_name = self.driver.find_element(By.XPATH, locator)
        doorbell_name = doorbell_name.text
        locator = "//div[@class='table-list-item__coll']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        return doorbell_name

    def input_doorbell_name(self):
        locator = "//input[@placeholder='Doorbell name']"
        doorbell = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        doorbell.click()
        if BROWSER == 1:
            doorbell.send_keys(Keys.HOME)
            time.sleep(1)
            doorbell.send_keys(Keys.COMMAND, "a")
        else:
            doorbell.clear()
        time.sleep(1)
        doorbell.send_keys(self.param[0])
        locator = "//button[text()=' Save ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        time.sleep(1)

    def RFID_cards_function(self):
        locator = "//div[text()=' Administrate users RFID cards ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def remove_buttons_from_doorbell(self):
        locator = "//div[text()=' Remove all buttons from the doorbell ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()

    def remove_user(self):
        locator = "//button[@class='remove-user-btn ng-star-inserted']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def save_day(self):
        locator = "//button[text()='Save']"
        self.driver.find_element(By.XPATH, locator).click()

    def select_any_doorbell(self):
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@class='table-list-item']"))).click()

    def select_any_building(self):
        locator = "//div[@class='table-list-item__coll']/child::span"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def select_building(self):
        # address = self.param[0]
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{BUILDING}')]"))).click()

    def select_doorbell(self):
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{DOORBELL}')]"))).click()

    def select_tag(self):
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, self.param[0]))).click()

    def settings_tab(self):
        locator = "//div[text()=' Settings ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def select_user(self):
        user = self.param[0]
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{user}')]"))).click()

    def schedule(self):
        locator = "//div[text()=' Schedule ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def set_up_custom_days(self):
        locator = "//button[text()=' Set Up Custom Days ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def make_unit_image_visible(self):
        locator = "//div[text()=' Make unit image visible ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def make_user_image_visible(self):
        locator = "//div[text()=' Make user image visible ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def make_your_schedule(self):
        locator = "//div[text()=' Make your schedule ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def never_allow(self):
        locator = "//div[text()=' Never allow ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def pin_code_is_mandatory(self):
        locator = "//div[text()=' PIN code is mandatory when entering with RFID card ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def your_units_button(self):
        locator = "//button[text()=' Your units ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def your_buildings_button(self):
        locator = "//button[text()=' Your buildings ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def volume_thumb(self):
        locator = "//div[@class='mat-slider-thumb']/following::mat-slider"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def user_image_disabled(self):
        locator = "//div[text()=' Visible ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def unit_image_disabled(self):
        locator = "//div[text()=' Visible ']/following::label[1]"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def upload_unit_image(self):
        locator = "//div[text()=' Upload unit image ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def use_schedule_defined_for_this_building(self):
        locator = "//div[text()=' Use the schedule defined for this building ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def uncheck_show_user_image(self):
        locator = "//div[text()=' Show user image ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()

    def uncheck_show_unit_image(self):
        locator = "//div[text()=' Show unit image ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()

    def users_tag(self):
        locator = "//div[text()=' Users ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

