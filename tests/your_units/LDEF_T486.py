import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME, PASSWORD, CODE
import time


@allure.title("Delete uploaded unit image")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME, PASSWORD, CODE)])
def test_case(setup, username, password, code):
    """
    [Units/Any unit from the list/Doorbell settings] Delete uploaded unit image
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup).delete_image()
    time.sleep(2)
    image_present = Base(setup).is_image_present()
    with allure.step("Step 1. Check for deleting image"):
        assert image_present is False, "Image not deleted"
