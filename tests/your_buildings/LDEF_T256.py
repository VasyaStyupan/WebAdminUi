import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.your_units import Units
from pom.pages.your_building import Buildings
from pom.pages.logout_menu import ACCESS_CARDS, START_LOGOUT_MENU
import time


@allure.title("Delete a card")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Users/Any user/Access cards] Delete a card
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).enter_the_unit()
    Units(setup).select_simple_user()
    Buildings(setup).access_cards()
    Base(setup, START_LOGOUT_MENU[0]).add_card()
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).delete_card()
    time.sleep(2)
    with allure.step("Step 1. Delete the card"):
        assert "Add or change card PIN code" not in setup.page_source, "Can`t delete the card"
