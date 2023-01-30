import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Check changes doorbell while unchecked 'Show user image'")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Doorbell/Doorbell name] Check changes doorbell while unchecked 'Show user image'
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    doorbell = Base(setup).enter_the_doorbell()
    time.sleep(1)
    Buildings(setup).uncheck_show_user_image().click()
    time.sleep(1)
    Base(setup, doorbell).enter_doorbell_unit_level()
    Is_disable = Base(setup).check_user_image_disabled()
    time.sleep(1)
    with allure.step("Step 1. Check changes doorbell while unchecked 'Show user image'"):
        assert Is_disable is True, "Error while unchecked 'Show user image'"
    Base(setup).checkbox_recovery()



