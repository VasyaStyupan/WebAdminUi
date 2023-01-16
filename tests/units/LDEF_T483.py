import allure
import pytest
from pom.selenium_functions import Signin, Base, Units
from configuration import USERNAME_UM, PASSWORD_UM, CODE
import time


@allure.title("Check Doorbell Button Visibility")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_UM, PASSWORD_UM, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Doorbell] Check Doorbell Button Visibility
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Units(setup).doorbell_tag()
    Units(setup).doorbell_item()
    Base(setup).doorbell_visibility()
    time.sleep(1)



