import allure
import pytest
from pom.selenium_functions import Signin, Base2, Units
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Change Unit Information")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Settings] Change Unit Information
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base2(setup).change_unit_info()
    Units(setup, 'Myunit').change_unit_name()
    time.sleep(1)
    with allure.step("Step 1. Check for change Unit name"):
        assert 'Myunit' in setup.page_source, "Name change error"
    Units(setup, 'dontdeletethisunit').change_unit_name()
