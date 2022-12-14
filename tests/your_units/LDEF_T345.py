import allure
import pytest
from pom.selenium_functions import Signin
from configuration import USERNAME, PASSWORD, CODE
import time


@allure.title("View the screen with units where logged user is it")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME, PASSWORD, CODE)])
def test_case(setup, username, password, code):
    """
    [Your units] View the screen with units where logged user is it
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    time.sleep(1)
    with allure.step("Step 1. Check presence of necessary users and tags"):
        assert username  in setup.page_source, "Required users  are missing"
        assert "Users" and "Your units" and "Access" and "Doorbell" in setup.page_source, "Required tags are missing"



