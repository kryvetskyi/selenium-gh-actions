from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, url: str):
        self._driver = driver
        self._url = url

    def _open(self) -> None:
        self._driver.get(self._url)

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, timeout: int = 7) -> None:
        self._wait_until_visible(locator, timeout)
        self._find(locator).send_keys(text)

    def _clear(self, locator: tuple, timeout: int = 7):
        self._wait_until_visible(locator, timeout)
        self._find(locator).clear()

    def _wait_until_visible(self, locator: tuple, timeout: int = 7) -> None:
        wait = WebDriverWait(self._driver, timeout)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_present(self, locator: tuple, timeout: int = 7) -> None:
        wait = WebDriverWait(self._driver, timeout)
        wait.until(ec.presence_of_element_located(locator))

    def _wait_until_clickable(self, locator: tuple, timeout: int = 7) -> None:
        wait = WebDriverWait(self._driver, timeout)
        wait.until(ec.element_to_be_clickable(locator))

    def _wait_invisibility(self, locator: tuple, timeout: int = 7):
        wait = WebDriverWait(self._driver, timeout)
        wait.until(ec.invisibility_of_element_located(locator))

    def _click(self, locator: tuple) -> None:
        self._wait_until_visible(locator)
        self._find(locator).click()

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _get_text(self, locator: tuple, timeout: int = 7) -> str:
        self._wait_until_visible(locator, timeout)
        return self._find(locator).text
