# pylint: disable=no-name-in-module
# pylint: disable=function-redefined
# pylint: disable=import-error

import requests
from configuration import GIT_USER, GIT_OAUTH, GIT_URL
from behave import given, when, then

@given('The Correct Git Credentials')
def step_impl(context):
    login_token = (GIT_USER(), GIT_OAUTH())
    context.session = requests.session()
    context.session.auth = login_token

@given(u'The Incorrect Git Credentials')
def step_impl(context):
    login_token = (GIT_USER(), "Bad Oauth Token")
    context.session = requests.session()
    context.session.auth = login_token


@when('Log in')
def step_impl(context):
    context.res = context.session.get(GIT_URL())

@then('Status Code Should Be {status_code:d}')
def step_impl(context, status_code):
    assert context.res.status_code == status_code