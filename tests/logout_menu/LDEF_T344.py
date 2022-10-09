import time
import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.logout_menu import ACCESS, START_LOGOUT_MENU, Logout
from pom.pages.mainscreen_page import MainScreen


@allure.title("View the list of Doors")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Profile/Access]View the list of Doors
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    MainScreen(setup).find_popup().click()
    Base(setup, START_LOGOUT_MENU[0], ACCESS).logout_menu()
    Logout(setup).access_tag()
    time.sleep(1)
    with allure.step("Step 1. Check presence of necessary tags"):
        assert "Personal info" and "Units" and "Access Cards" and "Reset Password" in setup.page_source, "Required tags  are missing"
    with allure.step("Step 2. Check presence of necessary fields"):
        assert "Doors" in setup.page_source, "Tag 'Doors' is missing"




