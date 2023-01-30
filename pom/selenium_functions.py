import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from configuration import BASE_URL, USERNAME_UM, USERNAME_BA, PASSWORD_UM, CODE, UNIT, UID, BUILDING, DOORBELL, server, \
    USERNAME_UO, SIMPLE_USER
from pom.pages.code_page import CodePage
from pom.pages.login_page import LoginPage, SELECT_SERVER_US, SELECT_SERVER_EU
from pom.pages.logout_menu import Logout, START_LOGOUT_MENU, LOGOUT, UNITS, ACCESS_CARDS, LOGOUT_MENU
from pom.pages.mainscreen_page import MainScreen
from pom.pages.your_units import Units
from pom.pages.your_building import Buildings, REMOVE_BUTTON_FROM_DOORBELL, ADD_USER, UNIT_USERS
from pom.pages.hwa import Hwa
from pathlib import Path


class Signin(LoginPage, CodePage):
    def __init__(self, driver, username, password, *code):
        super().__init__(driver)
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 2, 0.3)
        self.username = username
        self.password = password
        self.code = code

    def login_credentials(self):
        LoginPage(self.driver).search_login_field(self.username)
        LoginPage(self.driver).search_password_field(self.password)
        try:
            self.__wait.until(ec.url_to_be(f"{BASE_URL}/auth-code"))
        except Exception:
            pass
        return self.driver.current_url

    def login_code(self):
        CodePage(self.driver).search_code_field(self.code)
        try:
            self.__wait.until(ec.url_changes(f"{BASE_URL}/auth-code"))
            MainScreen(self.driver).check_load_main_page()
        except Exception:
            pass
        return self.driver.current_url


class Base(LoginPage):
    def __init__(self, driver, *param):
        super().__init__(driver)
        self.__wait = WebDriverWait(driver, 10, 0.3)
        self.driver = driver
        self.param = param

    def add_card(self):
        Logout(self.driver).add_card_button().click()
        if 'Add units' in self.driver.page_source:
            self.check_if_units_more_then_one()
        Base(self.driver, self.param[0], self.param[1]).input_card_info()
        status = Logout(self.driver).save_button().is_enabled()
        if status is True:
            Logout(self.driver).save_button().click()
        else:
            Buildings(self.driver).cancel()
        return status

    def add_pin_code(self):
        Logout(self.driver).add_pin_code().click()
        return Base(self.driver, "22222222").enter_pin_code()

    def add_units(self):
        Logout(self.driver).add_card_button()
        if "Add unit" in self.driver.page_source:
            Logout(self.driver).add_units_button()
            Logout(self.driver).mark_unit().click()
            Logout(self.driver).save_unit_button().click()
            return True

    def add_simple_user(self):
        element = Units(self.driver).add_user_button()
        time.sleep(1)  # safari
        element.click()
        Units(self.driver).fill_simple_user_data()

    def add_user(self):
        element = Units(self.driver).add_user_button()
        time.sleep(1)  # safari
        element.click()
        Units(self.driver).fill_user_data_first_part()
        Units(self.driver).fill_user_data_phone()
        Units(self.driver).fill_user_data_second_part()

    def add_user_without_phone(self):
        element = Units(self.driver).add_user_button()
        time.sleep(1)  # safari
        element.click()
        Units(self.driver).fill_user_data_first_part()
        Units(self.driver).fill_user_data_second_part()

    def add_user_phone_with_spaces(self):
        element = Units(self.driver).add_user_button()
        time.sleep(1)  # safari
        element.click()
        Units(self.driver).fill_user_data_first_part()
        Units(self.driver).fill_user_data_phone_with_spaces()
        Units(self.driver).fill_user_data_second_part()

    def add_user_with_only_email(self):
        element = Units(self.driver).add_user_button()
        time.sleep(1)  # safari
        element.click()
        Units(self.driver).fill_email_data()
        Units(self.driver).fill_lang()

    def add_user_with_old_email_and_new_data(self):
        element = Units(self.driver).add_user_button()
        time.sleep(1)  # safari
        element.click()
        Units(self.driver).fill_user_data_first_part_new()
        Units(self.driver).fill_user_data_phone()
        Units(self.driver).fill_user_data_second_part_new()

    def add_user_with_old_phone_and_new_data(self):
        element = Units(self.driver).add_user_button()
        time.sleep(1)  # safari
        element.click()
        Units(self.driver).fill_email_data()
        Units(self.driver).fill_lang()
        Units(self.driver).fill_user_data_phone()
        Units(self.driver).fill_user_data_second_part_new()

    def block_RFID_cards(self):
        i = 0
        while i < 3:
            Buildings(self.driver).block_adding_RFID_cards()
            time.sleep(1)
            i += 1
        Buildings(self.driver).pin_code_is_mandatory()

    def change_list_of_floors_part1(self):
        floors_number = self.param
        input_floors = Buildings(self.driver).floor_number()
        input_floors.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        input_floors.send_keys(floors_number)
        time.sleep(1)
        element = Buildings(self.driver).list_of_floors_button()
        time.sleep(1)  # safari
        element.click()
        items = Buildings(self.driver).list_of_floors_item()
        return items

    def change_list_of_floors_part2(self):
        abbreviation = self.param
        input_floors = Buildings(self.driver).floor_abbreviation()
        input_floors.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        input_floors.send_keys(abbreviation)
        Buildings(self.driver).save_changes_button().click()
        time.sleep(4)
        Buildings(self.driver).close_button().click()
        time.sleep(1)
        Buildings(self.driver).units_tag().click()

    def change_time(self):
        start_time = Buildings(self.driver).start_time()
        start_time(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        start_time.clear()
        # time.sleep(1)
        # start_time.send_keys('03:50')

    def change_unit_information(self):
        uid = self.param[0]
        unit = self.param[1]
        floor = self.param[2]
        Buildings(self.driver).edit_info_button().click()
        time.sleep(1)
        uid_name = Buildings(self.driver).unit_id()
        uid_name.clear()
        uid_name.send_keys(uid)
        time.sleep(1)
        unit_name = Buildings(self.driver).unit_name()
        unit_name.clear()
        unit_name.send_keys(unit)
        time.sleep(1)
        Buildings(self.driver).unit_floor().click()
        Buildings(self.driver, floor).select_floor().click()
        Buildings(self.driver).save_button().click()

    def change_unit_info_ba(self):
        Units(self.driver).select_building().click()
        time.sleep(1)
        Units(self.driver, UID).select_unit().click()
        time.sleep(1)
        Units(self.driver).settings().click()

    def change_unit_manager_role(self):
        Units(self.driver).select_building()
        Units(self.driver).settings()
        Units(self.driver).change_unit_manager()

    def change_unit_name(self):
        unit = self.param
        Units(self.driver).edit_info_button().click()
        time.sleep(1)
        unit_name = Units(self.driver).unit_id()
        unit_name.clear()
        unit_name.send_keys(unit)
        time.sleep(1)
        Buildings(self.driver).save_button().click()

    def change_unit_owner(self):
        username = self.param[0]
        Units(self.driver).change_unit_owner_button().click()
        time.sleep(1)
        search = Buildings(self.driver).search_units()
        time.sleep(1)  # safari
        search.send_keys(username)
        time.sleep(1)
        locator = f"//span[text()='{username}']/parent::div/parent::div/child::div[5]"
        first_name = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).text
        locator = f"//span[text()='{username}']/parent::div/parent::div/child::div[6]"
        last_name = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).text
        Units(self.driver).checkbox_unit_owner().click()
        Buildings(self.driver).done_button().click()
        return first_name, last_name

    def check_add_user_function(self):
        Buildings(self.driver).add_user_function()
        time.sleep(3)
        self.logout()
        Signin(self.driver, USERNAME_UM, PASSWORD_UM, CODE).login_credentials()
        Signin(self.driver, USERNAME_UM, PASSWORD_UM, CODE).login_code()
        Base(self.driver, UNIT).select_unit()

    def check_add_role_unit_manager__function(self):
        Buildings(self.driver).add_role_unit_manager_function().click()
        time.sleep(3)
        self.logout()
        Signin(self.driver, USERNAME_UM, PASSWORD_UM, CODE).login_credentials()
        Signin(self.driver, USERNAME_UM, PASSWORD_UM, CODE).login_code()
        Base(self.driver, UNIT).select_unit()
        element = Units(self.driver).add_user_button()
        time.sleep(1)
        element.click()
        Units(self.driver).fill_user_data_first_part()
        Units(self.driver).fill_user_data_phone()
        Units(self.driver).fill_user_data_second_part()
        Units(self.driver).make_unit_manager().click()

        # Buildings(self.driver).RFID_cards_function()

    def check_change_unit_name_function(self):
        Buildings(self.driver).change_unit_name_function()
        time.sleep(3)
        self.logout()
        Signin(self.driver, USERNAME_UM, PASSWORD_UM, CODE).login_credentials()
        Signin(self.driver, USERNAME_UM, PASSWORD_UM, CODE).login_code()
        Base(self.driver, UNIT).select_unit()

    def checkbox_recovery(self):
        self.enter_the_doorbell()
        self.driver.refresh()
        time.sleep(1)
        self.checkbox_recovery_after_selection()

    def checkbox_settings(self):
        Buildings(self.driver).select_building().click()
        Buildings(self.driver).settings_tab().click()
        self.checkbox_recovery_settings()

    def checkbox_recovery_after_selection(self):
        start_locator = REMOVE_BUTTON_FROM_DOORBELL
        elements = self.driver.find_elements(By.XPATH, start_locator)
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, f"{start_locator}/child::i")))
        if element.value_of_css_property('color') == 'rgba(255, 255, 255, 1)':
            element.click()
            time.sleep(1)
        # Check if always allow enabled
        locator = f"{start_locator}/following::i[9]"  # Allow unit manager to enable automatic opening
        element = self.driver.find_element(By.XPATH, locator)
        if element.value_of_css_property('color') == 'rgba(0, 0, 0, 0)':
            element = Buildings(self.driver).always_allow()
            element.click()
        time.sleep(1)
        for i in range(1, len(elements)):
            locator = f"{start_locator}/following::i[{i}]"
            element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
            if i != 1 and element.value_of_css_property('color') == 'rgba(0, 0, 0, 0)':
                element.click()
                time.sleep(1)
            if i == 1 and element.value_of_css_property('color') == 'rgba(255, 255, 255, 1)':
                element.click()
                time.sleep(1)

    def checkbox_recovery_settings(self):
        start_locator = ADD_USER
        elements = self.__wait.until(ec.presence_of_all_elements_located((By.XPATH, start_locator)))
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, f"{start_locator}/child::i")))
        if element.value_of_css_property('color') == 'rgba(0, 0, 0, 0)':
            element.click()
            time.sleep(1)
        for i in range(1, len(elements)):
            locator = f"{start_locator}/following::i[{i}]"
            element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
            if element.value_of_css_property('color') == 'rgba(0, 0, 0, 0)':
                element.click()
                time.sleep(1)

    def check_doorbell_display_conditions(self):
        self.enter_the_doorbell()
        time.sleep(1)
        Buildings(self.driver).upload_unit_image().click()
        time.sleep(1)
        Buildings(self.driver).make_unit_image_visible().click()
        time.sleep(1)
        Buildings(self.driver).make_user_image_visible().click()
        time.sleep(1)
        Buildings(self.driver).allow_um_enable_ao().click()

    def check_if_units_more_then_one(self):
        self.__wait.until(
            ec.element_to_be_clickable((By.XPATH, f"//button[contains(text(), 'Add units')]"))).click()
        time.sleep(1)
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@class='form-checkbox__label']"))).click()
        self.__wait.until(
            ec.element_to_be_clickable((By.XPATH, "//button[text()=' Save ']/following::button[2]"))).click()
        element = self.driver.find_element(By.XPATH, "//div[@class='add-units-cell']/following::div[1]")
        return element.text

    def check_if_doorbell_button_inactive(self):
        element = Logout(self.driver).checkbox_doorbell_button()
        if element.value_of_css_property('color') == 'rgba(0, 0, 0, 0)':
            return True
        else:
            return False

    def check_if_digital_key_inactive(self):
        element = Logout(self.driver).checkbox_digital_key()
        if element.value_of_css_property('color') == 'rgba(0, 0, 0, 0)':
            return True
        else:
            return False

    def check_if_unit_manager_active(self):
        element = Logout(self.driver).checkbox_unit_manager()
        return element.is_enabled()

    def check_tips(self):
        self.find_popup().click()
        self.logout_menu()
        Logout(self.driver).units_tag().click()

    def check_tips_doorbell_button(self):
        self.check_tips()
        xpath = Logout(self.driver).tips_doorbell_button()
        ActionChains(self.driver).move_to_element(xpath).perform()

    def check_tips_digital_keys(self):
        self.check_tips()
        xpath = Logout(self.driver).tips_digital_keys()
        ActionChains(self.driver).move_to_element(xpath).perform()

    def check_your_units(self):
        if "Your units" not in self.driver.page_source:
            self.fix_your_units()

    def check_user_image(self):
        self.enter_the_doorbell()
        Buildings(self.driver).uncheck_show_user_image()
        Buildings(self.driver).make_user_image_visible()
        Buildings(self.driver).uncheck_show_unit_image()
        Buildings(self.driver).make_unit_image_visible()
        Buildings(self.driver).upload_unit_image()

    def check_unit_image(self):
        self.enter_the_doorbell()
        Buildings(self.driver).uncheck_show_unit_image()
        Buildings(self.driver).upload_unit_image()
        Buildings(self.driver).make_unit_image_visible()
        Buildings(self.driver).uncheck_show_user_image()
        Buildings(self.driver).make_user_image_visible()

    def check_user_image_disabled(self):
        try:
            Buildings(self.driver).user_image_disabled()
            return False
        except Exception:
            return True

    def check_unit_image_disabled(self):
        try:
            Buildings(self.driver).unit_image_disabled()
            return False
        except Exception:
            return True

    def check_unit_manager_active(self):
        element = Logout(self.driver).checkbox_unit_manager()
        if element.value_of_css_property('color') == 'rgba(0, 0, 0, 0)':
            element = Logout(self.driver).checkbox_unit_manager()
            time.sleep(1)  # safari
            element.click()

    def check_volume(self):
        time.sleep(1)
        move = ActionChains(self.driver)
        thumb1 = Buildings(self.driver).brightness_thumb()
        move.click_and_hold(thumb1).move_by_offset(100, 0).release().perform()
        time.sleep(1)
        move.click_and_hold(thumb1).move_by_offset(-50, 0).release().perform()
        move = ActionChains(self.driver)
        thumb2 = Buildings(self.driver).volume_thumb()
        move.click_and_hold(thumb2).move_by_offset(100, 0).release().perform()
        time.sleep(1)
        move.click_and_hold(thumb2).move_by_offset(-50, 0).release().perform()
        time.sleep(1)

    def configure_ao(self):
        Units(self.driver).never_allow().click()
        time.sleep(1)
        Units(self.driver).always_allow().click()
        time.sleep(1)
        Units(self.driver).schedule().click()
        time.sleep(1)

    def delete_card(self):
        self.__wait.until(ec.visibility_of_element_located(
            (By.XPATH, f"//div[contains(text(), {self.param[0]})]")))
        Logout(self.driver).delete().click()
        Logout(self.driver).remove_button().click()
        time.sleep(1)

    def delete_image(self):
        Units(self.driver).doorbell_tag().click()
        Units(self.driver).doorbell().click()
        time.sleep(1)
        xpath = Units(self.driver).choose_delete()
        ActionChains(self.driver).move_to_element(xpath).perform()
        xpath = Units(self.driver).delete_img()
        ActionChains(self.driver).move_to_element(xpath).click().perform()
        Units(self.driver).accept_delete().click()

    def delete_user(self):
        Hwa(self.driver).signin_hwa()
        Hwa(self.driver, "JohnDoe@mail.com").search_hwa()
        time.sleep(1)
        Hwa(self.driver).delete_user_hwa()
        time.sleep(1)

    def delete_user_from_unit(self):
        start_locator = UNIT_USERS
        item_list = self.__wait.until(ec.visibility_of_all_elements_located((By.XPATH, start_locator)))
        for i in range(1, len(item_list) + 1):
            locator = f"{start_locator}[{i}]/child::div/child::div[3]"
            element = self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))
            if element.text == self.param[0]:
                locator = f"{start_locator}[{i}]/child::div/child::div[10]"
                self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
                self.__wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Yes, remove']"))).click()
                break

    def doorbell_button(self):
        Units(self.driver).select_building()
        time.sleep(1)
        Units(self.driver).select_unit()
        Units(self.driver).doorbell_tag()
        Units(self.driver).doorbell_item()

    def doorbell_tab(self):
        Units(self.driver).doorbell()

    def doorbell_layouts(self):
        i = 0
        while i < 2:
            Units(self.driver).check_button_layouts()
            i = i + 1

    def edit_card(self):
        Logout(self.driver).edit().click()
        self.edit_card_name()

    def edit_card_name(self):
        input_field = Logout(self.driver).card_name()
        input_field.send_keys(Keys.COMMAND, "a")
        input_field.send_keys(Keys.DELETE)
        input_field.send_keys("MyCard")
        Logout(self.driver).save_button().click()

    def edit_personal_info(self):
        firstname = self.param
        locator = "//span[text()='Edit Info']"
        self.__wait.until(ec.presence_of_element_located((By.XPATH, locator))).click()
        time.sleep(1)
        locator = "//input[@placeholder='Enter name']"
        search_field = self.driver.find_element(By.XPATH, locator)
        search_field.clear()
        search_field.send_keys(firstname)
        Logout(self.driver).save_button().click()

    def enter_building_settings(self):
        Units(self.driver).select_building().click()
        time.sleep(1)  # safari
        element = Buildings(self.driver).settings_tab()
        time.sleep(1)
        element.click()

    def enter_doorbell_um(self):
        doorbell = self.param
        Buildings(self.driver).doorbell_button().click()
        Buildings(self.driver, doorbell).select_doorbell().click()

    def enter_doorbell_unit_level(self):
        Buildings(self.driver).your_units_button().click()
        time.sleep(1)  # safari
        Buildings(self.driver).doorbell_button().click()
        Buildings(self.driver).select_doorbell().click()

    def enter_pin_code(self):
        pin_code = self.param
        Logout(self.driver).pin_code().send_keys(pin_code)
        Logout(self.driver).save_button().click()
        return pin_code

    # def edit_personal_info(self):
    #     self.profile_menu()
    #     Base(self.driver).edit_personal_info()

    def enable_search_field(self):
        self.enter_the_doorbell()
        Buildings(self.driver).enable_search()

    def enter_the_doorbell(self):
        Buildings(self.driver).your_buildings_button().click()
        Buildings(self.driver, BUILDING).select_building().click()
        time.sleep(1)
        element = Buildings(self.driver).doorbell_button()
        time.sleep(1)
        element.click()
        Buildings(self.driver, DOORBELL).select_doorbell().click()

    def enter_the_unit(self):
        unit = self.param[0]
        Units(self.driver).select_building().click()
        time.sleep(1)
        Units(self.driver, unit).select_unit().click()

    def find_popup(self):
        xpath = LOGOUT_MENU
        time.sleep(1)
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, xpath)))

    def fix_access_card(self):
        # Check and delete access card in profile menu
        Base(self.driver, START_LOGOUT_MENU[0], ACCESS_CARDS).profile_menu()
        time.sleep(1)
        if "CardName" in self.driver.page_source:
            self.__wait.until(ec.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(), 'CardName')]")))
            locator = "//div[@class='profile-cards-coll__rfid-name__text']/parent::div/following::i"
            element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
            if element.value_of_css_property('color') == 'rgba(0, 0, 0, 0)':
                element.click()
                time.sleep(1)
            Base(self.driver, "CardName").delete_card()
        # Check and delete SIMPLE USER access card
        Buildings(self.driver).your_buildings_button().click()
        Base(self.driver, UID).enter_the_unit()
        time.sleep(1)
        if SIMPLE_USER not in self.driver.page_source:
            Base(self.driver, SIMPLE_USER).link_unit()
            self.driver.get(BASE_URL)
            Base(self.driver, UID).enter_the_unit()
            time.sleep(1)
        Base(self.driver, SIMPLE_USER).select_user().click()
        Buildings(self.driver).access_cards_tag().click()
        time.sleep(1)
        if "CardName" in self.driver.page_source:
            Base(self.driver, "CardName").delete_card()

    def fix_your_units(self):
        if "Your units" not in self.driver.page_source:
            Base(self.driver, START_LOGOUT_MENU[0], UNITS).profile_menu()
            if UNIT in self.driver.page_source:
                Base(self.driver).check_unit_manager_active()
                time.sleep(1)
                Base(self.driver).check_unit_manager_active()
            elif "Myunit" in self.driver.page_source:
                Logout(self.driver).checkbox_unit_manager().click()
                Base(self.driver).check_unit_manager_active()
                self.driver.refresh()
                Buildings(self.driver).your_units_button().click()
                Units(self.driver).settings()
                Base(self.driver, UID, UNIT).change_unit_information()
            else:
                Base(self.driver, USERNAME_BA).link_unit()
                self.driver.get(BASE_URL)
                Base(self.driver, START_LOGOUT_MENU[0], UNITS).profile_menu()
                Logout(self.driver).checkbox_unit_manager().click()
                Base(self.driver).check_unit_manager_active()
        self.driver.refresh()

    def forbid_unit_image(self):
        self.enter_the_doorbell()
        Buildings(self.driver).forbid_upload_unit_image()
        time.sleep(1)
        return

    def hover_popup(self):  # hovering popup
        i = 0
        while i < 3:
            xpath = self.driver.find_element(By.XPATH, self.param[0][i])
            ActionChains(self.driver).move_to_element(xpath).perform()
            i = i + 1

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
        doorbell = Buildings(self.driver).doorbell_name()
        doorbell.click()
        doorbell.send_keys(Keys.HOME)
        time.sleep(1)
        doorbell.clear()
        doorbell.send_keys(self.param[0])
        save = Buildings(self.driver).save_button()
        if save.is_enabled() is True:
            save.click()
        time.sleep(1)
        return save.is_enabled()

    def input_card_info(self):
        card_number = self.param[1]
        card_name = self.param[0]
        element = Logout(self.driver).card_number()
        element.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        element.send_keys(card_number)
        element = Logout(self.driver).card_name()
        element.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        element.send_keys(card_name)

    def is_image_present(self):
        try:
            Units(self.driver).check_image_visibility()
            return True
        except Exception:
            return False

    def link_unit(self):
        Hwa(self.driver).signin_hwa()
        locator = f"//span[contains(text(), '{BUILDING}')]"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()  # select building
        Hwa(self.driver).apartment_management()
        # Select Unit
        locator = f"//input[@ng-reflect-model='{UID}']/following::p[1]"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        Hwa(self.driver, self.param[0]).add_existing_user()

    def logout(self):
        element = self.find_popup()
        time.sleep(1)
        element.click()
        Base(self.driver, START_LOGOUT_MENU[2], LOGOUT).logout_menu()

    def logout_menu(self):  # switch item in logout menu
        locator = self.__wait.until(ec.element_to_be_clickable((By.XPATH, self.param[0])))
        element = ActionChains(self.driver).move_to_element(locator)
        element.click().perform()

    def mark_unmark_unit_manager(self):
        i = 0
        while i < 4:
            element = Logout(self.driver).checkbox_unit_manager()
            time.sleep(1)
            element.click()
            time.sleep(1)
            i += 1

    def mark_unmark_digital_keys(self):
        self.profile_menu()
        i = 0
        while i < 3:
            Logout(self.driver).checkbox_digital_key().click()
            time.sleep(1)
            i += 1

    def mark_unmark_doorbel_button(self):
        self.profile_menu()
        i = 0
        while i < 3:
            Logout(self.driver).checkbox_doorbell_button().click()
            time.sleep(1)
            i += 1

    def mark_unit_manager(self):
        self.profile_menu()
        time.sleep(1)
        # Logout(self.driver).checkbox_unit_manager().click()
        # time.sleep(1)
        # Logout(self.driver).checkbox_unit_manager().click()
        # time.sleep(1)
        Base(self.driver).check_unit_manager_active()
        time.sleep(1)

    def popup_server(self):
        if server == 3:
            LoginPage(self.driver).change_server_Us_No().click()
        else:
            LoginPage(self.driver).change_server_No_Us().click()
        hidden_menu = self.driver.find_element(By.XPATH, self.param[0])
        ActionChains(self.driver).move_to_element(hidden_menu).click(hidden_menu).perform()
        time.sleep(1)
        if server == 3:
            self.driver.find_element(By.XPATH, SELECT_SERVER_EU)
        else:
            self.driver.find_element(By.XPATH, SELECT_SERVER_US)

    def press_button(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def profile_menu(self):
        self.find_popup().click()
        self.logout_menu()
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, self.param[1]))).click()

    def remove_user(self):
        self.profile_menu()
        Logout(self.driver).button_remove_user().click()
        Logout(self.driver).approve_remove().click()

    def remove_user_hwa(self):
        Hwa(self.driver).signin_hwa()
        Hwa(self.driver, self.param).signin_hwa()

    def restore_active_status(self):
        Hwa(self.driver).signin_hwa()
        Hwa(self.driver, self.param).search_hwa()
        Hwa(self.driver).delete_rfid_hwa()

    def restore_unit_owner(self):
        Buildings(self.driver).your_units_button().click()
        Buildings(self.driver).building_address()
        element = Units(self.driver).settings()
        time.sleep(1)
        element.click()
        Base(self.driver, USERNAME_UO).change_unit_owner()

    def restore_unit_manager(self):
        Buildings(self.driver).your_buildings_button().click()
        Base(self.driver, UID).enter_the_unit()
        Base(self.driver, USERNAME_UM).select_user().click()
        Logout(self.driver).units_tag().click()
        Base(self.driver).check_unit_manager_active()

    def scrolling(self):  # scrolling building addresses
        xpath_elements = self.param[0]
        status = self.param[1]
        elements = self.__wait.until(ec.presence_of_all_elements_located((By.XPATH, xpath_elements)))
        for i in range(len(elements)):
            if i == 0:
                xpath = xpath_elements
            else:
                xpath = f"{xpath_elements}[{i}]"
            if i < len(elements):
                xpath = self.__wait.until(ec.presence_of_element_located((By.XPATH, xpath)))
                if i < 10 and status == 1:
                    ActionChains(self.driver).move_to_element(xpath).perform()  # hovering
                else:
                    self.driver.execute_script("return arguments[0].scrollIntoView();", xpath)  # scrolling

    def select_always_allow(self):
        self.enter_the_doorbell()
        Buildings(self.driver).always_allow().click()
        time.sleep(1)

    def select_popup_lang(self):
        LoginPage(self.driver).search_lang().click()
        hidden_menu = self.driver.find_element(By.XPATH, self.param[0])
        time.sleep(0.5)
        ActionChains(self.driver).move_to_element(hidden_menu).click(hidden_menu).perform()
        return self.driver.find_element(By.XPATH, self.param[0])

    def select_never_allow(self):
        self.enter_the_doorbell()
        Buildings(self.driver).never_allow().click()
        time.sleep(1)
        return

    def select_schedule(self):
        self.enter_the_doorbell()
        Buildings(self.driver).schedule().click()
        time.sleep(1)
        return

    def select_user(self):
        locator = f"//span[contains(text(), '{self.param[0]}')]"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))

    def select_unit(self):
        if "Access" and "Doorbell" not in self.driver.page_source:
            Units(self.driver, self.param[0]).select_unit().click()

    def select_your_units(self):
        Buildings(self.driver).your_units_button().click()
        if "Users" and "Access" and 'Doorbell' not in self.driver.page_source:
            Base(self.driver, UNIT).select_unit()

    def set_schedule_and_day(self):
        self.select_schedule()
        Buildings(self.driver).set_up_custom_days().click()
        Buildings(self.driver).choose_day().click()
        Buildings(self.driver).ao_on()
        Buildings(self.driver).save_day_button().click()
        time.sleep(4)
        Buildings(self.driver).close_button().click()
        time.sleep(1)
        self.enter_doorbell_unit_level()

    def sorting(self):  # hovering and sorting
        sort_list = []
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, self.param[1])))
        time.sleep(0.5)  # safari
        element.click()
        time.sleep(1)
        sub_tag = self.param[2] + 1
        xpath_elements = self.param[0]
        elements = self.__wait.until(ec.presence_of_all_elements_located((By.XPATH, xpath_elements)))
        for i in range(1, len(elements)):
            xpath = f"{xpath_elements}[{i}]"
            element = self.driver.find_element(By.XPATH, f"{xpath}/child::div/child::div[{sub_tag}]")
            self.driver.find_element(By.XPATH, xpath)
            if element.text != "":
                if 'GID' and 'Number of users' in self.param[1] is True:
                    sort_list.append(len(element.text))
                elif self.param[0] == "//app-building-list-item":
                    sort_list.append(element.text[0])
                else:
                    sort_list.append(element.text)
                    # ActionChains(self.driver).move_to_element(item).perform()
        return sort_list

    def switch_to_lang(self):  # switch to lang in logout menu
        self.logout_menu()
        xpath = self.param[1]
        self.driver.find_element(By.XPATH, xpath).click()

    def units(self):
        self.profile_menu()

    def update_pin_code(self):
        Logout(self.driver).add_pin_code().click()
        return Base(self.driver, "111111111").enter_pin_code()

    def uncheck_user_image(self):
        self.enter_the_doorbell()
        Buildings(self.driver).uncheck_show_user_image().click()

    def uncheck_unit_image(self):
        self.enter_the_doorbell()
        Buildings(self.driver).uncheck_show_unit_image().click()

    def upload_image(self):
        Units(self.driver).doorbell_tag().click()
        Units(self.driver).doorbell().click()
        Units(self.driver).press_icon().click()
        mypath = Path("picture")
        path = mypath.home().joinpath("PycharmProjects", "WebAdminUi", "picture", "picture.jpeg")
        Units(self.driver).load_image().send_keys(str(path))
        time.sleep(1)
        Units(self.driver).save_image()
        time.sleep(1)
