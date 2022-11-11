from behave import *


@Given('I am on the Home page')
def step_impl(context):
    context.browser.go_to('')


@When('I click the Form Authentication button')
def step_impl(context):
    context.browser.click_authentication_button()


@Then('I am on the Login page')
def step_impl(context):
    assert context.browser.get_current_url() == \
           "https://the-internet.herokuapp.com/login", "URL error"


@When('I click the Inputs button')
def step_impl(context):
    context.browser.clik_inputs_button()


@Then('I am on the Inputs page')
def step_impl(context):
    assert context.browser.get_current_url() == \
           "https://the-internet.herokuapp.com/inputs", "URL error"


@When('I click the Sortable Data Tables button')
def step_impl(context):
    context.browser.clik_sortable_data_tables_button()


@Then('I am on the Sortable Data Tables page')
def step_impl(context):
    assert context.browser.get_current_url() == \
           "https://the-internet.herokuapp.com/tables", "URL error"