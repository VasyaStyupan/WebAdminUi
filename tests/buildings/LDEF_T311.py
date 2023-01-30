import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.selenium_functions import Units
from configuration import USERNAME_BA, PASSWORD_BA, CODE, UID
import time


@allure.title("Add/Edit user. Input Phone number with spaces")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Users] Add/Edit user. Input Phone number with spaces
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, UID).enter_the_unit()
    Base(setup).add_user_phone_with_spaces()
    current_url = setup.current_url
    Units(setup).save_button().click()
    time.sleep(1)
    with allure.step("Step 1. Check adding user phone number with spaces"):
        assert current_url == setup.current_url, "Error adding user"
    Base(setup).delete_user()
