import allure
import pytest
from pom.selenium_functions import Auth
from configuration import USERNAME, PASSWORD, CODE


@allure.title("Authorization, positive scenario")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME, PASSWORD, CODE, 0)])  # 0 - positive, 1 - negative
def test_case1(setup, username, password, code, scenario):
    """
    Log in with valid login & valid password
    """
    Auth(setup, username, password, code, scenario).log_in()


@allure.title("Authorization, positive scenario")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME.upper(), PASSWORD, CODE, 0)])  # 0 - positive, 1 - negative
def test_case2(setup, username, password, code, scenario):
    """
    Log in with valid login in upper case & valid password
    """
    Auth(setup, username, password, code, scenario).log_in()


@allure.title("Authorization, positive scenario")
@pytest.mark.parametrize('username, password, code, scenario', [
    (f" {USERNAME} ", PASSWORD, CODE, 0)])  # 0 - positive, 1 - negative
def test_case3(setup, username, password, code, scenario):
    """
    Log in with valid login with spaces & valid password
    """
    Auth(setup, username, password, code, scenario).log_in()


@allure.title("Authorization, positive scenario")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME, f" {PASSWORD} ", CODE, 0)])  # 0 - positive, 1 - negative
def test_case4(setup, username, password, code, scenario):
    """
    Log in with valid login  & valid password with spaces
    """
    Auth(setup, username, password, code, scenario).log_in()


@allure.title("Authorization, negative scenario")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME, PASSWORD.upper(), CODE, 1)])  # 0 - positive, 1 - negative
def test_case5(setup, username, password, code, scenario):
    """
    Log in with valid login  & valid password in upper case
    """
    Auth(setup, username, password, code, scenario).log_in()


@allure.title("Authorization, negative scenario")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME, PASSWORD[:-1], CODE, 1)])  # 0 - positive, 1 - negative
def test_case6(setup, username, password, code, scenario):
    """
    Log in with valid login & invalid password
    """
    Auth(setup, username, password, code, scenario).log_in()


@allure.title("Authorization, negative scenario")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME, PASSWORD[:5], CODE, 1)])  # 0 - positive, 1 - negative
def test_case7(setup, username, password, code, scenario):
    """
    Log in with valid login  & invalid password (less than 6 characters)
    """
    Auth(setup, username, password, code, scenario).log_in()


@allure.title("Authorization, negative scenario")
@pytest.mark.parametrize('username, password, code, scenario', [
    (USERNAME[:-1], PASSWORD, CODE, 1)])  # 0 - positive, 1 - negative
def test_case8(setup, username, password, code, scenario):
    """
    Log in with invalid login & valid password
    """
    Auth(setup, username, password, code, scenario).log_in()


@allure.title("Authorization, negative scenario")
@pytest.mark.parametrize('username, password, code, scenario', [
    ("", "", CODE, 1)])  # 0 - positive, 1 - negative
def test_case9(setup, username, password, code, scenario):
    """
    Log in with empty fields
    """
    Auth(setup, username, password, code, scenario).log_in()


@allure.title("Authorization, negative scenario")
@pytest.mark.parametrize('username, password, code, scenario', [
    ("", PASSWORD, CODE, 1)])  # 0 - positive, 1 - negative
def test_case10(setup, username, password, code, scenario):
    """
    Log in with empty login  & valid password
    """
    Auth(setup, username, password, code, scenario).log_in()


@allure.title("Authorization, negative scenario")
@pytest.mark.parametrize('username, password, code, scenario', [
    (PASSWORD, "", CODE, 1)])  # 0 - positive, 1 - negative
def test_case11(setup, username, password, code, scenario):
    """
    Log in with valid login  & empty password
    """
    Auth(setup, username, password, code, scenario).log_in()
