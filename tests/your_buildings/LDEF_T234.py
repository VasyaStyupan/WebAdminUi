import allure
import pytest
from pom.selenium_functions import Signin, Base2
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Сheck whether the selected (not selected) unit manager functions work correctly")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Settings] Сheck whether the selected (not selected) unit manager functions work correctly
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base2(setup).enter_building_settings()
    Base2(setup).check_um_functions()
    time.sleep(1)




