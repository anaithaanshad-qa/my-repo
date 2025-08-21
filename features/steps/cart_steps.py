from behave import given, when, then
from pages.cart_page import *
from pages.login_page import click_on_continue_button_in_launch_screen

def get_platform(context):
    return context.config.userdata.get("platform", "android").lower()


@when("I am on the Explore tab")
def step_impl(context):
    click_on_explore_tab(context.driver, get_platform(context))

@when("I search for diapers")
def step_impl(context):
    click_on_search(context.driver, get_platform(context))

@when("I go to the first product PDP page")
def step_impl(context):
    go_to_pdp_page(context.driver, get_platform(context))

@when("I add the product to the cart")
def step_impl(context):
    add_to_cart(context.driver, get_platform(context))

@then("I should see the product in the cart")
def step_impl(context):
    assert verify_product_in_cart(context.driver, get_platform(context)) is True
