import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME, PASSWORD, CODE
import time


@allure.title("Upload unit image")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME, PASSWORD, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Doorbell] Upload unit image
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).upload_image()
    setup.refresh()
    image_present = Base(setup).is_image_present()
    with allure.step("Step 1. Check for uploaded image"):
        assert image_present is True, "Image did not load"
