import allure
import pytest
from pom.selenium_functions import Signin
from pom.selenium_functions import Base2
from pom.pages.your_building import Buildings
from pom.pages.your_units import Units
from pom.pages.logout_menu import Logout
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Add user and make this user a unit manager")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Units/Any unit from the list/Users] Add user and make this user a unit manager
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Buildings(setup).your_units_button()
    Base2(setup).add_user()
    Units(setup).save_button()
    time.sleep(1)
    with allure.step("Step 1. Check adding user"):
        assert "JohnDoe" in setup.page_source, "Error user created"
    Buildings(setup).users_tag()
    Buildings(setup, 'JohnDoe@mail.com').select_user()
    time.sleep(1)
    Logout(setup).units_tag()
    Logout(setup).mark_unit_manager()
    time.sleep(1)
    Base2(setup).delete_user()
    time.sleep(1)

