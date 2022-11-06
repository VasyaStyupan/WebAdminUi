import allure
import pytest
from pom.selenium_functions import Signin, Base, Units
from pom.pages.your_building import Buildings, FIRST_LINE, FIRST_LINE_FOLLOWING, TAGS, SUBMENU_TAGS
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
    Buildings(setup).select_any_building()
    for j in TAGS:
        tag = TAGS.index(j)
        Buildings(setup, TAGS[tag]).select_tag()
        for i in SUBMENU_TAGS[tag]:
            index = SUBMENU_TAGS[tag].index(i)
            items_list = Base(setup, FIRST_LINE[tag], FIRST_LINE_FOLLOWING[tag], SUBMENU_TAGS[tag][index],
                              index).hover()
            with allure.step("Step 1. Check if reverse sort by field 'Building address' working"):
                assert items_list == sorted(items_list, key=lambda c: c.upper(),
                                            reverse=True), "Reverse sort is not working"
            items_list = Base(setup, FIRST_LINE[tag], FIRST_LINE_FOLLOWING[tag], SUBMENU_TAGS[tag][index],
                              index).hover()
            with allure.step("Step 2. Check if sort by field 'Building address' working"):
                assert items_list == sorted(items_list, key=lambda c: c.upper()), "Sort is not working"

