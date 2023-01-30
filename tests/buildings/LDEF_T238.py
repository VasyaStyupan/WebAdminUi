import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Remove all buttons from doorbell")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Doorbell/Doorbell name] Remove all buttons from doorbell
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).enter_the_doorbell()
    time.sleep(1)
    Buildings(setup).remove_buttons_from_doorbell().click()
    time.sleep(1)
    Buildings(setup).remove_buttons_from_doorbell().click()
    time.sleep(1)



