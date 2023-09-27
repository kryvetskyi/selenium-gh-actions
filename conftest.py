from pathlib import Path

import pytest
from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def get_chrome_path_binary():
    project_root = Path(__file__).resolve().parent
    chrome_executable_path = project_root / "binaries" / "chrome-mac-arm64" / "Google Chrome for Testing.app" / \
                                            "Contents" / "MacOS" / "Google Chrome for Testing"
    return str(chrome_executable_path)


@pytest.fixture()
def driver(request):
    options = webdriver.ChromeOptions()
    options.binary_location = get_chrome_path_binary()

    driver = request.config.getoption("--browser")
    if driver == "chrome":
        driver = webdriver.Chrome(options=options)
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
