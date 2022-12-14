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
    Base(setup, START_LOGOUT_MENU[0], UNITS).mark_unmark_unit_manager()
    Logout(setup).check_unit_manager_active()
    time.sleep(1)



