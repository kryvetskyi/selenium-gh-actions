import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()       # to parametrize use @pytest.fixture(params=["chrome", "firefox", ...])
def driver(request):    # and driver = request.param
    driver = request.config.getoption("--browser")
    if driver == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
    elif driver == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
    else:
        raise TypeError("Wrong browser. Supported are: ['chrome', 'firefox', 'brave']")
    yield driver

    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Please provide correct browser"
    )
