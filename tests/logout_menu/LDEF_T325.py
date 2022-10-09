import time
import allure
import pytest
from pom.selenium_functions import Signin, Base
from configuration import USERNAME_BA, PASSWORD_BA, CODE
from pom.pages.logout_menu import UNITS, START_LOGOUT_MENU
from pom.pages.mainscreen_page import MainScreen


@allure.title("View screen Personal Info")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Menu/Profile] View screen Personal Info
    """
    Signin(setup, username, password, code).login_credentials()
    Signin(setup, username, password, code).login_code()
    MainScreen(setup).find_popup().click()
    Base(setup, START_LOGOUT_MENU[0], UNITS).logout_menu()
    time.sleep(1)
    with allure.step("Step 1. Check presence of necessary tags"):
        assert "Personal info" and "Units" and "Access Cards" and "Reset Password" in setup.page_source, "Required tags are missing"
    with allure.step("Step 2. Check presence of necessary fields"):
        assert "First Name" and "Last Name" and "Phone" and "Username" and "Email" in setup.page_source, "Required fields are missing"

# Добавить две кнопки
