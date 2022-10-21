import allure
import pytest
from pom.selenium_functions import Signin
from configuration import SIMPLE_USER, SIMPLE_PASS, CODE


@allure.title("Try to login with credentials of the simple User")
@pytest.mark.parametrize('username, password', [
    (SIMPLE_USER, SIMPLE_PASS)])
def test_case(setup, username, password):
    """
    Check Open Privacy, Terms of use
    """
    current_url = Signin(setup, username, password).login_credentials()
    assert current_url != 200, "Wrong username or password"





