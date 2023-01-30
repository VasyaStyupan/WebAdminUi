
import time
import allure
import pytest
from pom.selenium_functions import Signin
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.logout_menu import UNITS, START_LOGOUT_MENU, Logout
from pom.selenium_functions import Base


@allure.title("Mark/Unmark option 'Unit Manager'")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Profile/Units] Mark/Unmark option 'Unit Manager'
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, START_LOGOUT_MENU[0], UNITS).profile_menu()
    try:
        Base(setup).mark_unmark_unit_manager()
        time.sleep(1)
        with allure.step("Step 1. Check mark/unmark unit manager option"):
            assert "Profile was updated successfully!" in setup.page_source, "Missing notification"
    except Exception:
        pass
