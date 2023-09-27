from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class SuccessLoginPage(BasePage):
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __success_login = (By.XPATH, "//h1[@class='post-title']")
    __logout_button = (By.LINK_TEXT, "Log out")

    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def header(self) -> str:
        return self._get_text(self.__success_login)

    def is_logout_btn_displayed(self) -> bool:
        return self._is_displayed(self.__logout_button)
