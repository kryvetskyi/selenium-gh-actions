from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __username_field = (By.ID, "username")
    __password_field = (By.XPATH, "//input[@id='password']")
    __submit_btn = (By.CLASS_NAME, "btn")
    __error_message = (By.ID, "error")

    def execute_login(self, username: str, password: str):
        self._type(self.__username_field, username)
        self._type(self.__password_field, password)
        self._click(self.__submit_btn)

    def get_error_message(self) -> str:
        return self._get_text(self.__error_message, timeout=2)
