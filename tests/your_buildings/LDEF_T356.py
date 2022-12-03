import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Set 'Schedule' and choose any day on Building level and 'Never allow' on Unit level")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [AO] Set 'Schedule' and choose any day on Building level and 'Never allow' on Unit level'
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).set_schedule_and_day()
    Buildings(setup).never_allow()
    time.sleep(1)
