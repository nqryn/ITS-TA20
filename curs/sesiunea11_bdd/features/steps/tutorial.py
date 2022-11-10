from behave import *


@given("we have behave installed")
def step_impl(context):
    pass


@when("we implement a test")
def step_impl(context):
    assert 1+1 == 3


@then("behave will test it for us!")
def step_impl(context):
    assert context.failed is False
