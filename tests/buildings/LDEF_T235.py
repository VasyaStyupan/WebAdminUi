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
    # Change floors number
    floors_number = Buildings(setup, "5").change_list_of_floors_part1()
    time.sleep(1)
    with allure.step("Step 1. Check if floors number is changed"):
        assert 5 is floors_number, "Floors number is not changed"
    # Change abbreviation
    Buildings(setup, "changed").change_list_of_floors_part2()
    time.sleep(1)
    with allure.step("Step 2. Check if floors number is changed"):
        assert "changed" in setup.page_source, "Abbreviation is not changed"
    # Restore list of floors
    setup.refresh()
    Base(setup).enter_building_settings()
    Buildings(setup, "3").change_list_of_floors_part1()
    Buildings(setup, "abbreviation 1").change_list_of_floors_part2()



