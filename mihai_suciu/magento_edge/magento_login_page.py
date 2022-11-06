import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class MagentoLoginTestCase(unittest.TestCase):

    def setUp(self) -> None:
        service = EdgeService(EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=service)
        self.driver.implicitly_wait(10)
        self.driver.get("https://magento.softwaretestingboard.com/"
                        "customer/account/login/referer/"
                        "aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/")

    def tearDown(self) -> None:
        self.driver.quit()

    def customer_login(self, user, password):
        email_field = self.driver.find_element(By.ID, "email")
        email_field.send_keys(user)
        password_field = self.driver.find_element(By.ID, "pass")
        password_field.send_keys(password)
        sign_in_button = self.driver.find_element(By.ID, "send2")
        sign_in_button.click()

    def test_bad_credentials_login(self):
        self.customer_login('Tester1@QAMagic.com', 'MagicPass!')
        error_msg_banner = self.driver.find_element(By.XPATH, '/ html / body / div[2] /'
                                                              ' header / div[1] / div / '
                                                              'ul / li[2] / a')
        assert error_msg_banner.is_displayed(), "Error message banner was not displayed"

    def test_no_credentials_login(self):
        self.customer_login('', '')
        error_msg_banner = self.driver.find_element(By.XPATH, '/ html / body / div[2] /'
                                                              ' header / div[1] / div / '
                                                              'ul / li[2] / a')
        assert error_msg_banner.is_displayed(), "Error message banner was not displayed"

    def test_good_credentials_login(self):
        self.customer_login('roni_cost@example.com', 'roni_cost3@example.com')
        assert self.driver.current_url == "https://magento.softwaretestingboard.com/" \
                                          "customer/account/login/referer/" \
                                          "aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/", \
            "URL error"

    def test_captcha_image(self):
        captcha_image = self.driver.find_element(By.TAG_NAME, 'img')
        assert captcha_image.is_displayed(), "Captcha image not displayed"
