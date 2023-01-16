import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE, SIMPLE_USER
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
    Base(setup).enter_the_unit()
    Base(setup, SIMPLE_USER).select_user()
    Buildings(setup).access_cards()
    Logout(setup).add_card_button()
    Base(setup).check_if_units_more_then_one()
    Logout(setup, "CardName", "").input_card_info()
    status = Logout(setup).save_button().is_enabled()
    time.sleep(1)
    with allure.step("Step 1. Check if it possible to add card with empty card name field"):
        assert status is False, "Error adding card with empty card name field"
    Logout(setup, "", "1234567890").input_card_info()
    status = Logout(setup).save_button().is_enabled()
    time.sleep(1)
    with allure.step("Step 2. Check if it possible to add card with empty card number field"):
        assert status is False, "Error adding card with empty card number field"
    Logout(setup, "CardName", "1").input_card_info()
    status = Logout(setup).save_button().is_enabled()
    time.sleep(1)
    with allure.step("Step 3. Check if it possible to add card with only character in the card number field"):
        assert status is True, "Error adding card with only character in the card number field"
    Logout(setup, Buildings(setup, 50).generate_random_string(), "1").input_card_info()
    status = Logout(setup).save_button().is_enabled()
    time.sleep(1)
    with allure.step("Step 4. Check if it possible to add card with 50 characters in the card name field"):
        assert status is True, "Error adding card with 50 characters in the card name field"
    Logout(setup, "CardName", "1234567890").input_card_info()
    Logout(setup).save_button().click()
    time.sleep(1)
    if "This access card is already registered" not in setup.page_source:
        with allure.step("Step 5. Check if it possible to add card"):
            assert "CardName" in setup.page_source, "Can`t add card"
    else:
        Buildings(setup).cancel()
    Base(setup, "CardName").delete_card()
    time.sleep(1)
