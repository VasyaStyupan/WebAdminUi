import allure
import pytest
from pom.selenium_functions import Signin, Base, Base2
from pom.selenium_functions import Units
from configuration import USERNAME_BA, PASSWORD_BA, CODE
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
    Base2(setup).enter_the_unit()
    Base2(setup).add_user_without_phone()
    current_url = setup.current_url
    Units(setup).save_button()
    time.sleep(1)
    with allure.step("Step 1. Check adding user without providing phone number"):
        assert current_url == setup.current_url, "Error. User must not be added"

