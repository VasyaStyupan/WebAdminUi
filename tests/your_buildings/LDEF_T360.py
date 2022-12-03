import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Set 'Schedule' and choose any day on Building level and 'Make your schedule' on Unit level")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [AO] Set 'Schedule' and choose any day on Building level and 'Make your schedule' on Unit level
    Choose same day/time
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).set_schedule_and_day()
    Buildings(setup).make_your_schedule()
    Buildings(setup).set_up_custom_days()
    Buildings(setup).choose_day()
    Buildings(setup).save_day()
    time.sleep(1)
