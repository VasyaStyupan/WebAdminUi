import allure
import pytest
from pom.selenium_functions import Signin
from pom.pages.your_building import Buildings
from pom.pages.logout_menu import Logout
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("View the list of Doors")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Units/Any unit from the list/Access] View the list of Doors
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Buildings(setup).your_units_button()
    Logout(setup).access_tag()
    with allure.step("Step 1. Check presence of necessary tags"):
        assert "Users" and "Access" and "Doorbell" and "Settings" in setup.page_source, "Required tags are missing"
        assert "Door Name" in setup.page_source, "'Door Name' tag is missing"
    time.sleep(1)

