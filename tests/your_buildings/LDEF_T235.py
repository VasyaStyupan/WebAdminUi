import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Changing list of floors")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Settings] Changing list of floors
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).enter_building_settings()
    time.sleep(1)
    Buildings(setup, "5").change_list_of_floors()
    time.sleep(1)
    with allure.step("Step 1. Check if floors number is changed"):
        assert "5" in setup.page_source, "Floors number is not changed"
    Buildings(setup, "3").change_list_of_floors()
    time.sleep(1)
