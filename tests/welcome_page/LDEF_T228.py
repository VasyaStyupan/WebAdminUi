import allure
from pom.pages.login_page import LoginPage
from pom.selenium_functions import Base


@allure.title("Check language switch to English/Norsk/Svenska")
def test_case(setup):
    """
    Check language switch to English/Norsk/Svenska
    """

    xpath = LoginPage(setup).change_lang_to_norsk()
    lang = Base(setup, xpath).select_popup_lang()
    with allure.step("Step 1. Change language to Norwegian"):
        assert lang.text == "Norsk", "Unable to change language"

    xpath = LoginPage(setup).change_lang_to_svenska()
    lang = Base(setup, xpath).select_popup_lang()
    with allure.step("Step 2. Change language to Swedish"):
        assert lang.text == "Svenska", "Unable to change language"
