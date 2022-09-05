import allure
from pom.pages.login_page import LoginPage
from pom.selenium_functions import Base


@allure.title("Change server No/Us")
def test_case(setup):
    """
    Check if server can switch from No to Us
    """
    xpath = LoginPage(setup).select_server_US()
    US = Base(setup, xpath).popup_server()
    with allure.step("Step 1. Change server to US"):
        assert US.text == "US", "Can`t change server to US"
