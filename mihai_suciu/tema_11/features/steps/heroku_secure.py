from behave import *


@When('I click the Logout button')
def step_impl(context):
    context.browser.click_logout_button()

