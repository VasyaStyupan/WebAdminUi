import allure
import pytest
from pom.selenium_functions import Signin, Base, Units
from configuration import USERNAME_UM, PASSWORD_UM, CODE
import time


@allure.title("Add user and set different options Doorbell button and digital keys")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_UM, PASSWORD_UM, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Users] Add user and set different options Doorbell button and digital keys
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).add_user()
    Units(setup).mark_doorbell_digital_keys()
    time.sleep(1)
    Base(setup).delete_user()
