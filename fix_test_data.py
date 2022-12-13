import time
from pom.selenium_functions import Signin
from configuration import USERNAME_BA, PASSWORD_BA, CODE, SIMPLE_USER
from pom.pages.logout_menu import START_LOGOUT_MENU, ACCESS_CARDS
from pom.pages.your_building import Buildings
from pom.selenium_functions import Base


def test_case(setup):
    """
    Check and fix test data
    """
    Signin(setup, USERNAME_BA, PASSWORD_BA).login_credentials()
    Signin(setup, USERNAME_BA, PASSWORD_BA, CODE).login_code()
    Base(setup).fix_your_units()  # check and fix if building manager is removed from the unit
    Base(setup).fix_access_card()  # check and fix if SIMPLE USERs access card is not deleted
    Base(setup).restore_unit_owner()  # check and fix if UNIT OWNER is not linked to unit
    Buildings(setup).your_buildings_button()
    Base(setup).checkbox_recovery()   # check and fix checkbox in doorbell chapter
    Buildings(setup).your_buildings_button()
    Base(setup).checkbox_settings()   # check and fix checkbox in settings chapter
