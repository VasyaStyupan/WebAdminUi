import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME, PASSWORD, CODE
from pom.pages.mainscreen_page import MainScreen
from pom.pages.logout_menu import START_LOGOUT_MENU
from pom.pages.logout_menu import SWEDISH
import time


@allure.title("Check UX translation with Svenska loc")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME, PASSWORD, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Language] Check UX translation with Svenska loc
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    MainScreen(setup).find_popup()
    Base(setup, START_LOGOUT_MENU[1], SWEDISH).switch_to_lang()
    time.sleep(1)
    with allure.step("Step 1. Check UX translation with Svenska loc"):
        assert "Ändra språk" and "Sök efter användare och enheter" in setup.page_source, "Switch to Svenska does not work"
