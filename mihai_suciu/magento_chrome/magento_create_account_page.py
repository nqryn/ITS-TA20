import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class MagentoCreateAccountTestCase(unittest.TestCase):

    def setUp(self) -> None:
        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)
        self.driver.get("https://magento.softwaretestingboard.com/customer/account/create/")

    def tearDown(self) -> None:
        self.driver.quit()

    def complete_fields(self, firstname, lastname, email, password1, password2):
        first_name_field = self.driver.find_element(By.ID, 'firstname')
        first_name_field.send_keys(firstname)
        last_name_field = self.driver.find_element(By.ID, 'lastname')
        last_name_field.send_keys(lastname)
        newsletter_button = self.driver.find_element(By.ID, 'is_subscribed')
        newsletter_button.click()
        email_field = self.driver.find_element(By.ID, 'email_address')
        email_field.send_keys(email)
        password_field = self.driver.find_element(By.ID, 'password')
        password_field.send_keys(password1)
        password_confirmation_field = self.driver.find_element(By.ID, 'password-confirmation')
        password_confirmation_field.send_keys(password2)

    def create_account_button_click(self):
        create_an_account_button = self.driver.find_elements(By.XPATH, '//*[text()="Create an Account"]')
        create_an_account_button[2].click()

    def test_page_title(self):
        page_title = self.driver.find_element(By.TAG_NAME, 'h1')
        assert page_title.text == "Create New Customer Account", "Error: Page title error"

    # !!! you need a new email each time else --> TEST FAILS!!!
    def test_create_account_good_credentials(self):
        self.complete_fields('Tester', 'Automation', 'qa22_tester@ibm.com',
                             'Q4T3ster!', 'Q4T3ster!')
        self.create_account_button_click()
        assert self.driver.current_url == "https://magento.softwaretestingboard.com/customer/account/", \
            "Error: !!!you need a new email each time, else --> TEST FAILS!!!"

    def test_password_strenght_banner_display(self):
        password_strenght_banner = self.driver.find_element(By.ID, 'password-strength-meter-label')
        assert password_strenght_banner.is_displayed(), "Password strenght banner is not displayed"

    def test_create_account_wrong_password(self):
        self.complete_fields('Tester2', 'Automation2', 'qa3_tester@ibm.com', 'Q4T3ster!', 'Autom4T!on')
        self.create_account_button_click()
        confirm_password_banner = self.driver.find_element(By.ID, 'password-confirmation-error')
        assert confirm_password_banner.text == "Please enter the same value again."

    def test_first_name_no_credentials(self):
        self.create_account_button_click()
        first_name_error_field = self.driver.find_element(By.XPATH, '//*[@id="firstname"]')
        assert first_name_error_field.text == 'This is a required field.', \
            "Error: Page has different behaviours manual/automated"

    def test_last_name_no_credentials(self):
        self.create_account_button_click()
        last_name_error_field = self.driver.find_element(By.XPATH, '//*[@id="lastname"]')
        assert last_name_error_field.text == 'This is a required field.', \
            "Error: Page has different behaviours manual/automated"

    def test_email_no_credentials(self):
        self.create_account_button_click()
        email_error_field = self.driver.find_element(By.XPATH, '//*[@id="email_address"]')
        assert email_error_field.text == 'This is a required field.', \
            "Error: Page has different behaviours manual/automated"

    def test_confirm_password_no_credentials(self):
        self.create_account_button_click()
        confirm_password_field = self.driver.find_element(By.XPATH, '//*[@id="password-confirmation-error"]')
        assert confirm_password_field.text == 'This is a required field.', \
            "Error: Page has different behaviours manual/automated"

    def test_luma_button(self):
        luma_button = self.driver.find_element(By.TAG_NAME, 'img')
        luma_button.click()
        assert self.driver.current_url == 'https://magento.softwaretestingboard.com/', "URL Error"

