import time
from behave import *


@Given('I am on the Sign In page')
def step_impl(context):
    context.browser.go_to('sign-in')


@When('I input a valid email for expired membership')
def step_impl(context):
    valid_email = "adella.neacsu@gmail.com"
    context.browser.input_email(valid_email)


@When('I input a valid password')
def step_impl(context):
    valid_password = "8-72Characters"
    context.browser.input_password(valid_password)


@When('I click the Log In button')
def step_impl(context):
    context.browser.click_login_button()


@Then('I receive the "{err_msg}" error message')
def step_impl(context, err_msg):
    assert context.browser.is_error_message_displayed(err_msg)


@Then('I am still on the Sign In page')
def step_impl(context):
    assert context.browser.get_current_url() == 'https://jules.app/sign-in'


@When("I input a fake email")
def step_impl(context):
    fake_email = "fake.email@ceva.com"
    context.browser.input_email(fake_email)


@When("I input a fake password")
def step_impl(context):
    fake_password = "FakePassword"
    context.browser.input_password(fake_password)

