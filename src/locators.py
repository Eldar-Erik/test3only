from selenium.webdriver.common.by import By


class Locators:
    COOKIE_BUTTON = (By.XPATH, ".//body/div//button[text() = 'Окей']")
    TAG_HEADER = (By.XPATH, ".//span[contains(@class, 'Header_logo')]")
    TAG_FOOTER = (By.XPATH, ".//footer//div[contains(@class, 'Footer_logo')]")
    BUTTON_PROJECT = (By.XPATH, ".//footer//button[contains(@class, 'Button_root')]")
    BUTTON_BEHANCE = (By.XPATH, ".//footer/div/div/a/span[text() = 'be']")
    TAG_PAGE_YEAR = (By.XPATH, ".//footer/div/p[text() = '© 2014 - ']")
    TAG_FOOTER_CREATIVE = (By.XPATH, ".//footer//span[contains(@class, 'word') and text() = 'creative']")
