import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.logout_menu import ACCESS_CARDS, START_LOGOUT_MENU
from pom.pages.your_building import Buildings
import time


@allure.title("Profile/Access cards] Add card")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Profile/Access cards] Add card
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).profile_menu()
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).add_card()
    time.sleep(2)
    if "This access card is already registered" not in setup.page_source:
        with allure.step("Step 1. Check if it possible to add card"):
            assert "CardName" in setup.page_source, "Can`t add card"
    else:
        Buildings(setup).cancel()
    time.sleep(1)
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).delete_card()
    time.sleep(1)

