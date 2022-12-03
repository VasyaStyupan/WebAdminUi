import time
import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.logout_menu import UNITS, START_LOGOUT_MENU


@allure.title("Check tips for 'Doorbell button' and 'Digital Keys'")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Profile/Units] Check tips for 'Doorbell button' and 'Digital Keys'
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, START_LOGOUT_MENU[0], UNITS).check_tips_doorbell_button()
    with allure.step("Step 1. Check presence of Doorbell button tips"):
        assert "Uncheck to remove user's doorbell button" in setup.page_source, "Doorbell button tips are missing"
    Base(setup, START_LOGOUT_MENU[0], UNITS).check_tips_digital_keys()
    with allure.step("Step 2. Check presence of Digital keys tips"):
        assert "Uncheck to remove user's doorbell button" in setup.page_source, "Doorbell button tips are missing"


