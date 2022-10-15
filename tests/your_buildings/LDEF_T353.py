import allure
import pytest
from pom.selenium_functions import Signin, Base2
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE, BASE_URL
import time


@allure.title("Set 'Always allow' on Building level and 'Never allow' on Unit level")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [AO] Set 'Always allow' on Building level and 'Never allow' on Unit level
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    doorbell = Base2(setup).select_always_allow()
    Buildings(setup, doorbell).enter_doorbell_unit_level()
    Buildings(setup).never_allow()
    time.sleep(1)



