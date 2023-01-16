import allure
from pom.pages.login_page import LoginPage
from configuration import CONTACT_URL_EN


@allure.title("Contact us")
def test_case(setup):
    """
    Contact us. Сheck what goes on the site and opens the form
    """
    LoginPage(setup).search_contact().click()
    current_url = setup.current_url
    with allure.step("Step 1. Open Contact page"):
        assert CONTACT_URL_EN in current_url, "Error reading Contact page"
