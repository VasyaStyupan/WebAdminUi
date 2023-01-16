import time

import pytest
import allure
from pom.selenium_functions import Signin
from configuration import CODE, USERNAME_UM, PASSWORD_UM


@allure.title("Unit manager is logged. View the screen")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_UM, PASSWORD_UM, CODE)])
def test_case(setup, username, password, code):
    """
    [Main screen] Unit manager is logged. View the screen
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    time.sleep(1)
    with allure.step("Step 1. Check if user can see 'Unit manager', 'Your unit', 'Users', 'Access', 'Doorbell'"):
        assert "Unit manager" and "Users" and "Access" and "Doorbell" and "Your unit" in setup.page_source, "Wrong user page"


