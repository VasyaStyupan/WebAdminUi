import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE, SIMPLE_USER
from pom.pages.your_building import Buildings
import time


@allure.title("[Building/Users/Any user/Access cards] Edit card")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Users/Any user/Access cards] Edit card
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).enter_the_unit()
    Base(setup, SIMPLE_USER).select_user()
    Buildings(setup).access_cards()
    time.sleep(1)
    if "CardName" and "MyCard" not in setup.page_source:
        Base(setup, "CardName", "1234567890").add_card()
        Base(setup).edit_card()
        time.sleep(1)
        with allure.step("Step 1. Check if it possible to edit card"):
            assert "Add or change card PIN code" and "MyCard" in setup.page_source, "Can`t edit card"
    Base(setup, "MyCard").delete_card()
    time.sleep(1)
