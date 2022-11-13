import allure
import pytest
from pom.selenium_functions import Signin
from pom.selenium_functions import Units, Base2
from configuration import USERNAME_UM, PASSWORD_UM, CODE
import time


@allure.title("Add user with only Email filled")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_UM, PASSWORD_UM, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Users] Add user with only Email filled
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base2(setup).add_user_with_only_email()
    time.sleep(5)
    Units(setup).save_button()
    time.sleep(1)
    with allure.step("Step 1. Check adding user"):
        assert "JohnDoe@mail.com" in setup.page_source, "User not created"
    Base2(setup).delete_user()

