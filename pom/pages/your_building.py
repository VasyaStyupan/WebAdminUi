import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Buildings:
    def __init__(self, driver, *param):
        self.param = param
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3)

    def settings_tab(self):
        locator = "//div[text()=' Settings ']"
        return self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def unit_manager_functions(self):
        locator = "//div[text()=' Add a user ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        time.sleep(1)
        locator = "//div[text()=' Change unit name ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        time.sleep(1)
        locator = "//div[text()=' Add the role of unit manager to another user ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        time.sleep(1)
        locator = "//div[text()=' Administrate users RFID cards ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def change_list_of_floors(self):
        floors_number = self.param
        locator = "//input[@placeholder='Enter number']"
        input_floors = self.__wait.until(ec.presence_of_element_located((By.XPATH, locator)))
        input_floors.send_keys(Keys.COMMAND, "a")
        input_floors.send_keys(floors_number)
        input_floors.send_keys(Keys.RETURN)
        # locator = "//button[text()=' List of floors ']"
        # self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        # locator = "//button[@class='close-btn']"
        # self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def select_building(self):
        address = self.param[0]
        self.driver.find_element(By.XPATH, f"//span[contains(text(), '{address}')]").click()

    def select_doorbell(self):
        doorbell = self.param[0]
        print(doorbell)
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{doorbell}')]")))
        element.click()

    def doorbell_button(self):
        locator = "//div[text()=' Doorbell ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()

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
        doorbell = self.driver.find_element(By.XPATH, locator)
        doorbell.send_keys(Keys.COMMAND, "a")
        doorbell.send_keys(self.param[0])
        locator = "//button[text()=' Save ']"
        self.driver.find_element(By.XPATH, locator).click()

    def enable_search(self):
        locator = "//div[text()=' Enable search field ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()
        self.driver.refresh()

    def remove_buttons_from_doorbell(self):
        locator = "//div[text()=' Remove all buttons from the doorbell ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()
        self.driver.refresh()

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

    def forbid_upload_unit_image(self):
        locator = "//div[text()=' Upload unit image ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()

    def make_unit_image_visible(self):
        locator = "//div[text()=' Make unit image visible ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()

    def make_user_image_visible(self):
        locator = "//div[text()=' Make user image visible ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()

    def allow_um_enable_ao(self):
        locator = "//div[text()=' Allow unit manager to enable automatic opening ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()
        time.sleep(1)

    def never_allow(self):
        locator = "//div[text()=' Never allow ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def always_allow(self):
        locator = "//div[text()=' Always allow ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def schedule(self):
        locator = "//div[text()=' Schedule ']"
        self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator))).click()

    def your_units_button(self):
        locator = "//button[text()=' Your units ']"
        element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        time.sleep(1)
        element.click()

    def building_address(self):
        locator = "//div[@class='breadcrumbs__btn']"
        address = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        locator = "//div[@class='section-entity-name']"
        unit = self.__wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        return address.text[8:], unit.text

    def enter_doorbell_unit_level(self):
        self.your_units_button()
        self.doorbell_button()
        self.select_doorbell()

    def user_image_disabled(self):
        locator = "//div[text()=' Visible ']"
        element = self.driver.find_element(By.XPATH, locator)
        time.sleep(1)
        element.click()

    def unit_image_disabled(self):
        locator = "//div[text()=' Visible ']/following::label[1]"
        element = self.driver.find_element(By.XPATH, locator)
        time.sleep(1)
        element.click()


