import time
import allure
import pytest
from pom.selenium_functions import Signin, Base, Units
from pom.pages.your_building import Buildings, FIRST_LINE, TAGS, SUB_TAGS
from configuration import USERNAME_BA, PASSWORD_BA, CODE


@allure.title("Check scroll")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Chosen Building screen] Check scroll on the every tab units/ users/access/doorbell
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Buildings(setup).select_any_building()
    for j in TAGS:
        tag = TAGS.index(j)
        Buildings(setup, TAGS[tag]).select_tag()
        Base(setup, FIRST_LINE[tag]).scrolling()
        setup.refresh()
    time.sleep(1)

