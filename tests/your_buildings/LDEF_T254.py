import allure
import pytest
from pom.selenium_functions import Signin, Base2, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.your_units import Units
from pom.pages.your_building import Buildings
from pom.pages.logout_menu import ACCESS_CARDS, START_LOGOUT_MENU
import time


@allure.title("[Building/Users/Any user/Access cards] Add a card")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Users/Any user/Access cards] Add a card
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base2(setup).enter_the_unit()
    Units(setup).select_simple_user()
    Buildings(setup).access_cards()
    time.sleep(1)
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).add_card()
    time.sleep(1)
    if "This access card is already registered" not in setup.page_source:
        with allure.step("Step 1. Check if it possible to add card"):
            assert "CardName" in setup.page_source, "Can`t add card"
    else:
        Buildings(setup).cancel()
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).delete_card()
    time.sleep(1)






