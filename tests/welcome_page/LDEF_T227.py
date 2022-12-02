import time

import allure
from pom.pages.login_page import SELECT_SERVER_US, SELECT_SERVER_EU
from pom.selenium_functions import Base
from configuration import LOGIN_URL_US


@allure.title("Change server No/Us")
def test_case(setup):
    """
    Check if server can switch from No to Us
    """
    Base(setup, SELECT_SERVER_US).popup_server()
    time.sleep(1)
    with allure.step("Step 1. Change server to US"):
        assert setup.current_url == LOGIN_URL_US, "Can`t change server to US"
