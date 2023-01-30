import allure
import pytest
from pom.selenium_functions import Signin, Base, Units
from configuration import USERNAME_UM, PASSWORD_UM, CODE, UNIT
import time


@allure.title("Change Unit Information")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_UM, PASSWORD_UM, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Settings] Change Unit Information
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, UNIT).select_unit()
    Units(setup).settings().click()
    Base(setup, 'Myunit').change_unit_name()
    time.sleep(1)
    with allure.step("Step 1. Check for change Unit name"):
        assert 'Myunit' in setup.page_source, "Name change error"
    Base(setup, f'{UNIT}').change_unit_name()
    time.sleep(1)
