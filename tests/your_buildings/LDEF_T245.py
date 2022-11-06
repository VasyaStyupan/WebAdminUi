import allure
import pytest
from pom.selenium_functions import Signin, Base2, Units, Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Check Doorbell Button Visibility")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Doorbell] Check Doorbell Button Visibility
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Buildings(setup).your_units_button()
    Units(setup).doorbell_button()
    Units(setup).doorbell_item()
    Base2(setup).doorbell_visibility()
    time.sleep(1)
