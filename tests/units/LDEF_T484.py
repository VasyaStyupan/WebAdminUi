import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.pages.your_units import Units
from configuration import USERNAME_UM, PASSWORD_UM, CODE, UNIT
import time


@allure.title("Check Doorbell Button Layouts")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_UM, PASSWORD_UM, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Doorbell] Check Doorbell Button Layouts
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, UNIT).select_unit()
    time.sleep(1)
    Units(setup).doorbell_tag().click()
    Units(setup).doorbell_item().click()
    Base(setup).doorbell_layouts()


