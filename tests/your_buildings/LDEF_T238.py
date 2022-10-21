import allure
import pytest
from pom.selenium_functions import Signin, Base2
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Remove all button from doorbell")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Doorbell/Doorbell name] Remove all button from doorbell
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base2(setup).remove_buttons()
    Buildings(setup).remove_buttons_from_doorbell()
    time.sleep(1)



