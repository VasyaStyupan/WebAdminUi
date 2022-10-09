import time

import allure
import pytest
from pom.selenium_functions import Signin
from configuration import USERNAME_BA, PASSWORD_BA, CODE, USERNAME_UM, BASE_URL
from pom.pages.logout_menu import UNITS, START_LOGOUT_MENU, Logout
from pom.selenium_functions import Base
from pom.selenium_functions import Hwa


@allure.title("Remove user")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Profile/Units] Remove user
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, START_LOGOUT_MENU[0], UNITS).remove_user()
    time.sleep(1)
    with allure.step("Step 1. Check if user is deleted from unit"):
        assert "Remove user" not in setup.page_source, "Error user deleting"
    Base(setup, USERNAME_UM).link_unit()
    setup.get(BASE_URL)
    Base(setup, START_LOGOUT_MENU[0], UNITS).profile_menu()

    Logout(setup).mark_unit_manager()
    time.sleep(1)
