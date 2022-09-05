import allure
import pytest
from pom.selenium_functions import Auth
from pom.pages.mainscreen_page import MainScreen
from configuration import USERNAME, PASSWORD, CODE


@allure.title("View Search Result screen  (No result)")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME, PASSWORD, CODE, 0)])  # 0 - positive, 1 - negative
def test_case(setup, username, password, code, scenario):
    """
    [Main screen/ Searching] View Search Result screen  (No result)
    """
    Auth(setup, username, password, code, scenario).log_in()
    MainScreen(setup).search_bar()
    with allure.step("Step 1. Check if no results"):
        assert "No results found" in setup.page_source
