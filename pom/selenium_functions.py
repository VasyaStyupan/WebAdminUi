import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from configuration import BASE_URL, USERNAME_UM, PASSWORD_UM, CODE
from pom.pages.code_page import CodePage
from pom.pages.login_page import LoginPage, SELECT_SERVER_US
from pom.pages.logout_menu import ADD_CARD, Logout, START_LOGOUT_MENU
from pom.pages.mainscreen_page import MainScreen
from pom.pages.your_units import Units
from pom.pages.your_building import Buildings
from pom.pages.hwa import Hwa


class Signin(LoginPage, CodePage):
    def __init__(self, driver, username, password, code):
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

    def select_popup_lang(self):
        LoginPage(self.driver).search_lang().click()
        hidden_menu = self.driver.find_element(By.XPATH, self.xpath)
        ActionChains(self.driver).move_to_element(hidden_menu).click(hidden_menu).perform()
        return self.driver.find_element(By.XPATH, self.xpath)

    def popup_server(self):
        LoginPage(self.driver).change_server_No_Us().click()
        hidden_menu = self.driver.find_element(By.XPATH, self.xpath)
        ActionChains(self.driver).move_to_element(hidden_menu).click(hidden_menu).perform()
        return self.driver.find_element(By.XPATH, SELECT_SERVER_US)

    def hover(self):  # hovering building addresses
        MainScreen(self.driver).press_sorting_button()
        xpath_elements = self.xpath
        elements = self.driver.find_elements(By.XPATH, xpath_elements)
        first_letter_list = []
        for i in range(len(elements)):
            if i == 0:
                xpath = xpath_elements
            else:
                xpath = f"{xpath_elements}/following::app-building-list-item[{i}]/div"
            xpath = self.driver.find_element(By.XPATH, xpath)
            first_letter_list.append(xpath.text[0])
            first_letter_list[i] = xpath.text[0]
            ActionChains(self.driver).move_to_element(xpath).perform()
        del first_letter_list[0:1]
        return first_letter_list

    def scrolling(self):  # scrolling building addresse
        xpath_elements = self.xpath
        elements = self.driver.find_elements(By.XPATH, xpath_elements)
        for i in range(len(elements)):
            if i == 0:
                xpath = xpath_elements
            else:
                xpath = f"{xpath_elements}/following::app-building-list-item[{i}]/div"
            xpath = self.driver.find_element(By.XPATH, xpath)
            if i % 5 == 0 or i == len(elements) - 1:
                ActionChains(self.driver).move_to_element(xpath).perform()

    def hover_popup(self):  # hovering popup
        i = 0
        while i < 3:
            xpath = self.driver.find_element(By.XPATH, self.xpath[i])
            ActionChains(self.driver).move_to_element(xpath).perform()
            i = i + 1

    def logout_menu(self):  # switch item in logout menu
        xpath = self.driver.find_element(By.XPATH, self.xpath)
        ActionChains(self.driver).move_to_element(xpath).click().perform()

    def switch_to_lang(self):  # switch to lang in logout menu
        self.logout_menu()
        xpath = self.xpath1[0]
        self.driver.find_element(By.XPATH, xpath).click()

    def press_button(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def profile_menu(self):
        MainScreen(self.driver).find_popup().click()
        self.logout_menu()
        self.driver.find_element(By.XPATH, self.xpath1[0]).click()

    def add_card(self):
        self.press_button(ADD_CARD)
        Logout(self.driver).input_card_number()
        Logout(self.driver).input_card_name()

    def add_pin_code(self, xpath):
        self.profile_menu()
        self.add_card()
        self.driver.find_element(By.XPATH, xpath).click()
        Logout(self.driver).enter_pin_code()

    def delete_card(self):
        Logout(self.driver).delete()
        Logout(self.driver).remove_button().click()

    def edit_card(self):
        self.add_card()
        Logout(self.driver).edit()
        Logout(self.driver).edit_card_name()

    def units(self):
        self.profile_menu()

    def mark_unmark_digital_keys(self):
        self.profile_menu()
        time.sleep(1)
        Logout(self.driver).mark_digital_key()
        time.sleep(1)
        Logout(self.driver).mark_digital_key()

    def mark_unmark_doorbel_button(self):
        self.profile_menu()
        time.sleep(1)
        Logout(self.driver).mark_doorbell_button()
        time.sleep(1)
        Logout(self.driver).mark_doorbell_button()

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

    def remove_user(self):
        self.profile_menu()
        Logout(self.driver).button_remove_user()
        Logout(self.driver).approve_remove()

    def edit_personal_info(self):
        self.profile_menu()
        time.sleep(1)
        Logout(self.driver).edit_personal_info(self.xpath1)

    def check_tips(self):
        MainScreen(self.driver).find_popup().click()
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

    def add_units(self):
        Logout(self.driver).add_card_button()
        Logout(self.driver).add_units_button()
        Logout(self.driver).mark_unit()
        # time.sleep(1)
        Logout(self.driver).save_unit_button()

    def restore_active_status(self):
        Hwa(self.driver).signin_hwa()
        Hwa(self.driver, self.xpath).search_hwa()
        Hwa(self.driver).delete_rfid_hwa()

    def remove_user_hwa(self):
        Hwa(self.driver).signin_hwa()
        Hwa(self.driver, self.xpath).signin_hwa()

    def link_unit(self):
        Hwa(self.driver).signin_hwa()
        Hwa(self.driver, self.xpath).search_hwa()
        building_address = Hwa(self.driver).building_address_um()
        building = building_address.text
        first_name = Hwa(self.driver).firstname_um()
        first_name = first_name.get_attribute('value')
        last_name = Hwa(self.driver).lastname_um()
        last_name = last_name.get_attribute('value')
        print(first_name, last_name)
        # building_ui = Hwa(self.driver).building_uid()
        # j = 0
        # for i in building_ui:
        #     j = j + 1
        Hwa(self.driver).manage_customers()
        j = 0
        for i in Hwa(self.driver).building_address_ba():
            j = + 1
            locator = f"//span[@tabindex='0']/following::span[{j}]"
            if i.text == building:
                self.driver.find_element(By.XPATH, locator).click()
                break
        Hwa(self.driver).apartment_management()
        j = 0
        for i in Hwa(self.driver).find_by_uid():
            if first_name and last_name in i.text:
                locator = f"//p[@class='add_user']/following::p[{j}]"
                self.driver.find_element(By.XPATH, locator).click()
                break
            j = j + 1
        Hwa(self.driver).add_existing_user()


class Base2(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def upload_image(self):
        Units(self.driver).doorbell_tab()
        Units(self.driver).doorbell()
        Units(self.driver).press_icon()
        time.sleep(1)
        Units(self.driver).load_image().send_keys("/Users/StyupanVasyl/Downloads/picture.jpeg")
        time.sleep(1)
        Units(self.driver).save_image()

    def delete_image(self):
        Units(self.driver).doorbell_tab()
        Units(self.driver).doorbell()
        time.sleep(1)
        xpath = Units(self.driver).choose_delete()
        ActionChains(self.driver).move_to_element(xpath).perform()
        xpath = Units(self.driver).delete_img()
        ActionChains(self.driver).move_to_element(xpath).click().perform()
        Units(self.driver).accept_delete()

    def access_tab(self):
        Units(self.driver).access()

    def doorbell_tab(self):
        Units(self.driver).doorbell()

    def configure_ao(self):
        Units(self.driver).never_allow()
        time.sleep(1)
        Units(self.driver).use_schedule()
        time.sleep(1)
        Units(self.driver).make_schedule()
        time.sleep(1)

    def change_unit_info(self):
        Units(self.driver).select_building()
        time.sleep(1)
        Units(self.driver).select_unit()
        Units(self.driver).settings()

    def change_unit_manager_role(self):
        Units(self.driver).select_building()
        Units(self.driver).settings()
        Units(self.driver).change_unit_manager()

    def enter_the_unit(self):
        Units(self.driver).select_building()
        time.sleep(1)
        Units(self.driver).select_unit()

    def find_doorbell(self):
        Buildings(self.driver).your_units_button()
        address, unit = Buildings(self.driver).building_address()
        self.driver.find_elements(By.XPATH, f"//div[contains(text(), '{address}')]")[0].click()
        self.driver.find_elements(By.XPATH, f"//span[contains(text(), '{unit}')]")[0].click()
        self.driver.find_elements(By.XPATH, "//div[contains(text(), ' Doorbell ')]")[0].click()
        doorbell = self.driver.find_elements(By.XPATH, "//div[@class='table-list-item__coll']")[0].text
        self.driver.get(f"{BASE_URL}/building/list")
        return doorbell, address

    def enter_the_doorbell(self):
        doorbell, address = Base2(self.driver).find_doorbell()
        Buildings(self.driver, address).select_building()
        Buildings(self.driver).doorbell_button()
        Buildings(self.driver, doorbell).select_doorbell()
        return doorbell

    def change_doorbell_name(self):
        doorbell = self.enter_the_doorbell()
        Buildings(self.driver, "My Doorbell Name").input_doorbell_name()
        return doorbell

    def enable_search_field(self):
        self.enter_the_doorbell()
        Buildings(self.driver).enable_search()

    def remove_buttons(self):
        self.enter_the_doorbell()
        Buildings(self.driver).remove_buttons_from_doorbell()

    def uncheck_user_image(self):
        self.enter_the_doorbell()
        Buildings(self.driver).uncheck_show_user_image()

    def uncheck_unit_image(self):
        self.enter_the_doorbell()
        Buildings(self.driver).uncheck_show_unit_image()

    def forbid_unit_image(self):
        self.enter_the_doorbell()
        Buildings(self.driver).forbid_upload_unit_image()

    def check_doorbell_display_conditions(self):
        self.enter_the_doorbell()
        Buildings(self.driver).make_unit_image_visible()
        Buildings(self.driver).make_user_image_visible()
        Buildings(self.driver).allow_um_enable_ao()

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
        self.enter_the_doorbell()
        Buildings(self.driver).schedule()
        time.sleep(1)

    def add_user(self):
        self.enter_the_unit()
        Units(self.driver).add_user()
        Units(self.driver).fill_user_data()

    def doorbell_button(self):
        Units(self.driver).select_building()
        time.sleep(1)
        Units(self.driver).select_unit()
        Units(self.driver).doorbell_button()
        Units(self.driver).doorbell_item()

    def doorbell_visibility(self):
        Units(self.driver).check_button_visibility()

    def doorbell_layouts(self):
        Units(self.driver).check_button_layouts()

    def is_image_present(self):
        try:
            Units(self.driver).check_image_visibility()
            return True
        except NoSuchElementException:
            return False

    def enter_building_settings(self):
        Units(self.driver).select_building()
        Buildings(self.driver).settings_tab()

    def check_um_functions(self):
        i = 0
        while i < 2:
            Buildings(self.driver).unit_manager_functions()
            i = i + 1
