import pytest
from selenium import webdriver
from configuration import BASE_URL, BROWSER
if BROWSER == 1:
    from selenium.webdriver.chrome.options import Options as chrome_options
    from selenium.webdriver.chrome.service import Service
else:
    from selenium.webdriver.safari.options import Options as safari_options
    from selenium.webdriver.safari.service import Service
from pathlib import Path


@pytest.fixture
def get_webdriver():
    if BROWSER == 1:
        options = chrome_options()
        options.add_argument('chrome')
        options.add_argument('--start-maximized')
        mypath = Path("chromedriver")
        path = mypath.home().joinpath("PycharmProjects", "WebAdminUi", "webdriver", "chromedriver")
        ser = Service(str(path))
        driver = webdriver.Chrome(service=ser, options=options)
    else:
        ser = Service('/usr/bin/safaridriver')
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
