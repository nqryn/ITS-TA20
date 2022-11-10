from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Browser:

    BASE_URL = 'https://jules.app/'
    EMAIL_SELECTOR = (By.XPATH, '//input[@type="text"]')
    PASSWORD_SELECTOR = (By.XPATH, '//input[@type="password"]')
    LOGIN_SELECTOR = (By.TAG_NAME, 'button')

    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.driver = Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def go_to(self, page):
        self.driver.get(f'{self.BASE_URL}{page}')

    def input_email(self, email):
        email_input = self.driver.find_element(*self.EMAIL_SELECTOR)
        email_input.send_keys(email)

    def input_password(self, password):
        password_input = self.driver.find_element(*self.PASSWORD_SELECTOR)
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(*self.LOGIN_SELECTOR)
        login_button.click()

    def is_error_message_displayed(self, error_message):
        selector = f'//span[text()="{error_message}"]'
        error_message_element = self.driver.find_element(By.XPATH, selector)
        return error_message_element.is_displayed()

    def get_current_url(self):
        return self.driver.current_url
