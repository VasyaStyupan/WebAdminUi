server = 1  # 1 - DEV, 2 - STAGE
if server == 2:
    BASE_URL = "https://dev-webadmin.defigo.no"
    BASE_URL2 = "https://webrtc.defigohome.com"
    HYPER_ADMIN_URL = "https://dev-hwa.defigo.no/"
    LOGIN_URL_US = "https://webadmin.getdefigo.com/login"
    USERNAME_HA = "test@ha.dev"
    BUILDING = " 300, 90 "
else:
    BASE_URL = "https://stage-webadmin.defigo.no"
    BASE_URL2 = "https://stage.defigohome.com"
    HYPER_ADMIN_URL = "https://stage-hwa.defigo.no/"
    LOGIN_URL_US = "https://stage-webadmin.defigoaccess.com/login"
    USERNAME_HA = "test@ha.stage"
    BUILDING = " Europaplein, 24 "

LOGIN_URL = f"{BASE_URL}/login"
CODE_URL = f"{BASE_URL}/auth-code"
HOME_URL = f"{BASE_URL}/building/"
MAIN_URL = f"{BASE_URL}/building/list"

PRIVACY_URL_EN = f"{BASE_URL2}/privacy-policy?lang=en"
TERMS_URL_EN = f"{BASE_URL2}/terms?lang=en"
CONTACT_URL_EN = "https://www.getdefigo.com/contact-us"
PRIVACY_URL_NOR = f"{BASE_URL2}/privacy-policy?lang=nb"
TERMS_URL_NOR = f"{BASE_URL2}/terms?lang=nb"
CONTACT_URL_NOR = "https://www.getdefigo.com/no/contact-us"

PASSWORD_HA = "Qwerty1"
USERNAME_HA_NO_UNIT = "ha@no.units"
PASSWORD_HA_NO_UNIT = "Qwerty1"
USERNAME_BA = "building@ma.nager"
PASSWORD_BA = "Qwerty1"
USERNAME_BA_NO_UNIT = "ba@no.units"
PASSWORD_BA_NO_UNIT = "Qwerty1"
USERNAME_UO = "owner@te.st"
PASSWORD_UO = "Qwerty123"
USERNAME_UM = "manager@te.st"
PASSWORD_UM = "Qwerty123"
EMAIL_UM = "new@email.com"
SIMPLE_USER = "simple_user"
SIMPLE_PASS = "Qwerty123"

USERNAME = USERNAME_UM
PASSWORD = PASSWORD_UM
EMAIL = EMAIL_UM
CODE = "1111"
UNIT = "Dontdeletethisunit"
UID = 'fortest'


