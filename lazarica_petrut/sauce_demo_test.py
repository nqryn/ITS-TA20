import unittest


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class SauceDemoTestCase(unittest.TestCase):

    @classmethod
    def setUp(self):
        Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.saucedemo.com/")

    def test_sauce_demo_login(self):
        inserting_username = self.driver.find_element(By.ID, "user-name")
        inserting_username.send_keys("standard_user")
        inserting_password = self.driver.find_element(By.ID, "password")
        inserting_password.send_keys("secret_sauce")
        press_login_button = self.driver.find_element(By.ID, "login-button")
        press_login_button.click()
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"

    def test_add_to_cart(self):
        inserting_username = self.driver.find_element(By.ID, "user-name")
        inserting_username.send_keys("standard_user")
        inserting_password = self.driver.find_element(By.ID, "password")
        inserting_password.send_keys("secret_sauce")
        press_login_button = self.driver.find_element(By.ID, "login-button")
        press_login_button.click()
        click_add_to_cart_backpack = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        click_add_to_cart_backpack.click()
        assert self.driver.find_element(By.ID, "remove-sauce-labs-backpack")

    def test_remove_from_cart(self):
        inserting_username = self.driver.find_element(By.ID, "user-name")
        inserting_username.send_keys("standard_user")
        inserting_password = self.driver.find_element(By.ID, "password")
        inserting_password.send_keys("secret_sauce")
        press_login_button = self.driver.find_element(By.ID, "login-button")
        press_login_button.click()
        add_item_to_cart_t_shirt = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        add_item_to_cart_t_shirt.click()
        add_item_to_cart_bike_light = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_item_to_cart_bike_light.click()
        click_cart_button = self.driver.find_element(By.ID, "shopping_cart_container")
        click_cart_button.click()
        assert self.driver.current_url == "https://www.saucedemo.com/cart.html"

    def test_checkout(self):
        inserting_username = self.driver.find_element(By.ID, "user-name")
        inserting_username.send_keys("standard_user")
        inserting_password = self.driver.find_element(By.ID, "password")
        inserting_password.send_keys("secret_sauce")
        press_login_button = self.driver.find_element(By.ID, "login-button")
        press_login_button.click()
        add_item_to_cart_t_shirt = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        add_item_to_cart_t_shirt.click()
        add_item_to_cart_bike_light = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_item_to_cart_bike_light.click()
        click_cart_button = self.driver.find_element(By.ID, "shopping_cart_container")
        click_cart_button.click()
        click_checkout_button = self.driver.find_element(By.ID, "checkout")
        click_checkout_button.click()
        assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"

    def test_enter_checkout_information(self):
        inserting_username = self.driver.find_element(By.ID, "user-name")
        inserting_username.send_keys("standard_user")
        inserting_password = self.driver.find_element(By.ID, "password")
        inserting_password.send_keys("secret_sauce")
        press_login_button = self.driver.find_element(By.ID, "login-button")
        press_login_button.click()
        add_item_to_cart_t_shirt = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        add_item_to_cart_t_shirt.click()
        add_item_to_cart_bike_light = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_item_to_cart_bike_light.click()
        click_cart_button = self.driver.find_element(By.ID, "shopping_cart_container")
        click_cart_button.click()
        click_checkout_button = self.driver.find_element(By.ID, "checkout")
        click_checkout_button.click()
        # ---------------------------
        enter_first_name = self.driver.find_element(By.ID, "first-name")
        enter_first_name.send_keys("James")
        enter_last_name = self.driver.find_element(By.ID, "last-name")
        enter_last_name.send_keys("Bond")
        enter_zipcode = self.driver.find_element(By.ID, "postal-code")
        enter_zipcode.send_keys("007")
        click_continue_button = self.driver.find_element(By.ID, "continue")
        click_continue_button.click()
        assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"

    def test_complete_checkout(self):
        inserting_username = self.driver.find_element(By.ID, "user-name")
        inserting_username.send_keys("standard_user")
        inserting_password = self.driver.find_element(By.ID, "password")
        inserting_password.send_keys("secret_sauce")
        press_login_button = self.driver.find_element(By.ID, "login-button")
        press_login_button.click()
        add_item_to_cart_t_shirt = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        add_item_to_cart_t_shirt.click()
        add_item_to_cart_bike_light = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_item_to_cart_bike_light.click()
        click_cart_button = self.driver.find_element(By.ID, "shopping_cart_container")
        click_cart_button.click()
        click_checkout_button = self.driver.find_element(By.ID, "checkout")
        click_checkout_button.click()
        # ---------------------------
        enter_first_name = self.driver.find_element(By.ID, "first-name")
        enter_first_name.send_keys("James")
        enter_last_name = self.driver.find_element(By.ID, "last-name")
        enter_last_name.send_keys("Bond")
        enter_zipcode = self.driver.find_element(By.ID, "postal-code")
        enter_zipcode.send_keys("007")
        click_continue_button = self.driver.find_element(By.ID, "continue")
        click_continue_button.click()
        # -----------------------------
        click_finish_checkout_button = self.driver.find_element(By.ID, "finish")
        click_finish_checkout_button.click()
        assert self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html"

    @classmethod
    def tearDown(self):
        self.driver.quit()

# if __name__ == '__main__':
#    unittest.main()