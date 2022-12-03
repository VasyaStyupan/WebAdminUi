import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE, DOORBELL
import time


@allure.title("Change doorbell name")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Doorbell/Doorbell name] Change doorbell name
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).change_doorbell_name()
    time.sleep(1)
    with allure.step("Step 1. Check if doorbell name is changed"):
        assert "My Doorbell Name" in setup.page_source, "Change Doorbell name error"
    Buildings(setup, DOORBELL).input_doorbell_name()

