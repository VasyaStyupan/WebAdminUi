import allure
import pytest
from pom.selenium_functions import Signin
from pom.selenium_functions import Units, Base
from configuration import USERNAME_UM, PASSWORD_UM, CODE, UNIT
import time


@allure.title("Add user with only Email filled")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_UM, PASSWORD_UM, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Users] Add user with only Email filled
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, UNIT).select_unit()
    Base(setup).add_user_with_only_email()
    status = Units(setup).save_button().is_enabled()
    time.sleep(1)
    with allure.step("Step 1. Check if Save button is active"):
        assert status is False, "Save button is active"

