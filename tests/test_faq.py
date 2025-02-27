import allure
from pages.faq_page import FAQPage

class TestFAQ:
    @allure.title('Проверка раздела «Вопросы о важном» - вопрос №1')
    def test_faq_1(self, driver):
        faq_page = FAQPage(driver)
        faq_page.click_on_cookie_button()
        faq_page.click_on_faq_button_1()
        faq_page.wait_visibility_of_faq_text_1()
        assert faq_page.get_text_of_faq_1() == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    @allure.title('Проверка раздела «Вопросы о важном» - вопрос №2')
    def test_faq_2(self, driver):
        faq_page = FAQPage(driver)
        faq_page.click_on_cookie_button()
        faq_page.click_on_faq_button_2()
        faq_page.wait_visibility_of_faq_text_2()
        assert faq_page.get_text_of_faq_2() == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    @allure.title('Проверка раздела «Вопросы о важном» - вопрос №3')
    def test_faq_3(self, driver):
        faq_page = FAQPage(driver)
        faq_page.click_on_cookie_button()
        faq_page.click_on_faq_button_3()
        faq_page.wait_visibility_of_faq_text_3()
        assert faq_page.get_text_of_faq_3() == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    @allure.title('Проверка раздела «Вопросы о важном» - вопрос №4')
    def test_faq_4(self, driver):
        faq_page = FAQPage(driver)
        faq_page.click_on_cookie_button()
        faq_page.click_on_faq_button_4()
        faq_page.wait_visibility_of_faq_text_4()
        assert faq_page.get_text_of_faq_4() == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    @allure.title('Проверка раздела «Вопросы о важном» - вопрос №5')
    def test_faq_5(self, driver):
        faq_page = FAQPage(driver)
        faq_page.click_on_cookie_button()
        faq_page.click_on_faq_button_5()
        faq_page.wait_visibility_of_faq_text_5()
        assert faq_page.get_text_of_faq_5() == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    @allure.title('Проверка раздела «Вопросы о важном» - вопрос №6')
    def test_faq_6(self, driver):
        faq_page = FAQPage(driver)
        faq_page.click_on_cookie_button()
        faq_page.click_on_faq_button_6()
        faq_page.wait_visibility_of_faq_text_6()
        assert faq_page.get_text_of_faq_6() == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    @allure.title('Проверка раздела «Вопросы о важном» - вопрос №7')
    def test_faq_7(self, driver):
        faq_page = FAQPage(driver)
        faq_page.click_on_cookie_button()
        faq_page.click_on_faq_button_7()
        faq_page.wait_visibility_of_faq_text_7()
        assert faq_page.get_text_of_faq_7() == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    @allure.title('Проверка раздела «Вопросы о важном» - вопрос №8')
    def test_faq_8(self, driver):
        faq_page = FAQPage(driver)
        faq_page.click_on_cookie_button()
        faq_page.click_on_faq_button_8()
        faq_page.wait_visibility_of_faq_text_8()
        assert faq_page.get_text_of_faq_8() == "Да, обязательно. Всем самокатов! И Москве, и Московской области."