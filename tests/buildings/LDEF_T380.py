import allure
import pytest
from pom.selenium_functions import Signin
from pom.selenium_functions import Base
from pom.pages.your_building import Buildings
from pom.pages.your_units import Units
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Add user. View the list of created users")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Units/Any unit from the list/Users] Add user. View the list of created users
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Buildings(setup).your_units_button().click()
    Base(setup).add_user()
    Units(setup).save_button().click()
    time.sleep(1)
    with allure.step("Step 1. Check adding user"):
        assert "JohnDoe" in setup.page_source, "Error adding user"
    Buildings(setup).users_tag().click()
    time.sleep(1)
    if "email must be unique" not in setup.page_source:
        with allure.step("Step 2. Check presence of necessary tags and buttons"):
            assert "Users" and "Access" and "Doorbell" and "Settings" in setup.page_source, "Required tags  are missing"
            assert "Email" and "Username" and "First Name" and "Last Name" and "Phone" in setup.page_source, "Required tags  are missing"
            assert "Add user" in setup.page_source, "Button is missing"
    Base(setup).delete_user()

