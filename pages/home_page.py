import allure
from pages.base_page import BasePage
from src.data import *
from src.locators import Locators


class HomePage(BasePage):

    @allure.step('Открываем и закрываем браузер "only.digital"')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем сайт "Login"')
    def home_open(self):
        self.open(URL_HOMEPAGE)

    @allure.step('ждём загрузки страницы')
    def wait_site(self):
        self.wait_for_element(Locators.TAG_HEADER)

    @allure.step('ждём загрузки окна куки')
    def click_cookie_button(self):
        self.click(Locators.COOKIE_BUTTON)

    @allure.step('скролл сайта до футера сайт')
    def scroll_till_footer(self):
        self.scroll_down(Locators.TAG_FOOTER)

    @allure.step('Ищем кнопку "Начать проект"')
    def visible_button(self):
        self.wait_for_element(Locators.BUTTON_PROJECT)

    @allure.step('Получаем текст')
    def text_search(self):
        self.get_text(Locators.BUTTON_BEHANCE)

    @allure.step('Видимость кнопки "Беханс"')
    def vis_of_element(self):
        return self.is_element_visible(Locators.BUTTON_BEHANCE)
