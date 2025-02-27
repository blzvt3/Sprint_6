import allure
import pytest
from data import Data
from pages.order_page import OrderPage

class TestOrder:
    @allure.title('Проверка переходов по сайту и редиректа на страницу Yandex')
    def test_yandex_redirect(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_cookie_button()
        order_page.click_on_order_button_top()
        order_page.wait_visibility_of_next_button()
        order_page.click_on_scooter_button()
        order_page.wait_visibility_of_order_button_down()
        order_page.click_on_order_button_down()
        order_page.wait_visibility_of_next_button()
        order_page.click_on_yandex_button()
        driver.switch_to.window(driver.window_handles[1])
        order_page.wait_visibility_of_find_button()
        assert driver.current_url == Data.DZEN_URL

    @allure.title('Проверка заказа самоката')
    @pytest.mark.parametrize(
        ("name", "surname", "address", "phone", "metro"),
        [("Саша", "Пушкин", "ул. Мира, д. 3", "11111111111", "Красные ворота"),
        ("Витя", "Цой", "ул. Спорта, д. 5", "22222222222", "Речной вокзал")])
    def test_order(self, driver, name, surname, address, phone, metro):
        order_page = OrderPage(driver)
        order_page.click_on_cookie_button()
        order_page.click_on_order_button_top()
        order_page.wait_visibility_of_next_button()
        order_page.fill_order_form(name, surname, address, phone, metro)
        order_page.click_on_metro_button()
        order_page.click_on_next_button()
        order_page.wait_visibility_of_date_input()
        order_page.fill_current_date(Data.CURRENT_DATE)
        order_page.click_on_rental_period_button()
        order_page.click_on_one_day_button()
        order_page.click_on_black_color_button()
        order_page.fill_comment(Data.COMMENT)
        order_page.click_on_order_button()
        order_page.click_on_yes_button()
        assert order_page.wait_visibility_of_order_placed_text()