import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.logout_menu import ACCESS_CARDS, START_LOGOUT_MENU
import time


@allure.title("Default status of created card is Active")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Profile/Access cards] Default status of created card is Active
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).profile_menu()
    card_is_present = Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).add_card()
    time.sleep(1)
    if card_is_present == 0:
        with allure.step("Step 1. Check if card is active"):
            assert "active" in setup.page_source, "Default status of created card is not Active"
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).delete_card()
    time.sleep(1)



