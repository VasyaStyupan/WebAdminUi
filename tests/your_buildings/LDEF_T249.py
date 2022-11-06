import time
import allure
import pytest
from pom.selenium_functions import Signin, Base2
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.logout_menu import Logout


@pytest.mark.skip
@allure.title("Personal Info. Edit personal data")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Profile] Personal Info. Edit personal data
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base2(setup).enter_the_user()
    time.sleep(1)
    Logout(setup, "First Name").edit_personal_info()
    Logout(setup, "Building").edit_personal_info()
    time.sleep(1)

# [Building/Users/Any user/Personal info] Edit Personal info with valid/not valid values
