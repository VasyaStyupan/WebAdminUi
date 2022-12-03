import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.selenium_functions import Buildings, Units
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Upload unit image")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Doorbell] Upload unit image
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Buildings(setup).your_units_button()
    time.sleep(1)
    Base(setup).upload_image()
    setup.refresh()
    image_present = Base(setup).is_image_present()
    time.sleep(1)
    with allure.step("Step 1. Check for uploaded image"):
        assert image_present is True, "Image did not load"
    Buildings(setup).your_units_button()
    Base(setup).delete_image()
    time.sleep(1)

