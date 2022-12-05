import time
import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE, SIMPLE_USER
from pom.pages.logout_menu import Logout


@allure.title("Check Digital keys")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Users/Any user/Units] Check Digital keys
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).enter_the_unit()
    Base(setup, SIMPLE_USER).select_user()
    Logout(setup).units_tag()
    i = 0
    while i < 3:
        Logout(setup).mark_digital_key()
        time.sleep(1)
        i += 1
