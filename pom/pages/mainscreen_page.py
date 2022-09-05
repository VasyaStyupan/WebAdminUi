from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainScreen:
    def __init__(self, driver, *search_word):
        self.driver = driver
        self.word = search_word

    def search_bar(self):
        search = self.driver.find_element(By.XPATH, "/html/body/app-root/app-building-host/app-admin-header/div[1]"
                                                    "/div[3]/app-admin-search/app-search-field/div/input")
        search.send_keys(self.word)
        return search.send_keys(Keys.RETURN)

    def search_user(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/app-root/app-building-host/main/app-search/div/div[2]/div/div/div[2]")

    def search_building_address(self):
        return "/html/body/app-root/app-building-host/main/app-unit-host/div/div[2]/app-unit-users-list/div/div/app-unit-users-list-item[1]"
