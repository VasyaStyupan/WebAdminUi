import allure
import pytest
from pom.selenium_functions import Signin, Base2
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("CCheck Access settings with RFID. Choose block adding RFID")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Doorbell/Doorbell name] Check Access settings with RFID. Choose block adding RFID and try to create
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base2(setup).enter_the_doorbell()
    Base2(setup).block_RFID_cards()
    time.sleep(1)

