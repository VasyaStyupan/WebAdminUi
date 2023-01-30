import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE, SIMPLE_USER, UID
from pom.pages.your_building import Buildings
from pom.pages.logout_menu import Logout
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
    Base(setup, UID).enter_the_unit()
    Base(setup, SIMPLE_USER).select_user().click()
    Buildings(setup).access_cards_tag().click()
    Logout(setup).add_card_button().click()
    if 'Add units' in setup.page_source:
        Base(setup).check_if_units_more_then_one()
    Base(setup, "CardName", "").input_card_info()
    status = Logout(setup).save_button().is_enabled()
    time.sleep(1)
    with allure.step("Step 1. Check if it possible to add card with empty card name field"):
        assert status is False, "Error adding card with empty card name field"
    Base(setup, "", "1234567890").input_card_info()
    status = Logout(setup).save_button().is_enabled()
    time.sleep(1)
    with allure.step("Step 2. Check if it possible to add card with empty card number field"):
        assert status is False, "Error adding card with empty card number field"
    Base(setup, "CardName", "1").input_card_info()
    status = Logout(setup).save_button().is_enabled()
    time.sleep(1)
    with allure.step("Step 3. Check if it possible to add card with only character in the card number field"):
        assert status is True, "Error adding card with only character in the card number field"
    Base(setup, Buildings(setup, 50).generate_random_string(), "1").input_card_info()
    status = Logout(setup).save_button().is_enabled()
    time.sleep(1)
    with allure.step("Step 4. Check if it possible to add card with 50 characters in the card name field"):
        assert status is True, "Error adding card with 50 characters in the card name field"
    Base(setup, "CardName", "1234567890").input_card_info()
    if "This access card is already registered" not in setup.page_source:
        Logout(setup).save_button().click()
        time.sleep(1)
        with allure.step("Step 5. Check if it possible to add card"):
            assert "CardName" in setup.page_source, "Can`t add card"
    else:
        Buildings(setup).cancel().clcik()
    Base(setup, "CardName").delete_card()
    time.sleep(1)
