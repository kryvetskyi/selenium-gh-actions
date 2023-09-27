from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    __add_btn = (By.ID, "add_btn")
    __row2_input = (By.XPATH, '//div[@id="row2"]/input')
    __row1_input = (By.XPATH, '//div[@id="row1"]/input')
    __row2_btn = (By.XPATH, '//div[@id="row2"]/button')
    __row1_save_btn = (By.XPATH, '//button[@id="save_btn"]')
    __row_confirmation = (By.ID, "confirmation")
    __edit_btn = (By.ID, "edit_btn")
    __instructions = (By.XPATH, '//p[@id="instructions"]')

    def click_add_btn(self) -> None:
        self._click(self.__add_btn)
        self._wait_until_visible(self.__row2_input)

    def is_row2_displayed(self) -> bool:
        return self._is_displayed(self.__row2_input)

    def add_second_dish(self, food: str) -> None:
        self._type(self.__row2_input, food)
        self._click(self.__row2_btn)
        self._wait_until_visible(self.__row_confirmation)

    def get_confirmation_msg(self) -> str:
        return self._get_text(self.__row_confirmation, timeout=3)

    def modify_row1(self, food: str):
        self._click(self.__edit_btn)
        self._wait_until_clickable(self.__row1_input)
        self._clear(self.__row1_input)
        self._type(self.__row1_input, food)
        self._click(self.__row1_save_btn)
        self._wait_until_visible(self.__row_confirmation)

    def check_invisibility(self) -> bool:
        return self._wait_invisibility(self.__instructions)
