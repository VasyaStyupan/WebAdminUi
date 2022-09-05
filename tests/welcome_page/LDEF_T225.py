import allure
from pom.pages.login_page import LoginPage
from configuration import PRIVACY_URL_EN, TERMS_URL_EN, CONTACT_URL_EN


@allure.title("Privacy, Terms of use")
def test_case(setup):
    """
    Check Open Privacy, Terms of use
    """
    LoginPage(setup).search_privacy().click()
    current_url = setup.current_url
    with allure.step("Step 1. Open Privacy page"):
        assert PRIVACY_URL_EN == current_url, "Error reading Privacy page"

    LoginPage(setup).search_terms().click()
    current_url = setup.current_url
    with allure.step("Step 2. Open Terms of use page"):
        assert TERMS_URL_EN == current_url, "Error reading Terms of use page"
