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
    Buildings(setup).your_units_button()
    Units(setup).doorbell_button()
    Units(setup).doorbell_item()
    Base(setup).doorbell_layouts()
    time.sleep(1)
