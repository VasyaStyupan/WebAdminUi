import allure
import pytest
from pom.selenium_functions import Signin, Base2
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE, BASE_URL
import time


@allure.title("Check option 'Never allow'")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [AO] Choose option 'Never allow' and check on the Unit level message 'Automatic opening is not allowed in this building.
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    doorbell = Base2(setup).select_never_allow()
    Buildings(setup, doorbell).enter_doorbell_unit_level()
    time.sleep(1)
    with allure.step("Step 1. Check on the Unit level message 'Automatic opening is not allowed in this building.'"):
        assert "Automatic opening is not allowed in this building." in setup.page_source, "Error choosing 'Never allow' option"
    setup.get(f"{BASE_URL}/building/list")
    Base2(setup).select_schedule()






