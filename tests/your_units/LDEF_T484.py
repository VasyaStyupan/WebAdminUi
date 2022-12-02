import allure
import pytest
from pom.selenium_functions import Signin, Base2
from pom.pages.your_units import Units
from configuration import USERNAME_UM, PASSWORD_UM, CODE
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
    Units(setup).doorbell_button()
    Units(setup).doorbell_item()
    Base2(setup).doorbell_layouts()
    time.sleep(3)

