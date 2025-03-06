import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    @allure.step('Открываем и закрываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод открытия страницы')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Метод ждет загрузки элемента и прожимает его')
    def click(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator)).click()

    @allure.step('Метод ждет и возвращает загрузку элемента')
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Метод возвращает видимость элемента')
    def is_element_visible(self, locator):
        return self.wait_for_element(locator).is_displayed()

    @allure.step('Скроллим вниз')
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
