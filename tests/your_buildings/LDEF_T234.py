import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Check whether the selected (not selected) unit manager functions work correctly")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case1(setup, username, password, code):
    """
    [Building/Settings] Check if the selected (not selected) unit manager can add user
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).enter_building_settings()
    Base(setup).check_add_user_function()
    time.sleep(1)
    with allure.step("Step 1. Check if 'Add user' button is missing"):
        assert "Add user" not in setup.page_source, "'Add user' function does not work properly"
    Base(setup).logout()
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).enter_building_settings()
    Base(setup).check_add_user_function()
    time.sleep(1)
    with allure.step("Step 2. Check if 'Add user' button is present"):
        assert "Add user" in setup.page_source, "'Add' user function does not work properly"


@allure.title("Check whether the selected (not selected) unit manager functions work correctly")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case2(setup, username, password, code):
    """
    [Building/Settings] Check if the unit manager can change the name of the unit
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).enter_building_settings()
    Base(setup).check_change_unit_name_function()
    time.sleep(1)
    with allure.step("Step 1. Check if 'Settings' tag is missing"):
        assert "Settings" not in setup.page_source, "'Change unit name' function does not work properly"
    Base(setup).logout()
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).enter_building_settings()
    Base(setup).check_change_unit_name_function()
    time.sleep(1)
    with allure.step("Step 1. Check if 'Settings' tag is present"):
        assert "Settings" in setup.page_source, "'Change unit name' function does not work properly"


@allure.title("Сheck whether the selected (not selected) unit manager functions work correctly")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case3(setup, username, password, code):
    """
    [Building/Settings] Check if the unit manager can add the unit manager role to another user
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).enter_building_settings()
    Base(setup).check_add_role_unit_manager__function()
    time.sleep(1)
    with allure.step("Step 1. Check if massage 'You don`t have admin permissions' is present"):
        assert "You don't have admin permissions" in setup.page_source, "'Error while adding unit manager role to " \
                                                                        "another user "
    time.sleep(2)
    Base(setup).logout()
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).enter_building_settings()
    Base(setup).check_add_role_unit_manager__function()
    Base(setup).logout()
    Base(setup).delete_user()
