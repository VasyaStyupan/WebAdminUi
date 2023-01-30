import allure
import pytest
from pom.selenium_functions import Signin, Base, Units
from configuration import USERNAME_UM, PASSWORD_UM, CODE, UNIT
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
    Base(setup, UNIT).select_unit()
    time.sleep(1)
    Units(setup).doorbell_tag().click()
    Units(setup).doorbell_item().click()
    Units(setup).check_button_visibility()
    time.sleep(1)



