Feature: Re-Using Steps
    --------------------------------------------------------------------------------------------------------
    haha, { } goes brr
    --------------------------------------------------------------------------------------------------------
  
  @GIT
  Scenario: Test Success Git Login
    Given The Correct Git Credentials
    When Log in
    Then Status Code Should Be 200
    #The trick here is to make generic catching steps where the flexible part is caught in {} and passed to the function as an argument
    #Also, making context.response a generic response catcher on all other API resources allows us to use this same step to check ALL possibilities,
    #regardless of API feature or status code needed, as the step will expects context to have the response set in context.response 

    #More Condition checks can be added through the And keyword.
    #And Check another thing like headers

  @GIT
  Scenario: Test Fail Git Login
    Given The Incorrect Git Credentials
    When Log in
    Then Status Code Should Be 401
    #This Then is caught by the same handler function as the previous Scenario's. It works because the status code is not hard coded in the step itself.