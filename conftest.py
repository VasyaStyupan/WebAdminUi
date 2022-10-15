import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service
from configuration import BASE_URL, HYPER_ADMIN_URL


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Use headless if you do not need a browser UI
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1650,900')
    # options.add_argument('--window-size=900,700')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    # ser = Service('/Users/driver/chromedriver')
    ser = Service('/Users/StyupanVasyl/WebAdminUi/webdriver/chromedriver')
    driver = webdriver.Chrome(service=ser, options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = f"{BASE_URL}/login"
    if request.cls is not None:
        request.cls.driver = driver
    driver.implicitly_wait(10)
    driver.get(url)
    yield driver
    driver.quit()

