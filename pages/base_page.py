from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import allure

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def click_on_element(self, locator):
        with allure.step(f"Кликнуть на элемент {locator}"):
            self.driver.find_element(*locator).click()

    def wait_visibility_of_element(self, locator):
        with allure.step(f"Подождать видимость элемента {locator}"):
            return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def get_text_of_element(self, locator):
        with allure.step(f"Получить текст элемента {locator}"):
            return self.driver.find_element(*locator).text

    def fill_input(self, locator, text):
        with allure.step(f"Заполнить поле {locator}"):
            self.driver.find_element(*locator).send_keys(text)

    def fill_date(self, locator, date):
        with allure.step("Заполнить дату"):
            self.driver.find_element(*locator).send_keys(date)
            self.driver.find_element(*locator).send_keys(Keys.RETURN)