import time
import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_HA, PASSWORD_HA, CODE
from pom.pages.mainscreen_page import MainScreen


@allure.title("Map. Check the possibility to approximate/distance.")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_HA, PASSWORD_HA, CODE)])
def test_case(setup, username, password, code):
    """
    [Main screen] Map. Сheck the possibility to approximate/distance. Choose building on map
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    MainScreen(setup).map_plus()
    MainScreen(setup).map_plus()
    MainScreen(setup).map_minus()
    time.sleep(1)
    MainScreen(setup).map_minus()



