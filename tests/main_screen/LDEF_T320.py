import time

import pytest
import allure
from pom.selenium_functions import Signin, Base
from configuration import CODE, USERNAME_HA, PASSWORD_HA
from pom.pages.mainscreen_page import START_MAIN_MENU


@allure.title("Check scrolling for Building addresses")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_HA, PASSWORD_HA, CODE)])
def test_case(setup, username, password, code):
    """
    [Main screen] Check scrolling for Building addresses
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, START_MAIN_MENU).scrolling()
    time.sleep(1)


