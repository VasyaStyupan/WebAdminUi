import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.your_units import Units
from pom.pages.your_building import Buildings
from pom.pages.logout_menu import ACCESS_CARDS, START_LOGOUT_MENU
import time


@allure.title("Add/change card PIN code")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Users/Any user/Access cards] Add/change card PIN code
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).enter_the_unit()
    Units(setup).select_simple_user()
    Buildings(setup).access_cards()
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).add_pin_code()
    time.sleep(1)
    with allure.step("Step 1. Check possibility of adding the card PIN code"):
        assert "Add or change card PIN code" in setup.page_source, "Can`t update PIN code"
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).delete_card()
    time.sleep(1)
