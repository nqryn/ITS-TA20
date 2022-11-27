from behave import *


@When('I click the Checkout button')
def step_impl(context):
    context.cart_page.click_checkout_btt()


@Then('I am on the Checkout Step One Page')
def step_impl(context):
    assert context.cart_page.is_checkout_page_1(), 'Page URL error'


@When('I input the first name')
def step_impl(context):
    context.cart_page.input_first_name()


@When('I input the last name')
def step_impl(context):
    context.cart_page.input_last_name()


@When('I input the Zip Code')
def step_impl(context):
    context.cart_page.input_zip_code()


@When('I click the Continue button')
def step_impl(context):
    context.cart_page.click_continue_btt()


@Then('I am on the Checkout Step Two Page')
def step_impl(context):
    assert context.cart_page.is_checkout_page_2(), 'Page URL error'


@When('I click Finish button')
def step_impl(context):
    context.cart_page.click_finish_btt()


@Then('I am on the Checkout Complete Page')
def step_impl(context):
    assert context.cart_page.is_checkout_complete_page(), 'Page URL error'

