import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Upload unit image")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Units/Any unit from the list/Doorbell] Upload unit image
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).check_your_units()
    Buildings(setup).your_units_button()
    Base(setup).upload_image()
    time.sleep(1)
    image_present = Base(setup).is_image_present()
    with allure.step("Step 1. Check for uploaded image"):
        assert image_present is True, "Image did not load"
