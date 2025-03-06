import allure
from pages.home_page import HomePage
import time


class TestFooterButton:

    @allure.title('Поиск кнопки "Начать проект"')
    def test_find_footer_button(self, driver):
        home = HomePage(driver)
        home.home_open()
        home.wait_site()
        home.click_cookie_button()
        home.scroll_to_bottom()
        time.sleep(5)
        assert home.vis_of_element()
