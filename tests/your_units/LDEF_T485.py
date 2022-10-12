import allure
import pytest
from pom.selenium_functions import Signin, Base2
from configuration import USERNAME, PASSWORD, CODE
import time


@allure.title("Upload unit image")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME, PASSWORD, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Doorbell] Upload unit image
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base2(setup).upload_image()
    setup.refresh()
    image_present = Base2(setup).is_image_present()
    time.sleep(1)
    with allure.step("Step 1. Check for uploaded image"):
        assert image_present is True, "Image cannot be loaded"
