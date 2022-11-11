from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Browser:

    BASE_URL = 'https://the-internet.herokuapp.com/'
    USERNAME_SELECTOR = (By.XPATH, '//input[@id="username"]')
    PASSWORD_SELECTOR = (By.XPATH, '//input[@id="password"]')
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

    def input_username(self, username):
        username_input = self.driver.find_element(*self.USERNAME_SELECTOR)
        username_input.send_keys(username)

    def input_password(self, password):
        password_input = self.driver.find_element(*self.PASSWORD_SELECTOR)
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(*self.LOGIN_SELECTOR)
        login_button.click()

    def is_error_message_valid(self, error_message):
        selector = f'//div[@id="flash"]'
        error_message_element = self.driver.find_element(By.XPATH, selector)
        verification = error_message in error_message_element.text
        return verification

    def get_current_url(self):
        return self.driver.current_url

    def click_authentication_button(self):
        selector = f'//*[text()="Form Authentication"]'
        self.driver.find_element(By.XPATH, selector).click()

    def clik_inputs_button(self):
        selector = f'//*[text()="Inputs"]'
        self.driver.find_element(By.XPATH, selector).click()

    def clik_sortable_data_tables_button(self):
        selector = f'//*[text()="Sortable Data Tables"]'
        self.driver.find_element(By.XPATH, selector).click()

    def click_logout_button(self):
        selector = f'//*[text()=" Logout"]'
        self.driver.find_element(By.XPATH, selector).click()

