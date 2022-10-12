import allure
import pytest
from pom.selenium_functions import Signin, Base2, Hwa, Units
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Add user and set different options Doorbell button and digital keys")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Users] Add user and set different options Doorbell button and digital keys
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base2(setup).add_user()
    Units(setup).mark_doorbell_digital_keys()
    Hwa(setup).signin_hwa()
    Hwa(setup, "JohnDoe@mail.com").search_hwa()
    Hwa(setup).delete_user_hwa()
