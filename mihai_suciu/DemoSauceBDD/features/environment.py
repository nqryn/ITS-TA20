from browser import Browser
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def before_scenario(context, scenario):
    context.browser = Browser()
    context.login_page = LoginPage(context.browser)
    context.inventory_page = InventoryPage(context.browser)
    context.cart_page = CartPage(context.browser)


def after_scenario(context, scenario):
    context.browser.quit()
