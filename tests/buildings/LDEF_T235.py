import allure
import pytest
from pom.selenium_functions import Signin, Base
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
    floors_number = Base(setup, "5").change_list_of_floors_part1()
    time.sleep(1)
    with allure.step("Step 1. Check if floors number is changed"):
        assert floors_number == 5, "Floors number is not changed"
    # Change abbreviation
    Base(setup, "changed").change_list_of_floors_part2()
    time.sleep(1)
    with allure.step("Step 2. Check if abbreviation is changed"):
        assert "changed" in setup.page_source, "Abbreviation is not changed"
    # Restore list of floors
    Base(setup).enter_building_settings()
    Base(setup, "3").change_list_of_floors_part1()
    Base(setup, "abbreviation 1").change_list_of_floors_part2()




