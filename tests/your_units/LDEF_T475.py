import allure
import pytest
from pom.selenium_functions import Signin, Base2
from pom.selenium_functions import Hwa, Units
from pom.pages.your_building import Buildings
from configuration import USERNAME_UM, PASSWORD_UM, CODE
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
    Base2(setup).add_user()
    Units(setup).save_button()
    Buildings(setup).users_tag()
    # Base2(setup).enter_the_unit()
    time.sleep(1)
    with allure.step("Step 1. Check adding user"):
        assert "JohnDoe@mail.com" in setup.page_source, "User not created"
    Base2(setup).delete_user()

