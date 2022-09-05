import allure
from pom.pages.login_page import LoginPage
from pom.selenium_functions import Base
from configuration import PRIVACY_URL_EN, TERMS_URL_EN, CONTACT_URL_EN

@allure.title("Set language to English and check Privacy/Terms/Contact")
def test_case(setup):
    """
    Set En language, Click Privacy/ Terms of use /Contact us. Make sure that system redirect to English loc pages (NO/US server)
    """

    xpath = LoginPage(setup).change_lang_to_english()
    lang = Base(setup, xpath).select_popup_lang()
    with allure.step("Step 1. Change language to English"):
        assert lang.text == "English", "Unable to change language"

    LoginPage(setup).search_privacy().click()
    current_url = setup.current_url
    with allure.step("Step 2. Open Privacy page"):
        assert PRIVACY_URL_EN == current_url, "Error reading Privacy page"

    LoginPage(setup).search_terms().click()
    current_url = setup.current_url
    with allure.step("Step 3. Open Terms of use page"):
        assert TERMS_URL_EN == current_url, "Error reading Terms of use page"

    LoginPage(setup).search_contact().click()
    current_url = setup.current_url
    with allure.step("Step 4. Open Contact page"):
        assert CONTACT_URL_EN == current_url, "Error reading Contact page"





