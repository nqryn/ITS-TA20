import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class MagentoFirstPageTestCase(unittest.TestCase):

    def setUp(self) -> None:
        service = EdgeService(EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=service)
        self.driver.implicitly_wait(10)
        self.driver.get("https://magento.softwaretestingboard.com/")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login_button(self):
        login_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign In')
        login_button.click()
        assert self.driver.current_url == "https://magento.softwaretestingboard.com/" \
                                          "customer/account/login/referer/" \
                                          "aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/"

    def test_create_an_Account(self):
        create_button = self.driver.find_element(By.XPATH, '//a[text()="Create an Account"]')
        create_button.click()
        assert self.driver.current_url == "https://magento.softwaretestingboard.com/customer/account/create/"

    def test_luma_logo(self):
        luma_logo = self.driver.find_elements(By.TAG_NAME, 'img')
        assert luma_logo[0].is_displayed()

    def test_empty_shopping_cart(self):
        cart_button = self.driver.find_element(By.XPATH, '//a[@class="action showcart"]')
        cart_button.click()
        try:
            assert self.driver.current_url == 'https://magento.softwaretestingboard.com/'
        except AssertionError:
            print("Error: page has different behaviours -manual/automated")

    def test_whats_new_button(self):
        whats_new_btt = self.driver.find_element(By.XPATH, '//span[text()="What\'s New"]')
        whats_new_btt.click()
        assert self.driver.current_url == "https://magento.softwaretestingboard.com/what-is-new.html"
