import allure
import pytest
from pom.selenium_functions import Signin, Base
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
    Base(setup).enter_the_unit()
    Base(setup).add_user()
    Units(setup).save_button()
    Buildings(setup).users_tag()
    Buildings(setup).delete_user_from_unit()
    time.sleep(1)
    with allure.step("Step 1. Check deleting user"):
        assert "JohnDoe@mail.com" not in setup.page_source, "User is not deleted"
    Base(setup).delete_user()



