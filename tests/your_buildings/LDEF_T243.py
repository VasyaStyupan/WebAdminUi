import allure
import pytest
from pom.selenium_functions import Signin, Units
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Change Unit Information")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Units/Any unit from the list/Settings] Change Unit Information
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Buildings(setup).your_units_button()
    address, unit = Buildings(setup).building_address()
    Units(setup).settings()
    Buildings(setup, 'Myunit').change_unit_name()
    time.sleep(1)
    with allure.step("Step 1. Check for change Unit name"):
        assert 'Myunit' in setup.page_source, "Name change error"
    Buildings(setup, unit).change_unit_name()
    time.sleep(1)
