import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_HA, PASSWORD_HA, CODE
from pom.pages.logout_menu import ACCESS_CARDS, START_LOGOUT_MENU
import time


@allure.title("Add units. Choose Units (one/multiple) from the list")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_HA, PASSWORD_HA, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Profile/Access cards] Add units. Choose Units (one/multiple) from the list
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).profile_menu()
    if Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).add_units() is True:
        time.sleep(1)
        with allure.step("Step 1. Check presence of necessary tags"):
            assert "Remove" in setup.page_source, "Unit adding error"


