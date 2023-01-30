import allure
import pytest
from pom.selenium_functions import Signin, Units, Base
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE, UNIT, UID
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
    Buildings(setup).your_units_button().click()
    Buildings(setup).building_address()
    Units(setup).settings().click()
    Base(setup, 'test_uid', 'Myunit', 'floor 2').change_unit_information()
    time.sleep(1)
    with allure.step("Step 1. Check for change Unit information"):
        assert 'test_uid' and 'Myunit' in setup.page_source, "Change information error"
    Base(setup, UID, UNIT, 'floor 1').change_unit_information()
    time.sleep(1)
