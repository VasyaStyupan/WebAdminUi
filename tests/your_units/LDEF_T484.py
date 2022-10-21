import allure
import pytest
from pom.selenium_functions import Signin, Base2
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Check Doorbell Button Layouts")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Doorbell] Check Doorbell Button Layouts
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base2(setup).doorbell_button()
    Base2(setup).doorbell_layouts()
    time.sleep(1)

