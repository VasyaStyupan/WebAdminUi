import allure
import pytest
from pom.selenium_functions import Signin, Base, Units
from configuration import USERNAME_BA, PASSWORD_BA, CODE, USERNAME_UM, PASSWORD_UM
import time


@allure.title("Check on doorbell display choosing conditions")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Doorbell/Doorbell name] Unit manager policy control. Check on doorbell display choosing conditions
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).check_doorbell_display_conditions()
    time.sleep(4)
    Base(setup).logout()
    Signin(setup, USERNAME_UM, PASSWORD_UM, code).login_credentials()
    Signin(setup, USERNAME_UM, PASSWORD_UM, code).login_code()
    Units(setup).doorbell_tag()
    Units(setup).doorbell_item()
    enabled = Units(setup).user_image_visible()
    with allure.step("Step 1. Check if user image is disabled"):
        assert enabled is False, "Error. User image is enabled"
    enabled = Units(setup).unit_image_visible()
    with allure.step("Step 2. Check if unit image is disabled"):
        assert enabled is False, "Error. Unit image is enabled"
    image = Base(setup).is_image_present()
    with allure.step("Step 3. Check if unit image is not uploaded"):
        assert image is False, "Error. Unit image uploaded"
    with allure.step("Step 4. Check if automatic opening is not allowed"):
        assert "Never allow" not in setup.page_source, "Error. Automatic opening is allowed"
    Base(setup).logout()
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).checkbox_recovery()




