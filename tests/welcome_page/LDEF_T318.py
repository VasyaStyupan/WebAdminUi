import allure
import pytest
from pom.selenium_functions import Auth
from configuration import SIMPLE_USER, SIMPLE_PASS, CODE


@allure.title("Try to login with credentials of the simple User")
@pytest.mark.parametrize('username, password, code, scenario', [
    (SIMPLE_USER, SIMPLE_PASS, CODE, 1)])  # 0 - positive, 1 - negative
def test_case(setup, username, password, code, scenario):
    """
    Check Open Privacy, Terms of use
    """
    Auth(setup, username, password, code, scenario).log_in()




