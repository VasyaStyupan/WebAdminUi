import time
import allure
import pytest
from pom.selenium_functions import Signin
from configuration import USERNAME_UM, PASSWORD_UM, CODE
from pom.pages.logout_menu import UNITS, START_LOGOUT_MENU
from pom.selenium_functions import Base


@allure.title("Mark/Unmark option 'Doorbell button' and check on the doorbell")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_UM, PASSWORD_UM, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Profile/Units] Mark/Unmarked option 'Doorbell button' and check on the doorbell
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, START_LOGOUT_MENU[0], UNITS).mark_unmark_doorbel_button()
    time.sleep(1)



