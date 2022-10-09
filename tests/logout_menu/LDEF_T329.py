import time
import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.logout_menu import UNITS, START_LOGOUT_MENU, Logout
from pom.pages.mainscreen_page import MainScreen


@allure.title("View the screen Units")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Profile] View the screen Units
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    MainScreen(setup).find_popup().click()
    Base(setup, START_LOGOUT_MENU[0], UNITS).logout_menu()
    Logout(setup).units_tag()
    time.sleep(1)
    with allure.step("Step 1. Check presence of necessary tags"):
        assert "Personal info" and "Units" and "Access Cards" and "Reset Password" in setup.page_source, "Required tags  are missing"
    with allure.step("Step 2. Check presence of next tags"):
        assert "Buildings" and "Units" and "Unit manager" and "Doorbell button" and "Digital keys" and "Remove user" in setup.page_source, "Required fields  are missing"
    time.sleep(1)





# нажать на edit и прооверить все кнопки и поля (они другие)
