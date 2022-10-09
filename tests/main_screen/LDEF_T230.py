import time

import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_HA, PASSWORD_HA, CODE
from pom.pages.mainscreen_page import MainScreen


@allure.title("Map. Сheck the possibility to approximate/distance.")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_HA, PASSWORD_HA, CODE)])
def test_case(setup, username, password, code):
    """
    [Main screen] Map. Сheck the possibility to approximate/distance. Choose building on map
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    MainScreen(setup).map_plus()
    time.sleep(1)
    MainScreen(setup).map_minus()
    MainScreen(setup).map_minus()
    time.sleep(1)

    # with allure.step("Step 1. Check if you are on the main page"):
    #     assert f"{BASE_URL}/building/list" == current_url, "Wrong page"
    #     assert "Building address" and "Units" and "Doors" and "Users" in setup.page_source, "Wrong page"
