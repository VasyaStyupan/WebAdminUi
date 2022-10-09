import time

import allure
import pytest
from pom.selenium_functions import Signin
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.logout_menu import UNITS, START_LOGOUT_MENU
from pom.selenium_functions import Base


@allure.title("Mark/Unmark option 'Digital Keys' and check opening the door from app")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Profile/Units] Mark/Unmark option 'Digital Keys' and check opening the door from app
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, START_LOGOUT_MENU[0], UNITS).mark_unmark_digital_keys()
    time.sleep(1)


