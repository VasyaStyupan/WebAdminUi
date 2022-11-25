import time

import pytest
import allure
from pom.selenium_functions import Signin, Base
from configuration import CODE, USERNAME_HA, PASSWORD_HA
from pom.pages.mainscreen_page import START_MAIN_MENU, BUILDING_ADDRESS_TAG


@allure.title("Check sorting by field 'Building address'")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_HA, PASSWORD_HA, CODE)])
def test_case(setup, username, password, code):
    """
    [Main screen] Check sorting by field "Building address"
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    items_list = Base(setup, START_MAIN_MENU, BUILDING_ADDRESS_TAG, 0).sorting()
    with allure.step("Step 1. Check if reverse sort by field 'Building address' working"):
        assert items_list == sorted(items_list, key=str.upper, reverse=True), "Reverse sort is not working"
    items_list = Base(setup, START_MAIN_MENU, BUILDING_ADDRESS_TAG, 0).sorting()
    with allure.step("Step 2. Check if sort by field 'Building address' working"):
        assert items_list == sorted(items_list, key=str.upper), "Sort is not working"


