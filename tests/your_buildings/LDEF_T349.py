import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Doorbell settings. Check Screen settings (volume)")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, browser, username, password, code):
    """
    [Building/Doorbell/Doorbell name] Doorbell settings. Check Screen settings (volume)
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).enter_the_doorbell()
    if browser == 'chrome':
        Base(setup).check_volume()
    time.sleep(1)

