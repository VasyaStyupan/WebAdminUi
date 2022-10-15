import allure
import pytest
from pom.selenium_functions import Signin, Base2
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE, BASE_URL
import time


@allure.title("Forbid unit manager to upload unit image")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Doorbell/Doorbell name] Unit manager policy control. Forbid unit manager to upload unit image
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base2(setup).forbid_unit_image()
    setup.refresh()
    Buildings(setup).forbid_upload_unit_image()
    time.sleep(1)


