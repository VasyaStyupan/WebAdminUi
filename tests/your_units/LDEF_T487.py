import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.pages.your_units import Units
from configuration import USERNAME_UM, PASSWORD_UM, CODE
import time


@allure.title("Configure 3 options of Automatic opening")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_UM, PASSWORD_UM, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Doorbell] Configure 3 options of Automatic opening
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Units(setup).doorbell_button()
    Units(setup).doorbell_item()
    Base(setup).configure_ao()
    time.sleep(1)

