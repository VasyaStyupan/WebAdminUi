import allure
import pytest
from pom.selenium_functions import Signin, Base2, Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Configure 3 options of Automatic opening")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Doorbell] Configure 3 options of Automatic opening
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    # Base2(setup).doorbell_button()
    doorbell = Base2(setup).find_doorbell()
    Buildings(setup, doorbell).enter_doorbell_unit_level()
    time.sleep(1)
    Base2(setup).configure_ao()
    time.sleep(1)

