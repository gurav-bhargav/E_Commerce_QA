from behave import given, when, then 
from saucedemo.login_page import LoginPage
from saucedemo.home_page import Home_Page 
from saucedemo.cart_page import Cart_Page
from saucedemo.checkout_page import Checkout_Page

@given('user login and is on home page')
def step_for_login(context):
    loginPage = LoginPage(context.page)
    loginPage.fill_login_form()

@when('user sort products by {option}')
def step_for_sorting(context, option):
    homePage = Home_Page(context.page)
    homePage.select_sorting_option(option)
    context.selected_sorting_option = option 

@when('user add product named {name_of_product} to cart and navigate to cart')
def step_for_add_to_cart(context, name_of_product):
    print(name_of_product, ' is the name of product')
    homePage = Home_Page(context.page)
    homePage.add_product_named(name_of_product)
    homePage.navigate_to_cart()

@when('user validate product in cart and continue')
def step_for_add_to_cart(context):
    cartPage = Cart_Page(context.page)
    cartPage.validate_product_name_price()
    cartPage.checkout()

@when('user provide details and checkout')
def step_for_add_to_cart(context):
    checkout = Checkout_Page(context.page)
    checkout.fill_form()

@then('user should get order confirmation')
def step_for_add_to_cart(context):
    checkout = Checkout_Page(context.page)
    checkout.validate_order_completion()
    
@then('user validate the order')
def step_for_validating_order(context):
    homePage = Home_Page(context.page)
    homePage.validate_order_of_items(context.selected_sorting_option)


