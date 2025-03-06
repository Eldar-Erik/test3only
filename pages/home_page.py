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

    @allure.step('Видимость кнопки "Беханс"')
    def vis_of_element(self, locator):
        return self.is_element_visible(locator)
