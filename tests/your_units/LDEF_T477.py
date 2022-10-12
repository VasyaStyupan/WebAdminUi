import allure
import pytest
from pom.selenium_functions import Signin, Base2
from pom.selenium_functions import Hwa, Units
from configuration import USERNAME_BA, PASSWORD_BA, CODE, USERNAME_UM
import time


@allure.title("Add user and make this user a unit manager")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Users] Add user and make this user a unit manager
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base2(setup).add_user()
    Units(setup).make_unit_manager()
    Hwa(setup).signin_hwa()
    Hwa(setup, "JohnDoe@mail.com").search_hwa()
    Hwa(setup).delete_user_hwa()


