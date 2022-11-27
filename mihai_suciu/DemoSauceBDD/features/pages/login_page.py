from selenium.webdriver.common.by import By


class LoginPage:

    URL = 'https://www.saucedemo.com/'
    USERNAME_SELECTOR = (By.ID, "user-name")
    PASSWORD_SELECTOR = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

    def __init__(self, browser):
        self.driver = browser.driver

    def go_to_page(self):
        self.driver.get(self.URL)

    def input_username(self, username):
        username_field = self.driver.find_element(*self.USERNAME_SELECTOR)
        username_field.send_keys(username)

    def input_password(self, password):
        password_field = self.driver.find_element(*self.PASSWORD_SELECTOR)
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()

    def is_error_message_valid(self, err_msg):
        error_message = self.driver.find_element(*self.ERROR_MESSAGE).text
        return err_msg == error_message

    def am_i_logged_in(self):
        current_url = self.driver.current_url
        return current_url == 'https://www.saucedemo.com/inventory.html'

    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()
