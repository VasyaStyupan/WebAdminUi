import allure
import pytest
from pom.selenium_functions import Signin, Base, Logout, BASE_URL, Units, Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE, SIMPLE_USER, SIMPLE_PASS
import time


@allure.title("Add user and make this user a unit manager")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Users] Add user and make this user a unit manager
    """

    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).select_your_units()
    Base(setup, SIMPLE_USER).delete_user_from_unit()
    time.sleep(1)
    with allure.step("Step 1. Check if Simple user is deleted from unit"):
        assert SIMPLE_USER not in setup.page_source, "Simple user is not deleted from unit"
    Base(setup).select_your_units()
    Base(setup).add_simple_user()
    Units(setup).save_button().click()
    time.sleep(3)
    with allure.step("Step 2. Check if Simple user is added to unit"):
        assert SIMPLE_USER in setup.page_source, "Simple user is not added to unit"
    Buildings(setup).users_tag().click()
    Base(setup, SIMPLE_USER).select_user().click()
    Buildings(setup).units_tag().click()
    Logout(setup).checkbox_unit_manager().click()
    time.sleep(2)   # safari
    Base(setup).logout()
    current_url = Signin(setup, SIMPLE_USER, SIMPLE_PASS).login_credentials()
    Signin(setup, username, password, code).login_code()
    with allure.step("Step 3. Check if Simple user can login as unit manager"):
        assert f"{BASE_URL}/auth-code" == current_url, "Simple user can`t login"
    Base(setup).logout()
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).select_your_units()
    Base(setup, SIMPLE_USER).select_user().click()
    Buildings(setup).units_tag().click()
    Logout(setup).checkbox_unit_manager().click()
    time.sleep(1)
