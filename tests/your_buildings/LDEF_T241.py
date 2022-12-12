import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE, USERNAME_UM, PASSWORD_UM
import time


@allure.title("Forbid unit manager to upload unit image")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Doorbell/Doorbell name] Unit manager policy control. Forbid unit manager to upload unit image
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    doorbell = Base(setup).forbid_unit_image()
    time.sleep(3)
    Base(setup).logout()
    Signin(setup, USERNAME_UM, PASSWORD_UM).login_credentials()
    Signin(setup, USERNAME_UM, PASSWORD_UM, code).login_code()
    Base(setup, doorbell).enter_doorbell_um()
    time.sleep(1)
    with allure.step("Step 1. Check forbidding for unit manager to upload unit image"):
        assert "This image will be displayed" not in setup.page_source, "Error forbidding to upload unit image"
    Base(setup).logout()
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).forbid_unit_image()
    Base(setup).checkbox_recovery()


