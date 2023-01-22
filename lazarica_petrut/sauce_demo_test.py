import unittest


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class SauceDemoTestCase(unittest.TestCase):

    # Setup for Unittest TestCase
    @classmethod
    def setUp(self):
        Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.saucedemo.com/")

# Functions ----------------------------------------------------------------------------

    # Finds the login form elements, inserts the credentials and clicks the button
    def log_in(self):
        inserting_username = self.driver.find_element(By.ID, "user-name")
        inserting_username.send_keys("standard_user")
        inserting_password = self.driver.find_element(By.ID, "password")
        inserting_password.send_keys("secret_sauce")
        press_login_button = self.driver.find_element(By.ID, "login-button")
        press_login_button.click()

    # Adds some items to the Cart
    def add_items_to_cart(self):
        add_item_to_cart_t_shirt = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        add_item_to_cart_t_shirt.click()
        add_item_to_cart_bike_light = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_item_to_cart_bike_light.click()

    # Finds and clicks the Shopping Cart Button
    def click_shopping_cart_button(self):
        click_cart_button = self.driver.find_element(By.ID, "shopping_cart_container")
        click_cart_button.click()

    # Finds and clicks the Checkout Button
    def click_checkout_button(self):
        click_checkout_button = self.driver.find_element(By.ID, "checkout")
        click_checkout_button.click()

    # Finds the elements and adds the info required for checkout
    def insert_checkout_details_and_click_continue(self):
        enter_first_name = self.driver.find_element(By.ID, "first-name")
        enter_first_name.send_keys("James")
        enter_last_name = self.driver.find_element(By.ID, "last-name")
        enter_last_name.send_keys("Bond")
        enter_zipcode = self.driver.find_element(By.ID, "postal-code")
        enter_zipcode.send_keys("007")
        click_continue_button = self.driver.find_element(By.ID, "continue")
        click_continue_button.click()

# Tests --------------------------------------------------------------------------------

    # Tests the login function of the site
    def test_sauce_demo_login(self):
        self.log_in()
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"

    # Tests the add to cart function of the site
    def test_add_to_cart(self):
        self.log_in()
        click_add_to_cart_backpack = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        click_add_to_cart_backpack.click()
        assert self.driver.find_element(By.ID, "remove-sauce-labs-backpack")

    # Tests the remove from cart function of the site
    def test_remove_from_cart(self):
        self.log_in()
        self.add_items_to_cart()
        self.click_shopping_cart_button()
        assert self.driver.current_url == "https://www.saucedemo.com/cart.html"

    # Tests the first step checkout function of the site
    def test_checkout(self):
        self.log_in()
        self.add_items_to_cart()
        self.click_shopping_cart_button()
        self.click_checkout_button()
        assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"

    # Tests the second step checkout function of the site
    def test_enter_checkout_information(self):
        self.log_in()
        self.add_items_to_cart()
        self.click_shopping_cart_button()
        self.click_checkout_button()
        self.insert_checkout_details_and_click_continue()
        assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"

    # Tests the last step checkout function of the site
    def test_complete_checkout(self):
        self.log_in()
        self.add_items_to_cart()
        self.click_shopping_cart_button()
        self.click_checkout_button()
        self.insert_checkout_details_and_click_continue()
        click_finish_checkout_button = self.driver.find_element(By.ID, "finish")
        click_finish_checkout_button.click()
        assert  self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html"

    # Teardown function for Unittest TestCase
    @classmethod
    def tearDown(self):
        self.driver.quit()