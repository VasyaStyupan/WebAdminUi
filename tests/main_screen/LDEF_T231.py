import time
import allure
import pytest
from pom.selenium_functions import Signin
from pom.pages.mainscreen_page import MainScreen
from configuration import USERNAME_HA, PASSWORD_HA, CODE, SIMPLE_USER, UNIT


@allure.title("Check the function of the search field")
@pytest.mark.parametrize('username, password, code, search_word', [
    (USERNAME_HA, PASSWORD_HA, CODE, SIMPLE_USER),
    (USERNAME_HA, PASSWORD_HA, CODE, SIMPLE_USER[:3]),
    (USERNAME_HA, PASSWORD_HA, CODE, UNIT),
    (USERNAME_HA, PASSWORD_HA, CODE, UNIT[:3]),
])
def test_case(setup, username, password, code, search_word):
    """
    [Main screen/ Searching] Check the function of the search field
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    MainScreen(setup, search_word).search_bar()
    MainScreen(setup, search_word).search_user().click()
    with allure.step("Step 1. Check if user or unit is found "):
        assert "Personal Info" or "You are managing the unit" in setup.page_source

