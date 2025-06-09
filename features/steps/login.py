from saucedemo.login_page import LoginPage
from saucedemo.home_page import Home_Page
from behave import given, when, then

@given('user goes to saucedemo website')
def step_navigating_to_saucedemo(context):
    context.page.wait_for_timeout(1000)  # Wait for 10 seconds

@given('user fill valid login details with username {username} and password {password}')
def step_fill_details(context, username: str, password: str):
    login_page = LoginPage(context.page)
    login_page.fill_login_form(username, password)

@then('user should be on homepage')
def step_validate_home_page(context):
    homepage = Home_Page(context.page)
    homepage.validate_home_page()
    