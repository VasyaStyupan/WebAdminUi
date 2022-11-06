import allure
import pytest
from pom.selenium_functions import Signin, Base2
from configuration import USERNAME_BA, PASSWORD_BA, CODE, BASE_URL
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
    Base2(setup).check_doorbell_display_conditions()
    setup.get(f"{BASE_URL}/building/list")
    Base2(setup).check_doorbell_display_conditions()
    time.sleep(1)


