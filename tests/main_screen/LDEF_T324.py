import allure
import pytest
from pom.selenium_functions import Signin
from configuration import USERNAME_HA, USERNAME_BA, USERNAME_HA_NO_UNIT, USERNAME_BA_NO_UNIT
from configuration import PASSWORD_HA, PASSWORD_HA_NO_UNIT, PASSWORD_BA, PASSWORD_BA_NO_UNIT, CODE
import time


@allure.title("'Your units' is available if hyper admin has unit")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME_HA, PASSWORD_HA, CODE, 0),
])
def test_case1(setup, username, password, code, scenario):
    """
    Check if the button "Your units" is available if  hyper admin  has an unit
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    with allure.step("Step 1. Check if the button is available if logged in by hyperadmin"):
        assert "Your units" in setup.page_source, "'Your units' is not available if logged in by hyperadmin"


@allure.title("'Your units' is available if building admin has unit")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME_BA, PASSWORD_BA, CODE, 0),
])
def test_case2(setup, username, password, code, scenario):
    """
    Check if the button "Your units" is available if  building admin has an unit
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    with allure.step("Step 1. Check if the button is available if logged in by building admin"):
        assert "Your units" in setup.page_source, "'Your units' is not available if logged in by building admin"


@allure.title("'Your units' is not available if hyper admin has no units")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME_HA_NO_UNIT, PASSWORD_HA_NO_UNIT, CODE, 0),
])
def test_case3(setup, username, password, code, scenario):
    """
    Check if the button "Your units" is not available if  hyper admin has no units
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    with allure.step("Step 1. Check if the button is not available if  hyperadmin has no units"):
        assert "Your units" not in setup.page_source, "'Your units' is not available if logged in by hyper admin that has no units"


@allure.title("The button is not available if building admin has no units")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA_NO_UNIT, PASSWORD_BA_NO_UNIT, CODE),
])
def test_case4(setup, username, password, code):
    """
    Check if the button "Your units" is not available if  building admin has no units
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    with allure.step("Step 1. Check if the button is available if building admin has no units"):
        assert "Your units" not in setup.page_source, "'Your units' is not available if logged in by building admin that has no units"
