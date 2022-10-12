import time

import pytest
import allure
from pom.selenium_functions import Signin
from configuration import CODE, USERNAME_UO, PASSWORD_UO


@allure.title("Unit owner is logged. View the screen")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_UO, PASSWORD_UO, CODE)])
def test_case(setup, username, password, code):
    """
    [Main screen] Unit owner is logged. View the screen
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    with allure.step("Step 1. Check if user can see 'Unit manager', 'Your unit', 'Users', 'Access', 'Doorbell'"):
        assert "Unit manager" and "Users" and "Access" and "Doorbell" and "Your unit" in setup.page_source, "Wrong user page"


