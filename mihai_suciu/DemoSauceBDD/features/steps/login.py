from behave import *


@Given('I am on the Login Page')
def step_impl(context):
    context.login_page.go_to_page()


@When('I input a fake username')
def step_impl(context):
    context.login_page.input_username('dshdhsdh')


@When('I input a fake password')
def step_impl(context):
    context.login_page.input_password('45hwh4ysh')


@When('I click the Login button')
def step_impl(context):
    context.login_page.click_login_button()


@Then('I receive the "{err_msg}" error message')
def step_impl(context, err_msg):
    assert context.login_page.is_error_message_valid(err_msg)


@When('I input a valid username')
def step_impl(context):
    context.login_page.input_username('standard_user')


@When('I input a valid password')
def step_impl(context):
    context.login_page.input_password('secret_sauce')


@Then('I am logged in')
def step_impl(context):
    assert context.login_page.am_i_logged_in(), "URL Error"
