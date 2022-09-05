import allure
import pytest
from pom.selenium_functions import Auth
from configuration import USERNAME_HA, PASSWORD_HA, CODE, HOME_URL


@allure.title("Displays List of buildings/ Map/ Search/ Menu")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME_HA, PASSWORD_HA, CODE, 0)])  # 0 - positive, 1 - negative
def test_case(setup, username, password, code, scenario):
    """
    [Main screen] Hyper admin is logged. Displays List of buildings/ Map/ Search/ Menu
    """
    Auth(setup, username, password, code, scenario).log_in()
    current_url = setup.current_url
    with allure.step("Step 1. Check if you are on the main page"):
        assert f"{HOME_URL}list" == current_url, "Wrong page"

