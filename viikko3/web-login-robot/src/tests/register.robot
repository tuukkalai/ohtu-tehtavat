*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  matias
    Set Password  sala5ana1
    Set Password Confirmation  sala5ana1
    Submit Credentials
	Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ma
    Set Password  sala5ana1
    Set Password Confirmation  sala5ana1
    Submit Credentials
    Register Should Fail With Message  Malformatted username, min. 3 characters, a-z

Register With Valid Username And Too Short Password
    Set Username  matias
    Set Password  salis
    Set Password Confirmation  salis
    Submit Credentials
    Register Should Fail With Message  Malformatted password (min. 8 characters, at least 1 other character than a-z)

Register With Nonmatching Password And Password Confirmation
    Set Username  matias
    Set Password  Sala5ana2
    Set Password Confirmation  Salasana1
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}
