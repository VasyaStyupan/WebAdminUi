import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE, BASE_URL
from pom.pages.logout_menu import ACCESS_CARDS, START_LOGOUT_MENU, Logout
from pom.pages.hwa import Hwa
import time


@allure.title("Change status of RFID in HA and check displaying changes in CWA")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Profile/Access cards] Change status of RFID in HA and check displaying changes in CWA
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).profile_menu()
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).add_card()
    Hwa(setup).signin_hwa()
    Hwa(setup, USERNAME_BA).search_hwa()
    Hwa(setup).change_rfid_status()
    time.sleep(1)
    with allure.step("Step 1. Check if card is disabled"):
        assert "disabled" in setup.page_source, "Can`t disable card"
    setup.get(BASE_URL)
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).profile_menu()
    Logout(setup).mark_status_card()
    time.sleep(1)
    Logout(setup).mark_status_card()
    setup.refresh()
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).profile_menu()
    Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).delete_card()
    time.sleep(3)
