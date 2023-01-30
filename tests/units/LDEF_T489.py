import allure
import pytest
from pom.selenium_functions import Signin, Base, Units
from configuration import USERNAME_BA, PASSWORD_BA, CODE, USERNAME_UO, SIMPLE_USER
import time


@allure.title("Change unit owner")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Settings] Change unit owner
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).change_unit_info_ba()
    first_name, last_name = Base(setup, SIMPLE_USER).change_unit_owner()
    time.sleep(1)
    with allure.step("Step 1. Check if unit owner is changed"):
        assert first_name and last_name in setup.page_source, "Change unit owner error"
    Base(setup, USERNAME_UO).change_unit_owner()
    time.sleep(1)
    Base(setup).restore_unit_owner()


