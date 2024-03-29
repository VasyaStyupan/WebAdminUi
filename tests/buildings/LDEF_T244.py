import allure
import pytest
from pom.selenium_functions import Signin, Base, Units
from pom.pages.your_building import Buildings
from pom.pages.logout_menu import START_LOGOUT_MENU, UNITS
from configuration import USERNAME_BA, PASSWORD_BA, CODE, USERNAME_UO
import time


@allure.title("Change unit owner")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Units/Any unit from the list/Settings] Change unit owner
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Buildings(setup).your_units_button().click()
    element = Units(setup).settings()
    time.sleep(1)  # safari
    element.click()
    first_name, last_name = Base(setup, USERNAME_BA).change_unit_owner()
    time.sleep(1)
    with allure.step("Step 1. Check if unit owner is changed"):
        assert first_name and last_name in setup.page_source, "Change unit owner error"
    Base(setup, USERNAME_UO).change_unit_owner()
    setup.refresh()
    Base(setup, START_LOGOUT_MENU[0], UNITS).mark_unit_manager()



