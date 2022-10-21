import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.logout_menu import ACCESS_CARDS, START_LOGOUT_MENU
import time


@allure.title("View empty screen Access Cards")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Profile/Access cards] View empty screen Access Cards
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).profile_menu()
    time.sleep(1)
    with allure.step("Step 1. Check presence of necessary tags and fields"):
        assert "Personal info" and "Units" and "Access Cards" and "Reset Password" in setup.page_source, "Required tags are missing"
        assert "UID" and "Units" and "Created" and "Status" and "Add card" and "Created by" in setup.page_source, "Required fields are missing"




