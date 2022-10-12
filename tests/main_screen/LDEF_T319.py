import time

import pytest
import allure
from pom.selenium_functions import Signin, Base
from configuration import CODE, USERNAME_HA, PASSWORD_HA
from pom.pages.mainscreen_page import START_MAIN_MENU, MainScreen


@allure.title("Check sorting by field 'Building address'")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_HA, PASSWORD_HA, CODE)])
def test_case(setup, username, password, code):
    # first_letter_arr = None
    """
    [Main screen] Check sorting by field "Building address"
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    first_letter_arr = Base(setup, START_MAIN_MENU).hover()
    with allure.step("Step 1. Check if reverse sort by field 'Building address' working"):
        assert first_letter_arr == sorted(first_letter_arr, key=lambda c: c.upper(), reverse=True), "Reverse sort is not working"
    first_letter_arr = Base(setup, START_MAIN_MENU).hover()
    with allure.step("Step 2. Check if sort by field 'Building address' working"):
        assert first_letter_arr == sorted(first_letter_arr, key=lambda c: c.upper()), "Sort is not working"



