import time

import allure
import pytest
from pom.selenium_functions import Signin
from configuration import USERNAME, PASSWORD, CODE, CODE_URL


@allure.title("Enter correct/incorrect Authentication Code")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME, PASSWORD, CODE, 0),
    (USERNAME, PASSWORD, "CODE", 0),
    (USERNAME, PASSWORD, CODE * 4, 0),
    (USERNAME, PASSWORD, "@#!&%$^*~+", 0),
    (USERNAME, PASSWORD, CODE[:-1], 1),
    (USERNAME, PASSWORD, "", 1),
])
def test_case(setup, username, password, code, scenario):
    """
    [Welcome page] Enter correct/incorrect Authentication Code
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    time.sleep(1)
    if scenario == 0:
        with allure.step("Step 1. Valid Authentication Code entry"):
            assert "Your units" in setup.page_source, "Wrong code"
    else:
        with allure.step("Step 1. Wrong Authentication Code entry"):
            assert "Enter Authentication Code" in setup.page_source, "Access error"


