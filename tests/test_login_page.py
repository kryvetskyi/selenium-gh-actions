import pytest
from page_objects.login_page import LoginPage
from page_objects.successfull_login import SuccessLoginPage


class TestLogin:
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver, "https://practicetestautomation.com/practice-test-login/")
        login_page._open()
        login_page.execute_login("student", "Password123")

        login_success = SuccessLoginPage(driver, "https://practicetestautomation.com/logged-in-successfully/")
        assert login_success.current_url == login_success.expected_url,  "Wrong url address"
        assert login_success.header == "Logged In Successfully", "Wrong header text"
        assert login_success.is_logout_btn_displayed(), "Log out button is not displayed"

    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, error_message",
                             [("incorrect_username", "Password123", "Your username is invalid!"),
                              ("student", "incorrect_password", "Your password is invalid!"),
                              ])
    def test_negative_login(self, driver, username, password, error_message):
        login_page = LoginPage(driver, "https://practicetestautomation.com/practice-test-login/")
        login_page._open()
        login_page.execute_login(username, password)
        assert login_page.get_error_message() == error_message, "Wrong error message"
