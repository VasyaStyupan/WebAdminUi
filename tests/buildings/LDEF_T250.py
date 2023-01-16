import time
import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE, SIMPLE_USER, SIMPLE_PASS
from pom.pages.logout_menu import Logout


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
    Base(setup, SIMPLE_USER).select_user()
    Logout(setup).units_tag()
    Logout(setup).mark_unit_manager()
    Base(setup).logout()
    Signin(setup, SIMPLE_USER, SIMPLE_PASS).login_credentials()
    with allure.step("Step 1. Check if simple user can log in as unit manager"):
        assert "You don't have access" not in setup.page_source, "Can`t log in as unit manager"
    Signin(setup, SIMPLE_USER, SIMPLE_PASS, code).login_code()
    time.sleep(1)
    Base(setup).logout()
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).enter_the_unit()
    Base(setup, SIMPLE_USER).select_user()
    Logout(setup).units_tag()
    Logout(setup).mark_unit_manager()
    time.sleep(1)
