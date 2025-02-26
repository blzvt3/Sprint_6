from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators

    def click_on_cookie_button(self):
        self.click_on_element(self.locators.COOKIE_BUTTON)

    def click_on_scooter_button(self):
        self.click_on_element(self.locators.SCOOTER_BUTTON)

    def click_on_yandex_button(self):
        self.click_on_element(self.locators.YANDEX_BUTTON)

    def wait_visibility_of_find_button(self):
        self.wait_visibility_of_element(self.locators.FIND_BUTTON)

    def click_on_order_button_top(self):
        self.click_on_element(self.locators.ORDER_BUTTON_TOP)

    def click_on_order_button_down(self):
        self.click_on_element(self.locators.ORDER_BUTTON_DOWN)

    def wait_visibility_of_order_button_down(self):
        self.wait_visibility_of_element(self.locators.ORDER_BUTTON_DOWN)

    def wait_visibility_of_next_button(self):
        self.wait_visibility_of_element(self.locators.NEXT_BUTTON)

    def fill_order_form(self, name, surname, address, phone, metro):
        self.fill_input(self.locators.NAME_INPUT, name)
        self.fill_input(self.locators.SURNAME_INPUT, surname)
        self.fill_input(self.locators.ADDRESS_INPUT, address)
        self.fill_input(self.locators.PHONE_INPUT, phone)
        self.fill_input(self.locators.METRO_INPUT, metro)

    def click_on_metro_button(self):
        self.click_on_element(self.locators.METRO_BUTTON)

    def click_on_next_button(self):
        self.click_on_element(self.locators.NEXT_BUTTON)

    def wait_visibility_of_date_input(self):
        self.wait_visibility_of_element(self.locators.DATE_INPUT)

    def fill_current_date(self, date):
        self.fill_date(self.locators.DATE_INPUT, date)

    def click_on_rental_period_button(self):
        self.click_on_element(self.locators.RENTAL_PERIOD_BUTTON)

    def click_on_one_day_button(self):
        self.click_on_element(self.locators.ONE_DAY_BUTTON)

    def click_on_black_color_button(self):
        self.click_on_element(self.locators.BLACK_COLOR_BUTTON)

    def fill_comment(self, text):
        self.fill_input(self.locators.DATE_INPUT, text)

    def click_on_order_button(self):
        self.click_on_element(self.locators.ORDER_BUTTON)

    def click_on_yes_button(self):
        self.click_on_element(self.locators.YES_BUTTON)

    def wait_visibility_of_order_placed_text(self):
        return self.wait_visibility_of_element(self.locators.ORDER_PLACED_TEXT)