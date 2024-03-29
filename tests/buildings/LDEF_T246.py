import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.pages.your_units import Units
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Check Doorbell Button Layouts")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Units/Any unit from the list/Doorbell] Check Doorbell Button Layouts
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).check_your_units()
    Buildings(setup).your_units_button().click()
    time.sleep(1)
    Units(setup).doorbell_tag().click()
    time.sleep(1)
    Units(setup).doorbell_item().click()
    time.sleep(1)
    Base(setup).doorbell_layouts()
    time.sleep(1)
