import unittest
import os
from mihai_suciu.config import API_KEY
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class MagentoFirstPageTestCase(unittest.TestCase):

    os.environ['GH_TOKEN'] = API_KEY

    def setUp(self) -> None:
        service = FirefoxService(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service)
        self.driver.implicitly_wait(10)
        self.driver.get("https://magento.softwaretestingboard.com/")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login_button(self):
        login_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign In')
        login_button.click()
        assert self.driver.current_url == "https://magento.softwaretestingboard.com/" \
                                          "customer/account/login/referer/" \
                                          "aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/", \
            "URL Error"

    def test_create_an_Account(self):
        create_button = self.driver.find_element(By.XPATH, '//a[text()="Create an Account"]')
        create_button.click()
        assert self.driver.current_url == "https://magento.softwaretestingboard.com/customer/account/create/", \
            "URL Error"

    def test_luma_logo(self):
        luma_logo = self.driver.find_elements(By.TAG_NAME, 'img')
        assert luma_logo[0].is_displayed(), "Logo not displayed"

    def test_empty_shopping_cart(self):
        cart_button = self.driver.find_element(By.XPATH, '//a[@class="action showcart"]')
        cart_button.click()
        assert self.driver.current_url == 'https://magento.softwaretestingboard.com/', \
            "Error: page has different behaviours -manual/automated"

    def test_whats_new_button(self):
        whats_new_btt = self.driver.find_element(By.XPATH, '//span[text()="What\'s New"]')
        whats_new_btt.click()
        assert self.driver.current_url == "https://magento.softwaretestingboard.com/what-is-new.html", \
            "URL Error"

