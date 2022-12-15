import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from configuration import BASE_URL, USERNAME_UM, PASSWORD_UM, CODE, UNIT, UID, BUILDING, DOORBELL, server, USERNAME_UO, SIMPLE_USER
from pom.pages.code_page import CodePage
from pom.pages.login_page import LoginPage, SELECT_SERVER_US, SELECT_SERVER_EU
from pom.pages.logout_menu import Logout, START_LOGOUT_MENU, LOGOUT, UNITS, ACCESS_CARDS
from pom.pages.mainscreen_page import MainScreen
from pom.pages.your_units import Units
from pom.pages.your_building import Buildings
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
        self.search_login_field(self.username)
        self.search_password_field(self.password)
        try:
            self.__wait.until(ec.url_to_be(f"{BASE_URL}/auth-code"))
        except Exception:
            pass
        return self.driver.current_url

    def login_code(self):
        self.search_code_field(self.code)
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

    def access_tab(self):
        Units(self.driver).access()

    def add_card(self):
        Logout(self.driver).add_card()
        self.check_if_units_more_then_one()
        Logout(self.driver).input_card_number()
        Logout(self.driver).input_card_name()

    def add_pin_code(self):
        self.add_card()
        Logout(self.driver).add_pin_code()
        return Logout(self.driver, "22222222").enter_pin_code()

    def add_units(self):
        Logout(self.driver).add_card_button()
        if "Add unit" in self.driver.page_source:
            Logout(self.driver).add_units_button()
            Logout(self.driver).mark_unit()
            Logout(self.driver).save_unit_button()
            return True

    def add_user(self):
        Units(self.driver).add_user()
        Units(self.driver).fill_user_data_first_part()
        Units(self.driver).fill_user_data_phone()
        Units(self.driver).fill_user_data_second_part()

    def add_user_without_phone(self):
        Units(self.driver).add_user()
        Units(self.driver).fill_user_data_first_part()
        Units(self.driver).fill_user_data_second_part()

    def add_user_phone_with_spaces(self):
        Units(self.driver).add_user()
        Units(self.driver).fill_user_data_first_part()
        Units(self.driver).fill_user_data_phone_with_spaces()
        Units(self.driver).fill_user_data_second_part()

    def add_user_with_only_email(self):
        Units(self.driver).add_user()
        Units(self.driver).fill_email_data()
        Units(self.driver).fill_user_data_phone()
        Units(self.driver).fill_lang()

    def block_RFID_cards(self):
        i = 0
        while i < 3:
            Buildings(self.driver).block_adding_RFID_cards()
            time.sleep(1)
            i += 1
        Buildings(self.driver).pin_code_is_mandatory()

    def change_doorbell_name(self, browser):
        self.enter_the_doorbell()
        Buildings(self.driver, "My Doorbell Name").input_doorbell_name(browser)

    def change_unit_info(self):
        Units(self.driver).settings()

    def change_unit_info_ba(self):
        Units(self.driver).select_building()
        time.sleep(1)
        Units(self.driver).select_unit()
        time.sleep(1)
        Units(self.driver).settings()

    def change_unit_manager_role(self):
        Units(self.driver).select_building()
        Units(self.driver).settings()
        Units(self.driver).change_unit_manager()

    def check_add_user_function(self):
        Buildings(self.driver).add_user_function()
        self.logout()
        Signin(self.driver, USERNAME_UM, PASSWORD_UM, CODE).login_credentials()
        Signin(self.driver, USERNAME_UM, PASSWORD_UM, CODE).login_code()

    def check_add_role_unit_manager__function(self):
        Buildings(self.driver).add_role_unit_manager_function()
        self.logout()
        Signin(self.driver, USERNAME_UM, PASSWORD_UM, CODE).login_credentials()
        Signin(self.driver, USERNAME_UM, PASSWORD_UM, CODE).login_code()
        Units(self.driver).add_user()
        Units(self.driver).fill_user_data_first_part()
        Units(self.driver).fill_user_data_phone()
        Units(self.driver).fill_user_data_second_part()
        Units(self.driver).make_unit_manager()

        # Buildings(self.driver).RFID_cards_function()

    def check_change_unit_name_function(self):
        Buildings(self.driver).change_unit_name_function()
        self.logout()
        Signin(self.driver, USERNAME_UM, PASSWORD_UM, CODE).login_credentials()
        Signin(self.driver, USERNAME_UM, PASSWORD_UM, CODE).login_code()

    def checkbox_recovery(self):
        self.enter_the_doorbell()
        self.driver.refresh()
        time.sleep(1)
        Buildings(self.driver).checkbox_recovery_after_selection()

    def checkbox_settings(self):
        Buildings(self.driver).select_building()
        Buildings(self.driver).settings_tab()
        Buildings(self.driver).checkbox_recovery_settings()

    def check_doorbell_display_conditions(self):
        self.enter_the_doorbell()
        time.sleep(1)
        Buildings(self.driver).upload_unit_image()
        time.sleep(1)
        Buildings(self.driver).make_unit_image_visible()
        time.sleep(1)
        Buildings(self.driver).make_user_image_visible()
        time.sleep(1)
        Buildings(self.driver).allow_um_enable_ao()

    def check_if_units_more_then_one(self):
        if 'Add units' in self.driver.page_source:
            self.__wait.until(
                ec.element_to_be_clickable((By.XPATH, f"//button[contains(text(), 'Add units')]"))).click()
            time.sleep(1)
            self.__wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@class='form-checkbox__label']"))).click()
            self.__wait.until(
                ec.element_to_be_clickable((By.XPATH, "//button[text()=' Save ']/following::button[2]"))).click()

    def check_tips(self):
        MainScreen(self.driver).find_popup()
        self.logout_menu()
        Logout(self.driver).units_tag()

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

    def check_volume(self):
        move = ActionChains(self.driver)
        thumb = Buildings(self.driver).volume_thumb()
        move.click_and_hold(thumb).move_by_offset(100, 0).release().perform()
        move.click_and_hold(thumb).move_by_offset(10, 0).release().perform()

    def configure_ao(self):
        i = 0
        while i < 2:
            Units(self.driver).never_allow()
            time.sleep(1)
            Units(self.driver).always_allow()
            time.sleep(1)
            Units(self.driver).schedule()
            time.sleep(1)
            i += 1

    def delete_card(self):
        Logout(self.driver).delete()
        element = Logout(self.driver).remove_button()
        time.sleep(1)
        element.click()

    def delete_image(self):
        Units(self.driver).doorbell_tab()
        Units(self.driver).doorbell()
        time.sleep(1)
        xpath = Units(self.driver).choose_delete()
        ActionChains(self.driver).move_to_element(xpath).perform()
        xpath = Units(self.driver).delete_img()
        ActionChains(self.driver).move_to_element(xpath).click().perform()
        Units(self.driver).accept_delete()

    def delete_user(self):
        Hwa(self.driver).signin_hwa()
        Hwa(self.driver, "JohnDoe@mail.com").search_hwa()
        time.sleep(1)
        Hwa(self.driver).delete_user_hwa()
        time.sleep(1)

    def doorbell_button(self):
        Units(self.driver).select_building()
        time.sleep(1)
        Units(self.driver).select_unit()
        Units(self.driver).doorbell_button()
        Units(self.driver).doorbell_item()

    def doorbell_tab(self):
        Units(self.driver).doorbell()

    def doorbell_visibility(self):
        Units(self.driver).check_button_visibility()

    def doorbell_layouts(self):
        i = 0
        while i < 2:
            Units(self.driver).check_button_layouts()
            i = i + 1

    def edit_card(self):
        self.add_card()
        Logout(self.driver).edit()
        Logout(self.driver).edit_card_name()

    def enter_doorbell_um(self):
        doorbell = self.param
        Buildings(self.driver).doorbell_button()
        Buildings(self.driver, doorbell).select_doorbell()

    def edit_personal_info(self):
        self.profile_menu()
        Logout(self.driver).edit_personal_info()

    def enable_search_field(self):
        self.enter_the_doorbell()
        Buildings(self.driver).enable_search()

    def enter_building_settings(self):
        Units(self.driver).select_building()
        time.sleep(1)
        Buildings(self.driver).settings_tab()

    def enter_the_doorbell(self):
        Buildings(self.driver).your_buildings_button()
        Buildings(self.driver, BUILDING).select_building()
        Buildings(self.driver).doorbell_button()
        Buildings(self.driver, DOORBELL).select_doorbell()

    def enter_the_unit(self):
        Units(self.driver).select_building()
        time.sleep(1)
        Units(self.driver).select_unit()

    def fix_your_units(self):
        if "Your units" not in self.driver.page_source:
            Base(self.driver, START_LOGOUT_MENU[0], UNITS).profile_menu()
            if UNIT in self.driver.page_source:
                Logout(self.driver).mark_unit_manager()
                Logout(self.driver).check_unit_manager_active()
            elif "Myunit" in self.driver.page_source:
                Logout(self.driver).mark_unit_manager()
                Logout(self.driver).check_unit_manager_active()
                self.driver.refresh()
                Buildings(self.driver).your_units_button()
                Units(self.driver).settings()
                Buildings(self.driver, UNIT).change_unit_name()
            else:
                Base(self.driver, USERNAME_UM).link_unit()
                self.driver.get(BASE_URL)
                Base(self.driver, START_LOGOUT_MENU[0], UNITS).profile_menu()
                Logout(self.driver).mark_unit_manager()
                Logout(self.driver).check_unit_manager_active()
        self.driver.refresh()

    def fix_access_card(self):
        self.driver.refresh()
        Buildings(self.driver).your_buildings_button()
        Base(self.driver).enter_the_unit()
        Base(self.driver, SIMPLE_USER).select_user()
        Buildings(self.driver).access_cards()
        time.sleep(1)
        if "CardName" in self.driver.page_source:
            Base(self.driver, START_LOGOUT_MENU[0], ACCESS_CARDS).delete_card()

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

    def is_image_present(self):
        try:
            Units(self.driver).check_image_visibility()
            return True
        except Exception:
            return False

    def link_unit(self):
        Hwa(self.driver).signin_hwa()
        Hwa(self.driver, self.param[0]).search_hwa()
        Hwa(self.driver).building_address_um()
        Hwa(self.driver).manage_customers()
        self.__wait.until(ec.element_to_be_clickable(
            (By.XPATH, f"//span[contains(text(), '{BUILDING}')]"))).click()  # select building
        Hwa(self.driver).apartment_management()
        # Select Unit
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@ng-reflect-model='fortest']/following::p[1]"))).click()
        Hwa(self.driver).add_existing_user()

    def logout(self):
        MainScreen(self.driver).find_popup()
        Base(self.driver, START_LOGOUT_MENU[2], LOGOUT).logout_menu()

    def logout_menu(self):  # switch item in logout menu
        locator = self.__wait.until(ec.element_to_be_clickable((By.XPATH, self.param[0])))
        element = ActionChains(self.driver).move_to_element(locator)
        element.click().perform()

    def mark_unmark_unit_manager(self):
        self.profile_menu()
        i = 0
        while i < 3:
            Logout(self.driver).mark_unit_manager()
            time.sleep(1)
            i += 1

    def mark_unmark_digital_keys(self):
        self.profile_menu()
        i = 0
        while i < 3:
            Logout(self.driver).mark_digital_key()
            time.sleep(1)
            i += 1

    def mark_unmark_doorbel_button(self):
        self.profile_menu()
        i = 0
        while i < 3:
            Logout(self.driver).mark_doorbell_button()
            time.sleep(1)
            i += 1

    def mark_unit_manager(self):
        self.profile_menu()
        time.sleep(1)
        Logout(self.driver).mark_unit_manager()
        time.sleep(1)
        Logout(self.driver).check_unit_manager_active()

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
        MainScreen(self.driver).find_popup()
        self.logout_menu()
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, self.param[1]))).click()

    def remove_user(self):
        self.profile_menu()
        Logout(self.driver).button_remove_user()
        Logout(self.driver).approve_remove()

    def restore_active_status(self):
        Hwa(self.driver).signin_hwa()
        Hwa(self.driver, self.param).search_hwa()
        Hwa(self.driver).delete_rfid_hwa()

    def restore_unit_owner(self):
        Buildings(self.driver).your_units_button()
        Buildings(self.driver).building_address()
        Units(self.driver).settings()
        Units(self.driver, USERNAME_UO).change_unit_owner()
        time.sleep(1)

    def remove_user_hwa(self):
        Hwa(self.driver).signin_hwa()
        Hwa(self.driver, self.param).signin_hwa()

    def remove_buttons(self):
        self.enter_the_doorbell()
        Buildings(self.driver).remove_buttons_from_doorbell()

    def select_popup_lang(self):
        LoginPage(self.driver).search_lang().click()
        hidden_menu = self.driver.find_element(By.XPATH, self.param[0])
        time.sleep(0.5)
        ActionChains(self.driver).move_to_element(hidden_menu).click(hidden_menu).perform()
        return self.driver.find_element(By.XPATH, self.param[0])

    def select_never_allow(self):
        self.enter_the_doorbell()
        Buildings(self.driver).never_allow()
        time.sleep(1)
        return

    def select_always_allow(self):
        self.enter_the_doorbell()
        Buildings(self.driver).always_allow()
        time.sleep(1)
        return

    def select_schedule(self):
        self.enter_the_doorbell()
        Buildings(self.driver).schedule()
        time.sleep(1)
        return

    def select_user(self):
        locator = f"//span[contains(text(), '{self.param[0]}')]"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def select_your_units(self):
        Buildings(self.driver).your_units_button()
        if "Users" and "Access" and 'Doorbell' not in self.driver.page_source:
            Base(self.driver, UNIT).select_unit()

    def select_unit(self):
        self.driver.find_element(By.XPATH, f"//span[contains(text(), '{self.param}')]").click()

    def scrolling(self):  # scrolling building addresses
        xpath_elements = self.param[0]
        elements = self.driver.find_elements(By.XPATH, xpath_elements)
        for i in range(len(elements) + 1):
            if i == 0:
                xpath = xpath_elements
            else:
                xpath = f"{xpath_elements}[{i}]"
            if i % 5 == 0 or i < len(elements):
                xpath = self.__wait.until(ec.presence_of_element_located((By.XPATH, xpath)))
                if i < 10:
                    ActionChains(self.driver).move_to_element(xpath).perform()  # hovering
                else:
                    self.driver.execute_script("return arguments[0].scrollIntoView();", xpath)  # scrolling

    def sorting(self):  # hovering and sorting
        sort_list = []
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, self.param[1])))
        time.sleep(0.5)
        element.click()
        time.sleep(1)
        sub_tag = self.param[2] + 1
        xpath_elements = self.param[0]
        elements = self.driver.find_elements(By.XPATH, xpath_elements)
        for i in range(1, len(elements)):
            # if i > 8:
            #     break
            # else:
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

    def set_schedule_and_day(self):
        self.select_schedule()
        Buildings(self.driver).set_up_custom_days()
        Buildings(self.driver).choose_day()
        Buildings(self.driver).ao_on()
        Buildings(self.driver).save_day()
        self.driver.refresh()
        Buildings(self.driver, DOORBELL).enter_doorbell_unit_level()

    def units(self):
        self.profile_menu()

    def update_pin_code(self):
        Logout(self.driver).add_pin_code()
        return Logout(self.driver, "111111111").enter_pin_code()

    def uncheck_user_image(self):
        self.enter_the_doorbell()
        Buildings(self.driver).uncheck_show_user_image()

    def uncheck_unit_image(self):
        self.enter_the_doorbell()
        Buildings(self.driver).uncheck_show_unit_image()

    def upload_image(self):
        Units(self.driver).doorbell_tab()
        Units(self.driver).doorbell()
        Units(self.driver).press_icon()
        mypath = Path("picture")
        path = mypath.home().joinpath("PycharmProjects", "WebAdminUi", "picture", "picture.jpeg")
        Units(self.driver).load_image().send_keys(str(path))
        time.sleep(1)
        Units(self.driver).save_image()
        time.sleep(1)
