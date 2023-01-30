import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE, DOORBELL
import time


@allure.title("Change doorbell name")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, browser, username, password, code):
    """
    [Building/Doorbell/Doorbell name] Change doorbell name
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).enter_the_doorbell()
    Base(setup, "  ").input_doorbell_name()
    with allure.step("Step 1. Check input empty field"):
        assert "must NOT have fewer than 1 characters" in setup.page_source, "Error while input empty field"
    save = Base(setup, "My").input_doorbell_name()
    with allure.step("Step 2. Check input empty field"):
        assert save is True, "Error while input name with 2 characters"
    doorbell_name = Buildings(setup, 50).generate_random_string()
    save = Base(setup, doorbell_name).input_doorbell_name()
    with allure.step("Step 3. Check field length 50 characters"):
        assert save is True, "Error while input name with 50 characters"
    doorbell_name = Buildings(setup, 51).generate_random_string()
    Base(setup, doorbell_name).input_doorbell_name()
    with allure.step("Step 4. Check field length 50 characters"):
        assert "must NOT have more than 50 characters" in setup.page_source, "Error while input name with 51 characters"
    Base(setup, "My Doorbell Name").input_doorbell_name()
    time.sleep(1)
    with allure.step("Step 5. Check if doorbell name is changed"):
        assert "Change doorbell name" in setup.page_source, "Change Doorbell name error"
    Base(setup, DOORBELL).input_doorbell_name()

