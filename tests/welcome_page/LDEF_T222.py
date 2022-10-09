import allure
import pytest
from pom.selenium_functions import Signin
from configuration import USERNAME, PASSWORD, CODE, BASE_URL


@allure.title("Enter correct/incorrect Authentication Code")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME, PASSWORD, CODE, 0),  # 0 - positive, 1 - negative
    (USERNAME.upper(), PASSWORD, CODE, 0),
    (f" {USERNAME} ", PASSWORD, CODE, 0),
    (USERNAME, f" {PASSWORD} ", CODE, 0),
    (USERNAME, PASSWORD.upper(), CODE, 1),
    (USERNAME, PASSWORD[:-1], CODE, 1),
    (USERNAME, PASSWORD[:5], CODE, 1),
    (USERNAME[:-1], PASSWORD, CODE, 1),
    ("", "", CODE, 1),
    ("", PASSWORD, CODE, 1),
    (PASSWORD, "", CODE, 1)])
def test_case(setup, username, password, code, scenario):
    """"
    [Welcome page] Enter correct/incorrect Authentication Code
    """
    current_url = Signin(setup, username, password, code).login_credentials()
    if scenario == 0:
        with allure.step("Step 1. Username and password entry"):
            assert f"{BASE_URL}/auth-code" == current_url, "Wrong username or password"
    else:
        with allure.step("Step 1. Username and password entry"):
            assert f"{BASE_URL}/login" == current_url, "Access error"
