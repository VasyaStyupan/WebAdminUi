import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE, SIMPLE_USER
from pom.pages.your_building import Buildings
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
    Base(setup, SIMPLE_USER).select_user()
    Buildings(setup).access_cards()
    Base(setup, "CardName", "1234567890").add_card()
    time.sleep(1)
    if "This access card is already registered" not in setup.page_source:
        with allure.step("Step 1. Check if it possible to add card"):
            assert "CardName" in setup.page_source, "Can`t add card"
    else:
        Buildings(setup).cancel()
    Base(setup, "CardName").delete_card()
    time.sleep(3)
    with allure.step("Step 2. Delete the card"):
        assert "Add or change card PIN code" not in setup.page_source, "Can`t delete the card"