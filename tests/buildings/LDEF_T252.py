import time
import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE, SIMPLE_USER, UID
from pom.pages.logout_menu import Logout, START_LOGOUT_MENU, UNITS


@allure.title("Changing value Doorbell button")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Users/Any user/Units] Changing value Doorbell button
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, UID).enter_the_unit()
    Base(setup, SIMPLE_USER).select_user().click()
    Logout(setup).units_tag().click()
    Base(setup, START_LOGOUT_MENU[0], UNITS).mark_unmark_doorbel_button()
    Logout(setup).units_tag().click()
    Logout(setup).checkbox_doorbell_button().click()




