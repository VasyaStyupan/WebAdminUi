import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE, SIMPLE_USER, UID
from pom.pages.your_building import Buildings
from pom.pages.logout_menu import Logout
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
    Base(setup, UID).enter_the_unit()
    Base(setup, SIMPLE_USER).select_user().click()
    Buildings(setup).access_cards_tag().click()
    time.sleep(1)
    if "CardName" and "MyCard" not in setup.page_source:
        Logout(setup).add_card_button().click()
        if 'Add units' in setup.page_source:
            unit = Base(setup).check_if_units_more_then_one()
            with allure.step("Step 1. Check if unit added"):
                assert unit in setup.page_source, "Can`t add unit"
            Logout(setup).remove_unit().click()
            Base(setup).check_if_units_more_then_one()
        Base(setup, "CardName", "1234567890").input_card_info()
        status = Logout(setup).save_button().is_enabled()
        if status is True:
            Logout(setup).save_button().click()
        else:
            Buildings(setup).cancel().click()
        Base(setup).edit_card()
        time.sleep(1)
        with allure.step("Step 3. Check if it possible to edit card"):
            assert "Add or change card PIN code" and "MyCard" in setup.page_source, "Can`t edit card"
    Base(setup, "MyCard").delete_card()
    time.sleep(1)
