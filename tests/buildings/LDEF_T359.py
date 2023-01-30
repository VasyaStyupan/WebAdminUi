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
    Choose another day
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).set_schedule_and_day()
    Buildings(setup).make_your_schedule().click()
    Buildings(setup).set_up_custom_days().click()
    Buildings(setup).choose_another_day().click()
    with allure.step("Step 1. Check on the Unit level message 'Automatic opening is not allowed on this day.'"):
        assert "Automatic opening is not allowed on this day." in setup.page_source, "Error choosing 'Schedule' option"

    time.sleep(1)
