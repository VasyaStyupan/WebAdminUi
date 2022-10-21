import time
import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.logout_menu import ACCESS, START_LOGOUT_MENU, Logout
from pom.pages.mainscreen_page import MainScreen


@allure.title("View the list of Doors")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Language] Choose different language
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    MainScreen(setup).find_popup().click()
    Base(setup, START_LOGOUT_MENU[1], ACCESS).logout_menu()
    time.sleep(1)
    with allure.step("Step 1. Check switch to English"):
        assert "Choose language" in setup.page_source, "Language selection error"
    Logout(setup).switch_to_norwegian()
    time.sleep(1)
    with allure.step("Step 2. Check switch to Norwegian"):
        assert "Velg språk" in setup.page_source, "Language selection error"
    Logout(setup).switch_to_swedish()
    time.sleep(1)
    with allure.step("Step 2. Check switch to S"):
        assert "Ändra språk" in setup.page_source, "Language selection error"



