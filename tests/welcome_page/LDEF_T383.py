import allure
from pom.pages.login_page import LoginPage, CHANGE_LANG_TO_NORSK
from pom.selenium_functions import Base
from configuration import PRIVACY_URL_NOR, TERMS_URL_NOR, CONTACT_URL_NOR, CONTACT_URL_NOR2
import time

"""
Set language to Norwegian and check Privacy/Terms/Contact
"""


@allure.title("Set language to Norwegian and check Privacy/Terms/Contact")
def test_step1(setup):
    Base(setup, CHANGE_LANG_TO_NORSK).select_popup_lang()
    time.sleep(1)
    with allure.step("Step 1. Check language switch to Norwegian"):
        assert "Personvern" in setup.page_source, "Unable to change language"
    save_url = setup.current_url
    LoginPage(setup).search_privacy_nor().click()
    current_url = setup.current_url
    time.sleep(2)
    with allure.step("Step 2. Check Privacy page"):
        assert PRIVACY_URL_NOR == current_url, "Error reading Privacy page"
    setup.get(save_url)
    LoginPage(setup).search_terms_nor().click()
    current_url = setup.current_url
    time.sleep(2)
    with allure.step("Step 3. Check Terms of use page"):
        assert TERMS_URL_NOR == current_url, "Error reading Terms of use page"
    setup.get(save_url)
    LoginPage(setup).search_contact_nor().click()
    current_url = setup.current_url
    time.sleep(2)
    with allure.step("Step 4. Check Contact page"):
        assert CONTACT_URL_NOR or CONTACT_URL_NOR2 == current_url, "Error reading Contact page"
