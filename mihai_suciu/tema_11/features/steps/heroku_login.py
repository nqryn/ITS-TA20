from behave import *


@Given('I am on the Login page')
def step_impl(context):
    context.browser.go_to('login')


@When('I input a fake username')
def step_impl(context):
    username = 'popescu.ionica'
    context.browser.input_username(username)


@When('I input a valid password')
def step_impl(context):
    password = 'SuperSecretPassword!'
    context.browser.input_password(password)


@When('I click on the Login button')
def step_impl(context):
    context.browser.click_login_button()


@Then('I receive the "{err_msg}" error message')
def step_impl(context, err_msg):
    assert context.browser.is_error_message_valid(err_msg), \
        "Error message is not valid"


@Then('I am still on the Login page')
def step_impl(context):
    assert context.browser.get_current_url() ==\
           "https://the-internet.herokuapp.com/login"


@When('I input a valid username')
def step_impl(context):
    username = 'tomsmith'
    context.browser.input_username(username)


@When('I input a fake password')
def step_impl(context):
    password = 'SuperSecretPass'
    context.browser.input_password(password)


@Then('I receive the "{msg}" login message')
def step_impl(context, msg):
    assert context.browser.is_error_message_valid(msg), \
        "Secure area message is not valid"


@Then('I am on the Secure page')
def step_impl(context):
    assert context.browser.get_current_url() == \
           "https://the-internet.herokuapp.com/secure"



