import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE, SIMPLE_USER, UID
from pom.pages.your_building import Buildings
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
    Base(setup, UID).enter_the_unit()
    Base(setup, SIMPLE_USER).select_user().click()
    Buildings(setup).access_cards_tag().click()
    Base(setup, "CardName", "1234567890").add_card()
    Base(setup).add_pin_code()
    time.sleep(1)
    with allure.step("Step 1. Check possibility of adding the card PIN code"):
        assert "Add or change card PIN code" in setup.page_source, "Can`t update PIN code"
    Base(setup).add_pin_code()
    Base(setup, "CardName").delete_card()
    time.sleep(1)
