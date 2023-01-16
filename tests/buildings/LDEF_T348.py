import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Check on doorbell and device inability to choose individual mode")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building] Doorbell settings. Family mode. Check on doorbell and device inability to choose individual mode (cloned)
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).enter_the_doorbell()
    i = 0
    while i < 3:
        Buildings(setup).check_family_mode()
        time.sleep(1)
        with allure.step("Step 1. Check notification while switching family mode"):
            assert "Doorbell was updated successfully!", "Missing notification"
        i += 1
    Buildings(setup).checkbox_recovery_after_selection()
