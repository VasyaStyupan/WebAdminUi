import allure
import pytest
from pom.selenium_functions import Signin, Base2
from configuration import USERNAME, PASSWORD, CODE
import time


@allure.title("View the list of Doors")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME, PASSWORD, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Access] View the list of Doors
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base2(setup).access_tab()
    with allure.step("Step 1. Check presence of necessary tags"):
        assert "Users" and "Access" and "Doorbell" and "Door Name" in setup.page_source, "Required tags  are missing"

