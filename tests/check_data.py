import time
from pom.selenium_functions import Signin
from configuration import USERNAME_BA, PASSWORD_BA, CODE, USERNAME_UM, USERNAME_UO, BASE_URL, UNIT, SIMPLE_USER
from pom.pages.logout_menu import UNITS, START_LOGOUT_MENU, Logout, ACCESS_CARDS
from pom.pages.your_units import Units
from pom.pages.your_building import Buildings
from pom.selenium_functions import Base


def test_case(setup):
    """
    Check and fix test data
    """
    Signin(setup, USERNAME_BA, PASSWORD_BA).login_credentials()
    Signin(setup, USERNAME_BA, PASSWORD_BA, CODE).login_code()
    Base(setup).fix_your_units()
    Buildings(setup).your_buildings_button()
    Base(setup).enter_the_unit()
    Base(setup, SIMPLE_USER).select_user()
    Buildings(setup).access_cards()
    time.sleep(1)
    if "CardName" in setup.page_source:
        Base(setup, START_LOGOUT_MENU[0], ACCESS_CARDS).delete_card()

    Base(setup).restore_unit_owner()
    Buildings(setup).your_buildings_button()
    setup.refresh()
    Base(setup).checkbox_recovery()
    time.sleep(1)
