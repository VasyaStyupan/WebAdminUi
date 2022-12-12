import allure
import pytest
from pom.selenium_functions import Signin, Base, Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Configure 3 options of Automatic opening")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Units/Any unit from the list/Doorbell] Configure 3 options of Automatic opening
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).check_your_units()
    Buildings(setup).your_units_button()
    Buildings(setup).doorbell_button()
    Buildings(setup).select_any_doorbell()
    Base(setup).configure_ao()
    time.sleep(1)
