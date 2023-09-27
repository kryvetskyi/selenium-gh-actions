import pytest
from page_objects.exceptions import ExceptionsPage


class TestExceptions:
    @pytest.mark.exception
    def test_no_such_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver, "https://practicetestautomation.com/practice-test-exceptions/")
        exceptions_page._open()
        exceptions_page.click_add_btn()
        assert exceptions_page.is_row2_displayed(), "Second row does not displayed"

    @pytest.mark.exception
    def test_element_not_interactable_exception(self, driver):
        exceptions_page = ExceptionsPage(driver, "https://practicetestautomation.com/practice-test-exceptions/")
        exceptions_page._open()
        exceptions_page.click_add_btn()
        exceptions_page.add_second_dish("pasta")
        assert exceptions_page.get_confirmation_msg() == "Row 2 was saved", "Row 2 was not saved"

    @pytest.mark.exception
    def test_invalid_element_state_exception(self, driver):
        exceptions_page = ExceptionsPage(driver, "https://practicetestautomation.com/practice-test-exceptions/")
        exceptions_page._open()
        exceptions_page.modify_row1("pasta")
        assert exceptions_page.get_confirmation_msg() == "Row 1 was saved", "Row 1 was not saved"

    @pytest.mark.exception
    def test_stale_reference_exception(self, driver):
        exceptions_page = ExceptionsPage(driver, "https://practicetestautomation.com/practice-test-exceptions/")
        exceptions_page._open()
        exceptions_page.click_add_btn()
        assert not exceptions_page.check_invisibility(), "Element is visible but should not"

    @pytest.mark.exception
    def test_timeout_exception(self, driver):
        exceptions_page = ExceptionsPage(driver, "https://practicetestautomation.com/practice-test-exceptions/")
        exceptions_page._open()
        exceptions_page.click_add_btn()
        assert exceptions_page.is_row2_displayed(), "Second row does not displayed"
