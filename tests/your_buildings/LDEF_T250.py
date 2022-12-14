import time
import allure
import pytest
from pom.selenium_functions import Signin, Base, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE, USERNAME_UM
from pom.pages.logout_menu import Logout, START_LOGOUT_MENU, UNITS


@allure.title("Changing role of user to unit manager")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Users/Any user/Units] Changing role of user to unit manager
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).enter_the_unit()
    Base(setup, USERNAME_UM).select_user()
    Logout(setup).units_tag()
    Logout(setup).mark_unit_manager()
    time.sleep(1)
    Logout(setup).mark_unit_manager()
    time.sleep(1)

