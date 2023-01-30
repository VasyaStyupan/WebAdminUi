import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME, PASSWORD, CODE
from pom.pages.mainscreen_page import MainScreen, START_LOGOUT_MENU
from pom.pages.logout_menu import NORWEGIAN
import time


@allure.title("Check UX translation with Norsk loc")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME, PASSWORD, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Language] Check UX translation with Norsk loc
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).find_popup().click()
    Base(setup, START_LOGOUT_MENU[1], NORWEGIAN).switch_to_lang()
    time.sleep(2)
    with allure.step("Step 1. Check UX translation with Norsk loc"):
        assert "Velg språk" and "Søk etter brukere og enheter" in setup.page_source, "Switch to Norsk does not work"




