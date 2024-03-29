import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.logout_menu import ACCESS_CARDS, START_LOGOUT_MENU
import time


@allure.title("Change card PIN code")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Profile/Access cards] Change card PIN code
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).profile_menu()
    Base(setup, "CardName", "1234567890").add_card()
    Base(setup).add_pin_code()
    time.sleep(1)
    with allure.step("Step 1. Check if PIN code is entered"):
        assert "Add or change card PIN code" in setup.page_source, "Can`t enter PIN code"
    Base(setup).update_pin_code()
    with allure.step("Step 2. Check if PIN code is edited"):
        assert "Add or change card PIN code" in setup.page_source, "Can`t update PIN code"
    Base(setup, "CardName").delete_card()
    time.sleep(1)


