
#BDD: Behavior Driven Development.
#Used in Agile Accptance Testing?
#Cucumber and Gherkin basically.

#The bureocratic pretty "code" is written in .feature files, while the actual code is written in .py files.
#Note that the files must be in the EXACT folder structure in use or else Behave doesn't.
#More subfolders in steps are allowed. Actual code MUST be under steps. Multiple .feature files can be present in features folder.

"""
-root
    -features
        -steps
            -filename.py
        filename.feature
"""

#pip install behave

#Actual code:
#Once behave is typed in the terminal to run the tests, Cucumber will run the "tests" files until it encounters a Keyword/Tag (GIVEN, THEN, WHEN, etc)
#Then it will parse the steps folder's python files until it finds a function with the same TAG and STRING


# Comments below are a way to disable pylint's buggy interactions with BDDs. Yes, they are meant to be in comment form.

# pylint: disable=no-name-in-module
# pylint: disable=function-redefined
# pylint: disable=import-error

import requests
from behave import given, when, then
from sql_connector import payload_generator

@given("The generated Payload through payload_generator()")
def step_impl(context):
    context.payload = payload_generator("001")
    expected_payload = {"app": "Default", "date": "Default", "quantity": "Default", "location": "Default"}
    assert context.payload == expected_payload, "Payload Incorrect"

@when('The post request is issued')
def step_impl(context):
    context.file_res = requests.post("https://httpbin.org/anything", files=context.payload)
    assert context.file_res.status_code == 200

@then('A response with the payload is recieved')
def step_impl(context):
    assert context.payload == context.file_res.json()["files"]
