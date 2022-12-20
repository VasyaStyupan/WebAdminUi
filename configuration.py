#################################################
# Select server (set 1, 2 or 3)
server = 2
# 1 - DEV, 2 - STAGE EU, 3 - STAGE US
#################################################

if server == 1:
    BASE_URL = "https://dev-webadmin.defigo.no"
    BASE_URL2 = "https://webrtc.defigohome.com"
    HYPER_ADMIN_URL = "https://dev-hwa.defigo.no/"
    LOGIN_URL_US = "webadmin.getdefigo.com/login"
    USERNAME_HA = "test@ha.dev"
    PASSWORD_HA = "Qwerty1"
    USERNAME_BA = "building@ma.nager"
    PASSWORD_BA = "Qwerty1"
    USERNAME_UO = "owner@te.st"
    PASSWORD_UO = "Qwerty123"
    USERNAME_UM = "manager@te.st"
    PASSWORD_UM = "Qwerty123"
    BUILDING = "300, 90"
    UNIT = "Dontdeletethisunit"
    DOORBELL = "Vet Test Emak 1"
    UID = 'fortest'
elif server == 2:
    BASE_URL = "https://stage-webadmin.defigo.no"
    BASE_URL2 = "https://stage.defigohome.com"
    HYPER_ADMIN_URL = "https://stage-hwa.defigo.no/"
    LOGIN_URL_US = "https://stage-webadmin.defigoaccess.com/login"
    USERNAME_HA = "test@ha.stage"
    PASSWORD_HA = "Qwerty1"
    USERNAME_BA = "building@ma.nager"
    PASSWORD_BA = "Qwerty1"
    USERNAME_UO = "owner@te.st"
    PASSWORD_UO = "Qwerty123"
    USERNAME_UM = "manager@te.st"
    PASSWORD_UM = "Qwerty123"
    BUILDING = "Europaplein, 24"
    UNIT = "Dontdeletethisunit"
    UID = 'fortest'
    DOORBELL = "Vet Test Emak 1"
else:
    BASE_URL = "https://stage-webadmin.defigoaccess.com"
    BASE_URL2 = "https://stage.defigoaccess.com"
    HYPER_ADMIN_URL = "https://stage-hwa.defigoaccess.com/"
    LOGIN_URL_US = "https://stage-webadmin.defigoaccess.com/login"
    USERNAME_HA = "ha@us.test"
    PASSWORD_HA = "Qwerty123"
    USERNAME_BA = "ba@with.build"
    PASSWORD_BA = "Qwerty123"
    USERNAME_UO = "unit_owner"
    PASSWORD_UO = "Qwerty123"
    USERNAME_UM = "unit_manager"
    PASSWORD_UM = "Qwerty123"
    BUILDING = "Deep, 00"
    UNIT = "Dontdeletethisunit"
    UID = 'fortest'
    DOORBELL = "EMAK1 US"
########################################################
LOGIN_URL = f"{BASE_URL}/login"
CODE_URL = f"{BASE_URL}/auth-code"
HOME_URL = f"{BASE_URL}/building/"
MAIN_URL = f"{BASE_URL}/building/list"
#########################################################
PRIVACY_URL_EN = f"{BASE_URL2}/privacy-policy?lang=en"
TERMS_URL_EN = f"{BASE_URL2}/terms?lang=en"
CONTACT_URL_EN = "getdefigo.com/contact-us"
PRIVACY_URL_NOR = f"{BASE_URL2}/privacy-policy?lang=nb"
TERMS_URL_NOR = f"{BASE_URL2}/terms?lang=nb"
CONTACT_URL_NOR = "https://www.getdefigo.com/no/contact-us"
CONTACT_URL_NOR2 = "https://getdefigo.com/no/contact-us/"
###########################################################
SIMPLE_USER = "simple_user"
SIMPLE_PASS = "Qwerty123"
USERNAME = USERNAME_UM
PASSWORD = PASSWORD_UM
CODE = "1111"
EMAIL_UM = "new@email.com"
EMAIL = EMAIL_UM
############################################################
USERNAME_HA_NO_UNIT = "ha@no.units"
PASSWORD_HA_NO_UNIT = "Qwerty1"
USERNAME_BA_NO_UNIT = "ba@no.units"
PASSWORD_BA_NO_UNIT = "Qwerty1"
