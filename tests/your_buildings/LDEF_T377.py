import allure
import pytest
from pom.selenium_functions import Signin
from pom.selenium_functions import Base
from pom.pages.your_building import Buildings
from pom.pages.your_units import Units
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Add user with only Email filled")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Units/Any unit from the list/Users] Add user with only Email filled
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Buildings(setup).your_units_button()
    Base(setup).add_user_with_only_email()
    Units(setup).fill_lang()
    Units(setup).save_button()
    time.sleep(1)
    if "email must be unique" not in setup.page_source:
        with allure.step("Step 1. Check adding user"):
            assert "JohnDoe" in setup.page_source, "Error adding user"
    Base(setup).delete_user()


