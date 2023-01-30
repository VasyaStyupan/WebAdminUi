import allure
import pytest
from pom.selenium_functions import Signin
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("View the tag Users")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Units/Any unit from the list] View the tag Users
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Buildings(setup).your_units_button().click()
    time.sleep(1)
    with allure.step("Step 1. Check presence of necessary tags"):
        assert "Users" and "Access" and "Doorbell" and "Settings" in setup.page_source, "Required tags are missing"
        assert "Email" and "Username" and "First Name" and "Last Name" and "Phone" in setup.page_source, "Submenu tags are missing"

