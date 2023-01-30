import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.selenium_functions import Units
from configuration import USERNAME_BA, PASSWORD_BA, CODE, UID
import time


@allure.title("Add user without providing phone number")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Units/Users] Add user without providing phone number
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, UID).enter_the_unit()
    Base(setup).add_user_without_phone()
    current_url = setup.current_url
    try:
        Units(setup).save_button()
    except Exception:
        pass
    with allure.step("Step 1. Check adding user without providing phone number"):
        assert current_url == setup.current_url, "Error. User must not be added"

