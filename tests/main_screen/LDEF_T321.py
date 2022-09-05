import pytest
import allure
from pom.selenium_functions import Auth
from configuration import USERNAME, PASSWORD, CODE
import time



@allure.title("Check Hovers for strings of Buildings")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME, PASSWORD, CODE, 0)])  # 0 - positive, 1 - negative
def test_case(setup, username, password, code, scenario):
    """
    Check Hovers for strings of Buildings
    """
    Auth(setup, username, password, code, scenario).log_in()
    Auth(setup, username, password, code, scenario).hover_building()
    time.sleep(1)

