import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.logout_menu import ACCESS_CARDS, START_LOGOUT_MENU, Logout
import time


@allure.title("Change status card on Disabled")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Profile/Access cards] Change status card on Disabled
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).profile_menu()
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).add_card()
    Logout(setup).mark_status_card()
    time.sleep(1)
    with allure.step("Step 1. Check if card is disabled"):
        assert "disabled" in setup.page_source, "Can`t disable card"
    Logout(setup).mark_status_card()
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS,"CardName").delete_card()
    time.sleep(1)

