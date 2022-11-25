import pytest
import allure
from pom.selenium_functions import Signin, Base
from configuration import CODE, USERNAME_HA, PASSWORD_HA
from pom.pages.mainscreen_page import START_MAIN_MENU, BUILDING_ADDRESS_TAG


@allure.title("Check Hovers for strings of Buildings")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_HA, PASSWORD_HA, CODE)])
def test_case(setup, username, password, code):
    """
    Check Hovers for strings of Buildings
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, START_MAIN_MENU, BUILDING_ADDRESS_TAG, 0).sorting()
    Base(setup, START_MAIN_MENU).scrolling()
    Base(setup, START_MAIN_MENU, BUILDING_ADDRESS_TAG, 0).sorting()
    Base(setup, START_MAIN_MENU).scrolling()
