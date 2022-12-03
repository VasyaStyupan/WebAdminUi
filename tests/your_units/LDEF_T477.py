import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.selenium_functions import Units
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Add user and make this user a unit manager")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Users] Add user and make this user a unit manager
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).select_your_units()
    Base(setup).add_user()
    Units(setup).make_unit_manager()
    time.sleep(1)
    Base(setup).delete_user()

