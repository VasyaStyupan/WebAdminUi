import time
import allure
import pytest
from pom.selenium_functions import Signin, Base
from pom.pages.your_building import Buildings, FIRST_LINE, TAGS, SUB_TAGS
from configuration import USERNAME_BA, PASSWORD_BA, CODE


@allure.title("Check the sorting")
@pytest.mark.parametrize('username, password, code', [
    (USERNAME_BA, PASSWORD_BA, CODE)])
def test_case(setup, username, password, code):
    """
    [Building] Units/Users/Access/Doorbell. List of units/users... of the selected building.
    Check the sorting
    """
    Signin(setup, username, password).login_credentials()
    Signin(setup, username, password, code).login_code()
    Buildings(setup).select_building()
    for j in TAGS:
        tag = TAGS.index(j)
        time.sleep(1)
        Buildings(setup, TAGS[tag]).select_tag()
        for i in SUB_TAGS[tag]:
            index = SUB_TAGS[tag].index(i)
            time.sleep(0.5)
            if SUB_TAGS[tag][index] != "" and SUB_TAGS[tag][index] != "//span[text()=' GID ']":
                items_list = Base(setup, FIRST_LINE[tag], SUB_TAGS[tag][index], index).sorting()
                with allure.step("Step 1. Check if reverse sort working"):
                    assert items_list == sorted(items_list, key=str.upper,
                                                reverse=True), "Reverse sort is not working"
                items_list = Base(setup, FIRST_LINE[tag], SUB_TAGS[tag][index], index).sorting()
                with allure.step("Step 2. Check if sort by field is working"):
                    assert items_list == sorted(items_list, key=str.upper), "Sort is not working"
