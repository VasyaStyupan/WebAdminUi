import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME, PASSWORD, CODE
from pom.pages.mainscreen_page import MainScreen
from pom.pages.logout_menu import START_LOGOUT_MENU
import time


@allure.title("Check the Menu: Profile/Language/Logout (with Hovers)")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME, PASSWORD, CODE)])
def test_case(setup, username, password, code):
    """
    [Main screen] Check the Menu: Profile/Language/Logout (with Hovers)
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    MainScreen(setup).find_popup().click()

    Base(setup, START_LOGOUT_MENU).hover_popup()


