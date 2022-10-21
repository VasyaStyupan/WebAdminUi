import time
import allure
import pytest
from pom.selenium_functions import Signin
from pom.pages.mainscreen_page import MainScreen
from configuration import USERNAME, PASSWORD, CODE


@allure.title("View Search Result screen  (No result)")
@pytest.mark.parametrize('username, password, code, search_word', [
    (USERNAME, PASSWORD, CODE, " "),
    (USERNAME, PASSWORD, CODE, "#"),
    (USERNAME, PASSWORD, CODE, "&"),
])
def test_case(setup, username, password, code, search_word):
    """
    [Main screen/ Searching] View Search Result screen  (No result)
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    MainScreen(setup, search_word).search_bar()
    with allure.step("Step 1. Check if no results"):
        assert "No results found" in setup.page_source

