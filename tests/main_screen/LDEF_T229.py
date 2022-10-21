import allure
import pytest
from pom.selenium_functions import Signin
from configuration import USERNAME_HA, PASSWORD_HA, CODE, BASE_URL


@allure.title("Displays List of buildings/ Map/ Search/ Menu")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_HA, PASSWORD_HA, CODE)])
def test_case(setup, username, password, code):
    """
    [Main screen] Hyper admin is logged. Displays List of buildings/ Map/ Search/ Menu
    """
    Signin(setup, username, password).login_credentials()
    current_url = Signin(setup, username, password, code).login_code()
    with allure.step("Step 1. Check if you are on the main page"):
        assert f"{BASE_URL}/building/list" == current_url, "Wrong page"
        assert "Building address" and "Units" and "Doors" and "Users" in setup.page_source, "Wrong page"


