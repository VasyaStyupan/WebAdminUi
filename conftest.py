import pytest
from selenium import webdriver
from configuration import BASE_URL
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service as chrome_serv
from selenium.webdriver.safari.options import Options as safari_options
from selenium.webdriver.safari.service import Service as safari_serv
from pathlib import Path


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: chrome or safari"
    )


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def get_webdriver(browser):
    if browser == 'chrome':
        options = chrome_options()
        options.add_argument('chrome')
        options.add_argument('--start-maximized')
        mypath = Path("chromedriver")
        path = mypath.home().joinpath("PycharmProjects", "WebAdminUi", "webdriver", "chromedriver")
        ser = chrome_serv(str(path))
        driver = webdriver.Chrome(service=ser, options=options)
        return driver
    if browser == 'safari':
        ser = safari_serv('/usr/bin/safaridriver')
        driver = webdriver.Safari(service=ser, options=safari_options())
        driver.set_window_size(1500, 900)
        return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = f"{BASE_URL}/login"
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
