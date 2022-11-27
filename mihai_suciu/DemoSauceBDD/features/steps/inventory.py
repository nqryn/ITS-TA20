from behave import *


@Given('I am a logged in user')
def step_impl(context):
    context.login_page.go_to_page()
    context.login_page.login("standard_user", "secret_sauce")


@Given('I am on the Inventory Page')
def step_impl(context):
    pass


@When('I click product_1 button')
def step_impl(context):
    context.inventory_page.click_product_button()


@Then('I am on the product_1 page')
def step_impl(context):
    assert context.inventory_page.am_i_on_product_page(), \
        "Page URL error"


@When('I click the Add to Cart button')
def step_impl(context):
    context.inventory_page.click_add_to_cart()


@Then('The product Add to Cart button changes to Remove')
def step_impl(context):
    assert context.inventory_page.is_remove_button_displayed(), \
        "Error: Remove button not displayed"


@Then('The Cart badge is increased')
def step_impl(context):
    assert context.inventory_page.is_cart_badge_increased(), \
        "Error: cart badge counter"


@When('I click product_1 Add to Cart button')
def step_impl(context):
    context.inventory_page.add_product_to_cart()


@Then('The Remove button is displayed')
def step_impl(context):
    assert context.inventory_page.is_remove_btt_o1_displayed(), \
        "Error: Remove button not displayed"


@When('I click product_1 Remove button')
def step_impl(context):
    context.inventory_page.click_remove_button()


@Then('The product button changes to Add to Cart')
def step_impl(context):
    assert context.inventory_page.is_add_to_cart_btt_o1_displayed(), \
        "Error: Add to Cart button is not displayed"


@When('I add to cart all the products under 20')
def step_impl(context):
    context.inventory_page.add_products_under_20()


@Then('The Cart badge counter is 4')
def step_impl(context):
    assert context.inventory_page.is_cart_badge_4(), \
        "Error: cart badge counter"


@When('I click the Cart button')
def step_impl(context):
    context.inventory_page.click_cart_button()


@Then('I am on the Cart Page')
def step_impl(context):
    assert context.inventory_page.am_i_on_the_cart_page(), \
        'Page URL error'
