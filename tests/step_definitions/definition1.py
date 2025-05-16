import pytest
from pytest_bdd import scenarios, given, when, then

# Load the feature file
scenarios('../bdd_features/login.feature')

@given("the API endpoint is {api}")
def apiendpoint(api):
    print(api)

@when("I make a {method} request to the API with auth header")
def callmethod(method):
    # Code to enter credentials
    print(method)

@then("the status code should be {statuscode}")
def status_code(statuscode):
    print(statuscode)
    assert True  # Replace with actual verification

