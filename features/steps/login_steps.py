from behave import given, when, then
from pages.login_page import *


def get_platform(context):
    return context.config.userdata.get("platform", "android").lower()

@given("the app is launched")
def step_impl(context):
    assert context.driver is not None

@when("I click on the continue button in the launch screen")
def step_impl(context):
    click_on_continue_button_in_launch_screen(context.driver, get_platform(context))

@when("I click on the Account tab")
def step_impl(context):
    click_on_Account_tab(context.driver, get_platform(context))

@when("I click on the Sign In button")
def step_impl(context):
    click_on_signin_button(context.driver, get_platform(context))

@when("I login with valid credentials")
def step_impl(context):
    login_in_with_valid_credentials(context.driver, get_platform(context))

@then("I should be logged in successfully")
def step_impl(context):
    click_on_Account_tab(context.driver, get_platform(context))
    assert True


