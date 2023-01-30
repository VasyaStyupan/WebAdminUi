import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.selenium_functions import Units
from pom.pages.your_building import Buildings
from configuration import USERNAME_UM, PASSWORD_UM, CODE, UNIT
import time


@allure.title("Add user with all fields filled")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_UM, PASSWORD_UM, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Users] Add user with all fields filled
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, UNIT).select_unit()
    Base(setup).add_user()
    Units(setup).save_button().click()
    time.sleep(1)
    Buildings(setup).users_tag()
    time.sleep(1)
    with allure.step("Step 1. Check adding user"):
        assert "JohnDoe@mail.com" in setup.page_source, "User is not created"
    Base(setup).delete_user()

