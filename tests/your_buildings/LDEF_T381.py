import allure
import pytest
from pom.selenium_functions import Signin
from pom.selenium_functions import Base2, Base
from pom.pages.your_building import Buildings
from pom.pages.your_units import Units
from pom.pages.logout_menu import Logout
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("View the list of doors")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Users/Any user/Access] View the list of doors
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Buildings(setup).your_units_button()
    Base2(setup).add_user()
    Units(setup).save_button()
    time.sleep(1)
    if "email must be unique" not in setup.page_source:
        with allure.step("Step 1. Check adding user"):
            assert "JohnDoe" in setup.page_source, "Error adding user"
        Logout(setup).access_tag()
        time.sleep(1)
        with allure.step("Step 2. Check presence of necessary tags and buttons"):
            assert "Users" and "Access" and "Doorbell" and "Settings" in setup.page_source, "Required tags  are missing"
            assert "Door Name" in setup.page_source, "Sub tag is missing"
    Base2(setup).delete_user()
    time.sleep(1)

