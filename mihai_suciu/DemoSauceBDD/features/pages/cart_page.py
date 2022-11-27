from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class CartPage(BasePage):
    URL = 'https://www.saucedemo.com/cart.html'
    CART_BADGE_SELECTOR = (By.XPATH, '//span[@class="shopping_cart_badge"]')
    CHECKOUT_BUTTON_SELECTOR = (By.ID, 'checkout')
    FIRST_NAME_SELECTOR = (By.ID, 'first-name')
    LAST_NAME_SELECTOR = (By.ID, 'last-name')
    ZIP_SELECTOR = (By.ID, 'postal-code')
    CONTINUE_BTT_SELECTOR = (By.ID, 'continue')
    FINISH_BTT_SELECTOR = (By.ID, 'finish')

    def click_checkout_btt(self):
        checkout_btt = self.driver.find_element(*self.CHECKOUT_BUTTON_SELECTOR)
        checkout_btt.click()

    def is_checkout_page_1(self):
        current_url = self.driver.current_url
        expected_url = 'https://www.saucedemo.com/checkout-step-one.html'
        return current_url == expected_url

    def input_first_name(self):
        first_name_field = self.driver.find_element(*self.FIRST_NAME_SELECTOR)
        first_name_field.send_keys('Tom')

    def input_last_name(self):
        last_name_field = self.driver.find_element(*self.LAST_NAME_SELECTOR)
        last_name_field.send_keys('Cat')

    def input_zip_code(self):
        zip_code_field = self.driver.find_element(*self.ZIP_SELECTOR)
        zip_code_field.send_keys('486144')

    def click_continue_btt(self):
        continue_btt = self.driver.find_element(*self.CONTINUE_BTT_SELECTOR)
        continue_btt.click()

    def is_checkout_page_2(self):
        current_url = self.driver.current_url
        expected_url = 'https://www.saucedemo.com/checkout-step-two.html'
        return current_url == expected_url

    def click_finish_btt(self):
        finish_btt = self.driver.find_element(*self.FINISH_BTT_SELECTOR)
        finish_btt.click()

    def is_checkout_complete_page(self):
        current_url = self.driver.current_url
        expected_url = 'https://www.saucedemo.com/checkout-complete.html'
        return current_url == expected_url
