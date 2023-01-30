import allure
import pytest
from pom.selenium_functions import Signin, Base, Units
from configuration import USERNAME_UM, PASSWORD_UM, CODE, UNIT
import time


@allure.title("Add user. View the list of created users")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_UM, PASSWORD_UM, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Users] Add user. View the list of created users
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, UNIT).select_unit()
    Base(setup).add_user()
    Units(setup).view_list_of_users()
    time.sleep(1)
    with allure.step("Step 1. Check presence of necessary tags"):
        assert "Users" and "Access" and "Doorbell" in setup.page_source, "Required tags  are missing"
    time.sleep(1)
    with allure.step("Step 2. Check presence of created user"):
        assert "JohnDoe@mail.com" in setup.page_source, "User not created"
    Base(setup).delete_user()
