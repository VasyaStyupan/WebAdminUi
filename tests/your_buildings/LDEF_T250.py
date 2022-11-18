import time
import allure
import pytest
from pom.selenium_functions import Signin, Base2, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.your_units import Units
from pom.pages.logout_menu import Logout, START_LOGOUT_MENU, UNITS

# @pytest.mark.skip
@allure.title("Changing role of user to unit manager")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Users/Any user/Units] Changing role of user to unit manager
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base2(setup).enter_the_unit()
    Units(setup).select_simple_user()
    Logout(setup).units_tag()
    Logout(setup).mark_unit_manager()
    time.sleep(1)
    Logout(setup).mark_unit_manager()
    time.sleep(1)

