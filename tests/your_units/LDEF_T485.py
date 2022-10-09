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
    time.sleep(1)
    Base2(setup).upload_image()
    time.sleep(1)
    # with allure.step("Step 1. Check UX translation with Norsk loc"):
    #     assert "Velg språk" in setup.page_source, "Switch to Norsk does not work"
