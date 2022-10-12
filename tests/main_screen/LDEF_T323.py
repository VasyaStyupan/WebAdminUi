import allure
import pytest
from pom.selenium_functions import Signin
from configuration import USERNAME_HA, USERNAME_BA, USERNAME_UO, USERNAME_UM
from configuration import PASSWORD_HA, PASSWORD_UO, PASSWORD_UM, PASSWORD_BA, CODE
import time


@allure.title("The button is available if logged in by hyperadmin")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME_HA, PASSWORD_HA, CODE, 0),
])
def test_case1(setup, username, password, code, scenario):
    """
    Check if the button is available if logged in by hyperadmin
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    with allure.step("Step 1. Check if the button is available if logged in by hyperadmin"):
        assert "Your buildings" in setup.page_source


@allure.title("The button is available if logged in by building manager")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME_BA, PASSWORD_BA, CODE, 0),
])
def test_case2(setup, username, password, code, scenario):
    """
    Check if the button is available if logged in by hyperadmin
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    time.sleep(1)
    with allure.step("Step 1. Check if the button is available if logged in by building manager"):
        assert "Your buildings" in setup.page_source


@allure.title("The button is not available if logged in by unit owner")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME_UO, PASSWORD_UO, CODE, 0),
])
def test_case3(setup, username, password, code, scenario):
    """
    Check if the button is not available if logged in by unit owner
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    # time.sleep(1)
    with allure.step("Step 1. Check if the button is not available if logged in by unit owner"):
        assert "Your buildings" not in setup.page_source


@allure.title("The button is not available if logged in by unit manager")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME_UM, PASSWORD_UM, CODE, 0),
])
def test_case4(setup, username, password, code, scenario):
    """
    Check if the button is not available if logged in by unit manager
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    time.sleep(1)
    with allure.step("Step 1. Check if the button is not available if logged in by unit manager"):
        assert "Your buildings" not in setup.page_source
