import allure
from pom.pages.login_page import LoginPage, CHANGE_LANG_TO_ENGLISH
from pom.selenium_functions import Base
from configuration import PRIVACY_URL_EN, TERMS_URL_EN, CONTACT_URL_EN

"""
Set En language, Click Privacy/ Terms of use /Contact us. Make sure that system redirect to English loc pages (NO/US server)
"""


@allure.title("Set language to English and check Privacy/Terms/Contact")
def test_step1(setup):
    lang = Base(setup, CHANGE_LANG_TO_ENGLISH).select_popup_lang()
    with allure.step("Step 1. Change language to English"):
        assert lang.text == "English", "Unable to change language"


def test_step2(setup):
    LoginPage(setup).search_privacy().click()
    current_url = setup.current_url
    with allure.step("Step 2. Open Privacy page"):
        assert PRIVACY_URL_EN == current_url, "Error reading Privacy page"


def test_step3(setup):
    LoginPage(setup).search_terms().click()
    current_url = setup.current_url
    with allure.step("Step 3. Open Terms of use page"):
        assert TERMS_URL_EN == current_url, "Error reading Terms of use page"


def test_step4(setup):
    LoginPage(setup).search_contact().click()
    current_url = setup.current_url
    with allure.step("Step 4. Open Contact page"):
        assert CONTACT_URL_EN in current_url, "Error reading Contact page"
