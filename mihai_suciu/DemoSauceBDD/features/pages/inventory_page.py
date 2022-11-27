from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class InventoryPage(BasePage):

    URL = 'https://www.saucedemo.com/inventory.html'
    PRODUCT1_SELECTOR = (By.XPATH, '//*[@id="item_4_img_link"]/img')
    ADD_TO_CART_SELECTOR = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    ADD_TO_CART_O1_SELECTOR = (By.ID, 'add-to-cart-sauce-labs-backpack')
    ADD_TO_CART_O2_SELECTOR = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    ADD_TO_CART_O3_SELECTOR = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    ADD_TO_CART_O4_SELECTOR = (By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
    ADD_TO_CART_O5_SELECTOR = (By.ID, 'add-to-cart-sauce-labs-onesie')
    ADD_TO_CART_O6_SELECTOR = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
    REMOVE_SELECTOR = (By.XPATH, '//button[@id="remove-sauce-labs-backpack"]')
    REMOVE_O1_SELECTOR = (By.ID, 'remove-sauce-labs-backpack')
    CART_BADGE_SELECTOR = (By.XPATH, '//span[@class="shopping_cart_badge"]')
    CART_BUTTON_SELECTOR = (By.XPATH, '//a[@class="shopping_cart_link"]')
    PRODUCT_PRICES_LIST_SELECTOR = (By.XPATH, '//div[@class="inventory_item_price"]')
    ADD_TO_CART_SELECTORS_LIST = [ADD_TO_CART_O1_SELECTOR,
                                  ADD_TO_CART_O2_SELECTOR,
                                  ADD_TO_CART_O3_SELECTOR,
                                  ADD_TO_CART_O4_SELECTOR,
                                  ADD_TO_CART_O5_SELECTOR,
                                  ADD_TO_CART_O6_SELECTOR]

    def click_product_button(self):
        product_1_button = self.driver.find_element(*self.PRODUCT1_SELECTOR)
        product_1_button.click()

    def am_i_on_product_page(self):
        product_page_url = self.driver.current_url
        expected_url = 'https://www.saucedemo.com/inventory-item.html?id=4'
        return product_page_url == expected_url

    def click_add_to_cart(self):
        add_to_cart_button = self.driver.find_element(*self.ADD_TO_CART_SELECTOR)
        add_to_cart_button.click()

    def is_remove_button_displayed(self):
        remove_button = self.driver.find_element(*self.REMOVE_SELECTOR)
        return remove_button.is_displayed()

    def is_cart_badge_increased(self):
        cart_badge = self.driver.find_element(*self.CART_BADGE_SELECTOR)
        return cart_badge.text == '1'

    def add_product_to_cart(self):
        add_to_cart_button = self.driver.find_element(*self.ADD_TO_CART_O1_SELECTOR)
        add_to_cart_button.click()

    def click_remove_button(self):
        remove_button = self.driver.find_element(*self.REMOVE_O1_SELECTOR)
        remove_button.click()

    def is_add_to_cart_btt_o1_displayed(self):
        add_to_cart_button = self.driver.find_element(*self.ADD_TO_CART_O1_SELECTOR)
        return add_to_cart_button.is_displayed()

    def is_remove_btt_o1_displayed(self):
        remove_button = self.driver.find_element(*self.REMOVE_O1_SELECTOR)
        return remove_button.is_displayed()

    def add_products_under_20(self):
        product_prices_list = self.driver.find_elements(*self.PRODUCT_PRICES_LIST_SELECTOR)
        working_list = []
        for item in product_prices_list:
            working_list.append(float(item.text.replace('$', '')))
        counter = -1
        for item in working_list:
            counter += 1
            if item <= 20:
                product = self.driver.find_element(*self.ADD_TO_CART_SELECTORS_LIST[counter])
                product.click()

    def is_cart_badge_4(self):
        cart_badge = self.driver.find_element(*self.CART_BADGE_SELECTOR)
        return cart_badge.text == '4'

    def click_cart_button(self):
        cart_button = self.driver.find_element(*self.CART_BUTTON_SELECTOR)
        cart_button.click()

    def am_i_on_the_cart_page(self):
        cart_page_url = self.driver.current_url
        expected_url = 'https://www.saucedemo.com/cart.html'
        return cart_page_url == expected_url
