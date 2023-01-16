import allure
import pytest
from pom.selenium_functions import Signin
from configuration import USERNAME_UM, PASSWORD_UM, CODE
import time


@allure.title("View the tab Users")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_UM, PASSWORD_UM, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list] View the tab Users
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    time.sleep(1)
    with allure.step("Step 1. Check presence of necessary tags and buttons"):
        assert "Users" and "Access" and "Doorbell"  in setup.page_source, "Required tags  are missing"
        assert "Email" and "Username" and "First Name" and "Last Name" and "Phone" in setup.page_source, "Required tags  are missing"



