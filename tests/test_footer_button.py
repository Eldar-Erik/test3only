import pytest
import allure
from pages.home_page import HomePage
from src.locators import Locators


class TestFooterButton:

    @allure.title('Поиск кнопки "Начать проект"')
    @pytest.mark.parametrize('footer_locator', [
        (Locators.BUTTON_PROJECT),
        (Locators.BUTTON_BEHANCE),
        (Locators.TAG_PAGE_YEAR),
        (Locators.TAG_FOOTER_CREATIVE)
        ])
    def test_find_footer_button(self, driver, footer_locator):
        home = HomePage(driver)
        home.home_open()
        home.wait_site()
        home.click_cookie_button()
        home.scroll_to_bottom()
        assert home.vis_of_element(footer_locator)
