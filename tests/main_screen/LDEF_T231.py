import allure
import pytest
from pom.selenium_functions import Auth
from pom.pages.mainscreen_page import MainScreen
from configuration import USERNAME, PASSWORD, CODE, SIMPLE_USER


@allure.title("View Search Result screen")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME, PASSWORD, CODE, 0)])  # 0 - positive, 1 - negative
def test_case(setup, username, password, code, scenario):
    """
    [Main screen/ Searching] View Search Result screen
    """
    Auth(setup, username, password, code, scenario).log_in()
    MainScreen(setup, SIMPLE_USER).search_bar()
    MainScreen(setup, SIMPLE_USER).search_user().click()

    with allure.step("Step 1. Check if user found"):
        assert "Personal Info" in setup.page_source

