import allure
import pytest
from pom.selenium_functions import Signin, Base2
from pom.selenium_functions import Units
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.your_building import Buildings
import time


@allure.title("Remove a user")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Users/Any user/Units] Remove a user
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base2(setup).enter_the_unit()
    Base2(setup).add_user()
    Units(setup).save_button()
    Buildings(setup).users_tag()
    time.sleep(1)
    with allure.step("Step 1. Check adding user"):
        assert "JohnDoe@mail.com" in setup.page_source, "User not created"
    Buildings(setup).delete_user_from_unit()
    Base2(setup).delete_user()


