import time
import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.logout_menu import UNITS, START_LOGOUT_MENU, Logout
from pom.pages.mainscreen_page import MainScreen


@pytest.mark.skip
@allure.title("Personal Info. Edit personal data")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Profile] Personal Info. Edit personal data
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    MainScreen(setup).find_popup()
    Base(setup, START_LOGOUT_MENU[0], UNITS).logout_menu()
    Logout(setup).edit_info()
    time.sleep(1)
    with allure.step("Step 1. Check presence of necessary tags"):
        assert "Personal info" and "Units" and "Access Cards" and "Reset Password" in setup.page_source, "Required tags  are missing"
    with allure.step("Step 2. Check presence of necessary fields"):
        assert "First Name" and "Last Name" and "Country code" and "Phone" and "Username" and "Email" in setup.page_source, "Required fields  are missing"
    with allure.step("Step 3. Check presence of necessary buttons"):
        assert "Cancel" and "Save" in setup.page_source, "Required buttons are missing"

