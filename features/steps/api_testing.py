from behave import given, then, when
from playwright.sync_api import expect
from utils.logger import log_message

@when('user send {longitude} and {latitude} to API')
def test_geolocation_api(context, longitude, latitude):
    apiContext = context.playwright.request.new_context(base_url='https://nominatim.openstreetmap.org')
    context.api_response = apiContext.get(f'/reverse?lat={latitude}&lon={longitude}&format=json', headers={'Content-Type': 'application/json'})


@then('user gets response with {location} in api response')
def test_api_response(context, location):
    assert context.api_response.status == 200
    context.api_data = context.api_response.json()
    assert location in context.api_data['display_name']
    log_message('info', f"The place information : {context.api_data['display_name']}")

