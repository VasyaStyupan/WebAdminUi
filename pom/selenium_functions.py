import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from configuration import BASE_URL, USERNAME_UM, PASSWORD_UM, CODE, UNIT, UID, BUILDING
from pom.pages.code_page import CodePage
from pom.pages.login_page import LoginPage, SELECT_SERVER_US
from pom.pages.logout_menu import Logout, START_LOGOUT_MENU, LOGOUT, ACCESS_CARDS
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
            time.sleep(1)
        except Exception:
            pass
        return self.driver.current_url


class Base(LoginPage):
    def __init__(self, driver, xpath, *xpath1):
        super().__init__(driver)
        self.__wait = WebDriverWait(driver, 10, 0.3)
        self.driver = driver
        self.xpath = xpath
        self.xpath1 = xpath1
        self.xpath2 = xpath1

    def add_units(self):
        Logout(self.driver).add_card_button()
        Logout(self.driver).add_units_button()
        Logout(self.driver).mark_unit()
        Logout(self.driver).save_unit_button()

    def add_card(self):
        Logout(self.driver).add_card()
        self.check_if_units_more_then_one()
        Logout(self.driver).input_card_number()
        Logout(self.driver).input_card_name()

    def add_pin_code(self):
        self.add_card()
        Logout(self.driver).add_pin_code()
        return Logout(self.driver, "22222222").enter_pin_code()

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

    def delete_card(self):
        Logout(self.driver).delete()
        Logout(self.driver).remove_button().click()

    def edit_card(self):
        self.add_card()
        Logout(self.driver).edit()
        Logout(self.driver).edit_card_name()

    def edit_personal_info(self):
        self.profile_menu()
        time.sleep(1)
        Logout(self.driver).edit_personal_info()

    def enter_doorbell_um(self):
        doorbell = self.xpath
        Buildings(self.driver).doorbell_button()
        Buildings(self.driver, doorbell).select_doorbell()

    def hover(self):  # hovering and sorting
        self.__wait.until(ec.presence_of_element_located((By.XPATH, self.xpath1[1]))).click()
        if len(self.xpath1) == 2:
            index = 0
        else:
            index = self.xpath1[2]
        xpath_elements = self.xpath
        elements = self.driver.find_elements(By.XPATH, xpath_elements)
        items_list = []
        for i in range(len(elements)):
            if i == 0:
                xpath = xpath_elements
            elif i > 7:
                break
            else:
                xpath = f"{xpath_elements}{self.xpath1[0]}[{i}]/div"
            xpath = self.driver.find_element(By.XPATH, xpath)
            items_list.append(xpath.text.split()[index])
            ActionChains(self.driver).move_to_element(xpath).perform()
        del items_list[0:10]
        return items_list

    def hover_popup(self):  # hovering popup
        i = 0
        while i < 3:
            xpath = self.driver.find_element(By.XPATH, self.xpath[i])
            ActionChains(self.driver).move_to_element(xpath).perform()
            i = i + 1

    def logout_menu(self):  # switch item in logout menu
        locator = self.driver.find_element(By.XPATH, self.xpath)
        ActionChains(self.driver).move_to_element(locator).click().perform()

    def link_unit(self):
        Hwa(self.driver).signin_hwa()
        Hwa(self.driver, self.xpath).search_hwa()
        building_address = Hwa(self.driver).building_address_um()
        # building = building_address.text
        # uid = Hwa(self.driver).unit_uid().text
        Hwa(self.driver).manage_customers()
        self.driver.find_element(By.XPATH, f"//span[contains(text(), '{BUILDING}')]").click()  # select building
        Hwa(self.driver).apartment_management()
        j = 0  # Select Unit
        for i in Hwa(self.driver).find_by_uid():
            if i.get_attribute('ng-reflect-model') == UID:
                locator = f"//p[@class='add_user']/following::p[{j}]"
                self.driver.find_element(By.XPATH, locator).click()
                break
            j = j + 1
        Hwa(self.driver).add_existing_user()

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

    def mark_unmark_unit_manager(self):
        self.profile_menu()
        time.sleep(1)
        Logout(self.driver).mark_unit_manager()
        time.sleep(1)
        Logout(self.driver).mark_unit_manager()

    def mark_unit_manager(self):
        self.profile_menu()
        time.sleep(1)
        Logout(self.driver).mark_unit_manager()

    def popup_server(self):
        LoginPage(self.driver).change_server_No_Us().click()
        hidden_menu = self.driver.find_element(By.XPATH, self.xpath)
        ActionChains(self.driver).move_to_element(hidden_menu).click(hidden_menu).perform()
        return self.driver.find_element(By.XPATH, SELECT_SERVER_US)

    def press_button(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def profile_menu(self):
        MainScreen(self.driver).find_popup()
        self.logout_menu()
        self.driver.find_element(By.XPATH, self.xpath1[0]).click()

    def remove_user(self):
        self.profile_menu()
        Logout(self.driver).button_remove_user()
        Logout(self.driver).approve_remove()

    def restore_active_status(self):
        Hwa(self.driver).signin_hwa()
        Hwa(self.driver, self.xpath).search_hwa()
        Hwa(self.driver).delete_rfid_hwa()

    def remove_user_hwa(self):
        Hwa(self.driver).signin_hwa()
        Hwa(self.driver, self.xpath).signin_hwa()

    def select_popup_lang(self):
        LoginPage(self.driver).search_lang().click()
        hidden_menu = self.driver.find_element(By.XPATH, self.xpath)
        ActionChains(self.driver).move_to_element(hidden_menu).click(hidden_menu).perform()
        return self.driver.find_element(By.XPATH, self.xpath)

    def select_unit(self):
        self.driver.find_element(By.XPATH, f"//span[contains(text(), '{self.xpath}')]").click()

    def scrolling(self):  # scrolling building addresses
        xpath_elements = self.xpath
        elements = self.driver.find_elements(By.XPATH, xpath_elements)
        for i in range(len(elements)):
            if i == 0:
                xpath = xpath_elements
            else:
                xpath = f"{xpath_elements}/following::app-building-list-item[{i}]/div"

            if i % 5 == 0 or i < len(elements):
                xpath = self.driver.find_element(By.XPATH, xpath)
                ActionChains(self.driver).move_to_element(xpath).perform()

    def switch_to_lang(self):  # switch to lang in logout menu
        self.logout_menu()
        xpath = self.xpath1[0]
        self.driver.find_element(By.XPATH, xpath).click()

    def units(self):
        self.profile_menu()


class Base2(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def access_tab(self):
        Units(self.driver).access()

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

    def change_unit_info(self):
        Units(self.driver).settings()

    def change_unit_info_ba(self):
        Units(self.driver).select_building()
        time.sleep(1)
        Units(self.driver).select_unit()
        Units(self.driver).settings()

    def change_unit_manager_role(self):
        Units(self.driver).select_building()
        Units(self.driver).settings()
        Units(self.driver).change_unit_manager()

    def change_doorbell_name(self):
        doorbell = self.enter_the_doorbell()
        Buildings(self.driver, "My Doorbell Name").input_doorbell_name()
        return doorbell

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

    def check_add_user_function(self):
        Buildings(self.driver).add_user_function()
        self.logout()
        Signin(self.driver, USERNAME_UM, PASSWORD_UM, CODE).login_credentials()
        Signin(self.driver, USERNAME_UM, PASSWORD_UM, CODE).login_code()

    def check_change_unit_name_function(self):
        Buildings(self.driver).change_unit_name_function()
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

    def checkbox_recovery(self):
        self.enter_the_doorbell()
        time.sleep(1)
        Buildings(self.driver).checkbox_recovery_after_selection()

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

    def doorbell_button(self):
        Units(self.driver).select_building()
        time.sleep(1)
        Units(self.driver).select_unit()
        Units(self.driver).doorbell_button()
        Units(self.driver).doorbell_item()

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
        Hwa(self.driver).delete_user_hwa()
        time.sleep(1)

    def doorbell_tab(self):
        Units(self.driver).doorbell()

    def doorbell_visibility(self):
        Units(self.driver).check_button_visibility()

    def doorbell_layouts(self):
        i = 0
        while i < 2:
            Units(self.driver).check_button_layouts()
            i = i + 1

    def enter_the_unit(self):
        Units(self.driver).select_building()
        time.sleep(1)
        Units(self.driver).select_unit()

    def enter_the_user(self):
        self.enter_the_unit()
        Units(self.driver).select_user()

    def enter_the_doorbell(self):
        doorbell, address = Base2(self.driver).find_doorbell()
        Buildings(self.driver, address).select_building()
        Buildings(self.driver).doorbell_button()
        Buildings(self.driver, doorbell).select_doorbell()
        return doorbell

    def enable_search_field(self):
        self.enter_the_doorbell()
        Buildings(self.driver).enable_search()

    def enter_building_settings(self):
        Units(self.driver).select_building()
        Buildings(self.driver).settings_tab()

    def find_doorbell(self):
        Buildings(self.driver).your_units_button()
        address, unit = Buildings(self.driver).building_address()
        self.driver.find_elements(By.XPATH, f"//div[contains(text(), '{address}')]")[0].click()
        self.driver.find_elements(By.XPATH, f"//span[contains(text(), '{unit}')]")[0].click()
        self.driver.find_elements(By.XPATH, "//div[contains(text(), ' Doorbell ')]")[0].click()
        doorbell = self.driver.find_elements(By.XPATH, "//div[@class='table-list-item__coll']")[0].text
        self.driver.get(f"{BASE_URL}/building/list")
        return doorbell, address

    def forbid_unit_image(self):
        doorbell = self.enter_the_doorbell()
        Buildings(self.driver).forbid_upload_unit_image()
        time.sleep(1)
        return doorbell

    def is_image_present(self):
        try:
            Units(self.driver).check_image_visibility()
            return True
        except NoSuchElementException:
            return False

    def logout(self):
        MainScreen(self.driver).find_popup()
        Base(self.driver, START_LOGOUT_MENU[2], LOGOUT).logout_menu()

    def remove_buttons(self):
        self.enter_the_doorbell()
        Buildings(self.driver).remove_buttons_from_doorbell()

    def select_never_allow(self):
        doorbell = self.enter_the_doorbell()
        Buildings(self.driver).never_allow()
        time.sleep(1)
        return doorbell

    def select_always_allow(self):
        doorbell = self.enter_the_doorbell()
        Buildings(self.driver).always_allow()
        time.sleep(1)
        return doorbell

    def select_schedule(self):
        doorbell = self.enter_the_doorbell()
        Buildings(self.driver).schedule()
        time.sleep(1)
        return doorbell

    def select_your_units(self):
        Buildings(self.driver).your_units_button()
        if "Users" and "Access" and 'Doorbell' not in self.driver.page_source:
            Base(self.driver, UNIT).select_unit()

    def set_schedule_and_day(self):
        doorbell = self.select_schedule()
        Buildings(self.driver).set_up_custom_days()
        Buildings(self.driver).choose_day()
        Buildings(self.driver).ao_on()
        Buildings(self.driver).save_day()
        self.driver.refresh()
        Buildings(self.driver, doorbell).enter_doorbell_unit_level()

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

    def uncheck_user_image(self):
        self.enter_the_doorbell()
        Buildings(self.driver).uncheck_show_user_image()

    def uncheck_unit_image(self):
        self.enter_the_doorbell()
        Buildings(self.driver).uncheck_show_unit_image()
