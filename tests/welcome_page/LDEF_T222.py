import allure
import pytest
from pom.selenium_functions import Signin
from configuration import USERNAME, PASSWORD, BASE_URL, EMAIL


@allure.title("Login with valid credentials")
@pytest.mark.parametrize('username, password, scenario', [
    (USERNAME, PASSWORD, 0)])  # 0 - positive, 1 - negative
def test_case1(setup, username, password, scenario):
    """"
    [Welcome page] Login with valid credentials
    """
    current_url = Signin(setup, username, password).login_credentials()
    with allure.step("Step 1. Username and password entry"):
        assert f"{BASE_URL}/auth-code" == current_url, "Access error"


@allure.title("Login with valid credentials")
@pytest.mark.parametrize('username, password, scenario', [
    (EMAIL, PASSWORD, 0)])  # 0 - positive, 1 - negative
def test_case2(setup, username, password, scenario):
    """"
    [Welcome page] Login with valid email and password
    """
    current_url = Signin(setup, username, password).login_credentials()
    with allure.step("Step 1. Username and password entry"):
        assert f"{BASE_URL}/auth-code" == current_url, "Access error"


@allure.title("Login with invalid credentials")
@pytest.mark.parametrize('username, password, scenario', [
    (EMAIL, PASSWORD[:-1], 1)])  # 0 - positive, 1 - negative
def test_case3(setup, username, password, scenario):
    """"
    [Welcome page] Login with valid email and invalid password
    """
    current_url = Signin(setup, username, password).login_credentials()
    with allure.step("Step 1. Username and password entry"):
        assert "Wrong username or password" in setup.page_source and f"{BASE_URL}/login" == current_url, "Missing notification"
        assert f"{BASE_URL}/login" == current_url, "Access error"


@allure.title("Login with valid credentials")
@pytest.mark.parametrize('username, password, scenario', [
    (USERNAME.upper(), PASSWORD, 0)])  # 0 - positive, 1 - negative
def test_case4(setup, username, password, scenario):
    """"
    [Welcome page] Login with valid username in upper case and valid password
    """
    current_url = Signin(setup, username, password).login_credentials()
    with allure.step("Step 1. Username and password entry"):
        assert f"{BASE_URL}/auth-code" == current_url, "Access error"


@allure.title("Login with valid credentials")
@pytest.mark.parametrize('username, password, scenario', [
    (f" {USERNAME} ", PASSWORD, 0)])  # 0 - positive, 1 - negative
def test_case5(setup, username, password, scenario):
    """"
    [Welcome page] Login with valid username with spaces and valid password
    """
    current_url = Signin(setup, username, password).login_credentials()
    with allure.step("Step 1. Username and password entry"):
        assert f"{BASE_URL}/auth-code" == current_url, "Access error"


@allure.title("Login with valid credentials")
@pytest.mark.parametrize('username, password, scenario', [
    (USERNAME, f" {PASSWORD} ", 0)])  # 0 - positive, 1 - negative
def test_case6(setup, username, password, scenario):
    """"
    [Welcome page] Login with valid username and valid password with spaces
    """
    current_url = Signin(setup, username, password).login_credentials()
    with allure.step("Step 1. Username and password entry"):
        assert f"{BASE_URL}/auth-code" == current_url, "Access error"


@allure.title("Login with invalid credentials")
@pytest.mark.parametrize('username, password, scenario', [
    (USERNAME, PASSWORD.upper(), 1)])  # 0 - positive, 1 - negative
def test_case7(setup, username, password, scenario):
    """"
    [Welcome page] Login with valid username and invalid password (upper case)
    """
    current_url = Signin(setup, username, password).login_credentials()
    with allure.step("Step 1. Username and password entry"):
        assert "Wrong username or password" in setup.page_source and f"{BASE_URL}/login" == current_url, "Missing notification"
        assert f"{BASE_URL}/login" == current_url, "Access error"


@allure.title("Login with invalid credentials")
@pytest.mark.parametrize('username, password, scenario', [
    (USERNAME, PASSWORD[:-1], 1)])  # 0 - positive, 1 - negative
def test_case8(setup, username, password, scenario):
    """"
    [Welcome page] Login with valid username and invalid password
    """
    current_url = Signin(setup, username, password).login_credentials()
    with allure.step("Step 1. Username and password entry"):
        assert "Wrong username or password" in setup.page_source and f"{BASE_URL}/login" == current_url, "Missing notification"
        assert f"{BASE_URL}/login" == current_url, "Access error"


@allure.title("Login with invalid credentials")
@pytest.mark.parametrize('username, password, scenario', [
    (USERNAME, PASSWORD[:5], 1)])  # 0 - positive, 1 - negative
def test_case9(setup, username, password, scenario):
    """"
    [Welcome page] Login with valid username and invalid password (less than 6 characters)
    """
    current_url = Signin(setup, username, password).login_credentials()
    with allure.step("Step 1. Username and password entry"):
        assert "must NOT have fewer than 6 characters" in setup.page_source and f"{BASE_URL}/login" == current_url, "Missing notification"
        assert f"{BASE_URL}/login" == current_url, "Access error"


@allure.title("Login with invalid credentials")
@pytest.mark.parametrize('username, password, scenario', [
    (USERNAME[:-1], PASSWORD, 1)])  # 0 - positive, 1 - negative
def test_case10(setup, username, password, scenario):
    """"
    [Welcome page] Login with invalid username and valid password
    """
    current_url = Signin(setup, username, password).login_credentials()
    with allure.step("Step 1. Username and password entry"):
        assert "Wrong username or password" in setup.page_source and f"{BASE_URL}/login" == current_url, "Missing notification"
        assert f"{BASE_URL}/login" == current_url, "Access error"


@allure.title("Login with invalid credentials")
@pytest.mark.parametrize('username, password, scenario', [
    (USERNAME[:5], PASSWORD, 1)])  # 0 - positive, 1 - negative
def test_case11(setup, username, password, scenario):
    """"
    [Welcome page] Login with invalid username (less than 6 characters) and valid password
    """
    current_url = Signin(setup, username, password).login_credentials()
    with allure.step("Step 1. Username and password entry"):
        assert "Wrong username or password" in setup.page_source and f"{BASE_URL}/login" == current_url, "Missing notification"
        assert f"{BASE_URL}/login" == current_url, "Access error"


@allure.title("Login with invalid credentials")
@pytest.mark.parametrize('username, password, scenario', [
    ("", "", 1)])  # 0 - positive, 1 - negative
def test_case12(setup, username, password, scenario):
    """"
    [Welcome page] Login with empty spaces
    """
    current_url = Signin(setup, username, password).login_credentials()
    with allure.step("Step 1. Username and password entry"):
        assert f"{BASE_URL}/login" == current_url, "Access error"


@allure.title("Login with invalid credentials")
@pytest.mark.parametrize('username, password, scenario', [
    ("", PASSWORD, 1)])  # 0 - positive, 1 - negative
def test_case13(setup, username, password, scenario):
    """"
    [Welcome page] Login with invalid username (empty space) and valid password
    """
    current_url = Signin(setup, username, password).login_credentials()
    with allure.step("Step 1. Username and password entry"):
        assert f"{BASE_URL}/login" == current_url, "Access error"


@allure.title("Login with invalid credentials")
@pytest.mark.parametrize('username, password, scenario', [
    (USERNAME, "", 1)])  # 0 - positive, 1 - negative
def test_case14(setup, username, password, scenario):
    """"
    [Welcome page] Login with valid username and invalid password (empty space)
    """
    current_url = Signin(setup, username, password).login_credentials()
    with allure.step("Step 1. Username and password entry"):
        assert f"{BASE_URL}/login" == current_url, "Access error"


