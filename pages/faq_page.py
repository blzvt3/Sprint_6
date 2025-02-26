from locators.faq_page_locators import FAQPageLocators
from pages.base_page import BasePage

class FAQPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = FAQPageLocators

    def click_on_cookie_button(self):
        self.click_on_element(self.locators.COOKIE_BUTTON)

    def click_on_faq_button_1(self):
        self.click_on_element(self.locators.FAQ_BUTTON_1)

    def wait_visibility_of_faq_text_1(self):
        self.wait_visibility_of_element(self.locators.FAQ_TEXT_1)

    def get_text_of_faq_1(self):
        return self.get_text_of_element(self.locators.FAQ_TEXT_1)

    def click_on_faq_button_2(self):
        self.click_on_element(self.locators.FAQ_BUTTON_2)

    def wait_visibility_of_faq_text_2(self):
        self.wait_visibility_of_element(self.locators.FAQ_TEXT_2)

    def get_text_of_faq_2(self):
        return self.get_text_of_element(self.locators.FAQ_TEXT_2)

    def click_on_faq_button_3(self):
        self.click_on_element(self.locators.FAQ_BUTTON_3)

    def wait_visibility_of_faq_text_3(self):
        self.wait_visibility_of_element(self.locators.FAQ_TEXT_3)

    def get_text_of_faq_3(self):
        return self.get_text_of_element(self.locators.FAQ_TEXT_3)

    def click_on_faq_button_4(self):
        self.click_on_element(self.locators.FAQ_BUTTON_4)

    def wait_visibility_of_faq_text_4(self):
        self.wait_visibility_of_element(self.locators.FAQ_TEXT_4)

    def get_text_of_faq_4(self):
        return self.get_text_of_element(self.locators.FAQ_TEXT_4)

    def click_on_faq_button_5(self):
        self.click_on_element(self.locators.FAQ_BUTTON_5)

    def wait_visibility_of_faq_text_5(self):
        self.wait_visibility_of_element(self.locators.FAQ_TEXT_5)

    def get_text_of_faq_5(self):
        return self.get_text_of_element(self.locators.FAQ_TEXT_5)

    def click_on_faq_button_6(self):
        self.click_on_element(self.locators.FAQ_BUTTON_6)

    def wait_visibility_of_faq_text_6(self):
        self.wait_visibility_of_element(self.locators.FAQ_TEXT_6)

    def get_text_of_faq_6(self):
        return self.get_text_of_element(self.locators.FAQ_TEXT_6)

    def click_on_faq_button_7(self):
        self.click_on_element(self.locators.FAQ_BUTTON_7)

    def wait_visibility_of_faq_text_7(self):
        self.wait_visibility_of_element(self.locators.FAQ_TEXT_7)

    def get_text_of_faq_7(self):
        return self.get_text_of_element(self.locators.FAQ_TEXT_7)

    def click_on_faq_button_8(self):
        self.click_on_element(self.locators.FAQ_BUTTON_8)

    def wait_visibility_of_faq_text_8(self):
        self.wait_visibility_of_element(self.locators.FAQ_TEXT_8)

    def get_text_of_faq_8(self):
        return self.get_text_of_element(self.locators.FAQ_TEXT_8)