
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

from behave import given, when, then


@given("The generated Payload through payload_generator()")
def step_impl(context):
    assert True

@when('The post request is issued')
def step_impl(context):
    assert True

@then('A response with the payload is recieved')
def step_impl(context):
    assert False