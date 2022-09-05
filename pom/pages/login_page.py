from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from configuration import LOGIN_URL


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(LOGIN_URL)

    def search_login_fields(self, username, password):
        search_field = self.driver.find_element(By.XPATH, "/html/body/app-root/app-auth-host/div[2]/app-login/"
                                                          "div/form/div[1]/div/app-form-input/input")
        search_field.send_keys(username)
        search_field = self.driver.find_element(By.XPATH, "/html/body/app-root/app-auth-host/div[2]/app-login/"
                                                          "div/form/div[2]/div/app-form-input/input")
        search_field.send_keys(password)
        return search_field.send_keys(Keys.RETURN)

    def search_privacy(self):
        return self.driver.find_element(By.XPATH, "/html/body/app-root/app-auth-host/div[3]/div/p/a[1]")

    def search_terms(self):
        return self.driver.find_element(By.XPATH, "/html/body/app-root/app-auth-host/div[3]/div/p/a[2]")

    def search_contact(self):
        return self.driver.find_element(By.XPATH, "/html/body/app-root/app-auth-host/div[3]/p[2]/a")

    def change_server_No_Us(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/app-root/app-auth-host/div[1]/div[3]/app-server-switch/div[1]")

    def select_server_US(self):
        return "/html/body/app-root/app-auth-host/div[1]/div[3]/app-server-switch/div[2]/div[1]"

    def set_server_US(self):
        return "/html/body/app-root/app-auth-host/div[1]/div[3]/app-server-switch/div[1]/div[2]/span"

    def search_lang(self):
        return self.driver.find_element(By.XPATH, "/html/body/app-root/app-auth-host/div[1]/div[3]/app-language-switch/"
                                                  "div[1]/div[2]/span")

    def change_lang_to_norsk(self):
        return "/html/body/app-root/app-auth-host/div[1]/div[3]/app-language-switch/div[2]/div[2]"

    def change_lang_to_svenska(self):
        return "/html/body/app-root/app-auth-host/div[1]/div[3]/app-language-switch/div[2]/div[3]"

    def change_lang_to_english(self):
        return "/html/body/app-root/app-auth-host/div[1]/div[3]/app-language-switch/div[2]/div[1]"
