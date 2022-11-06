import allure
import pytest
from pom.selenium_functions import Signin, Base2
from pom.pages.your_building import Buildings
from configuration import USERNAME_BA, PASSWORD_BA, CODE
import time


@allure.title("Check changes doorbell while unchecked 'Enable search field'")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Doorbell/Doorbell name] Check changes doorbell while unchecked 'Enable search field'
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base2(setup).enable_search_field()
    Base2(setup).checkbox_recovery()
    time.sleep(1)



