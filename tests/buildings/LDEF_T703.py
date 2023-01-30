import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.selenium_functions import Units
from configuration import USERNAME_BA, PASSWORD_BA, CODE, UID
from pom.pages.your_building import Buildings
import time


@allure.title(" Add user with existed email/phone/personal data")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building/Units/Any unit from the list/Users] Add user with existed email/phone/personal data
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Base(setup, UID).enter_the_unit()
    Base(setup).add_user()
    Units(setup).save_button().click()
    time.sleep(1)
    Buildings(setup).users_tag().click()
    Base(setup).add_user_with_old_email_and_new_data()
    Units(setup).save_button().click()
    time.sleep(1)
    Buildings(setup).users_tag().click()
    time.sleep(1)
    with allure.step("Step 1. Check adding user"):
        assert "John" and "Doe" in setup.page_source, "User is not deleted"
        assert "User was successfully added to the unit" in setup.page_source, "Missing notification"
    Base(setup).delete_user()
