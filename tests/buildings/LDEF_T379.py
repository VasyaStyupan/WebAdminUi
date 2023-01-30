import allure
import pytest
from pom.selenium_functions import Signin
from pom.selenium_functions import Base
from pom.pages.your_building import Buildings
from pom.pages.your_units import Units
from pom.pages.logout_menu import Logout
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Add user and set different options Doorbell button and digital keys")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Units/Any unit from the list/Users] Add user and set different options Doorbell button and digital keys
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Buildings(setup).your_units_button().click()
    Base(setup).add_user()
    Units(setup).save_button().click()
    Units(setup).mark_doorbell_digital_keys()
    time.sleep(1)
    if "email must be unique" not in setup.page_source:
        with allure.step("Step 1. Check adding user"):
            assert "JohnDoe" in setup.page_source, "Error adding user"
    Buildings(setup).users_tag().click()
    Buildings(setup, 'JohnDoe@mail.com').select_user()
    Logout(setup).units_tag().click()
    status = Base(setup).check_if_doorbell_button_inactive()
    with allure.step("Step 2. Check doorbell button in profile menu is inactive"):
        assert status is False, "Doorbell button is active"
    status = Base(setup).check_if_digital_key_inactive()
    with allure.step("Step 3. Check digital key in profile menu is inactive"):
        assert status is False, "Digital key is active"
    Base(setup).delete_user()
