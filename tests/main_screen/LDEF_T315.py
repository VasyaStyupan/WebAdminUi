import pytest
import allure
from pom.selenium_functions import Signin, Base
from configuration import CODE, USERNAME_BA, PASSWORD_BA


@allure.title("View the Main screen when BA is logged")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Main screen] View the Main screen when BA is logged
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    with allure.step("Step 1. Check if user can see 'Building manager', 'Your buildings', 'Building address','Units',"
                     " 'Doors', 'Users' "):
        assert "Building manager" and 'Your buildings' and 'Building address' and 'Units' and 'Doors' and 'Users' in \
               setup.page_source, "Wrong user page"

