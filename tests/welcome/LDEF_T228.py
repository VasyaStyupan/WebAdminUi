import allure
from pom.pages.login_page import CHANGE_LANG_TO_ENGLISH, CHANGE_LANG_TO_NORSK, CHANGE_LANG_TO_SVENSKA, CHANGE_LANG_TO_DEUTSCH
from pom.selenium_functions import Base


@allure.title("Check language switch to English/Norsk/Svenska/Deutsch")
def test_case(setup):
    """
    Check language switch to English/Norsk/Svenska/Deutsch
    """

    lang = Base(setup, CHANGE_LANG_TO_ENGLISH).select_popup_lang()
    with allure.step("Step 1. Change language to English"):
        assert lang.text == "English" and "English" in setup.page_source , "Unable to change language"

    lang = Base(setup, CHANGE_LANG_TO_NORSK).select_popup_lang()
    with allure.step("Step 2. Change language to Norwegian"):
        assert lang.text == "Norsk" and "Norsk" in setup.page_source, "Unable to change language"

    lang = Base(setup, CHANGE_LANG_TO_SVENSKA).select_popup_lang()
    with allure.step("Step 3. Change language to Swedish"):
        assert lang.text == "Svenska" and "Svenska" in setup.page_source, "Unable to change language"

    lang = Base(setup, CHANGE_LANG_TO_DEUTSCH).select_popup_lang()
    with allure.step("Step 4. Change language to Deutsch"):
        assert lang.text == "Deutsch" and "Deutsch" in setup.page_source, "Unable to change language"
