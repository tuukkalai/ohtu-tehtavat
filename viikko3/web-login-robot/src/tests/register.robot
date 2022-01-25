*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
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
    Register Should Fail With Message  ${USERNAME REGISTER ERROR}

Register With Valid Username And Too Short Password
    Set Username  matias
    Set Password  salis
    Set Password Confirmation  salis
    Submit Credentials
    Register Should Fail With Message  ${PASSWORD ERROR}

Register With Nonmatching Password And Password Confirmation
    Set Username  matias
    Set Password  Sala5ana2
    Set Password Confirmation  Salasana1
    Submit Credentials
    Register Should Fail With Message  ${PASSWORD MATCH ERROR}

Login After Successful Registration
	Create User And Go To Login Page
	Set Username  kalle
	Set Password  kalle123
	login_resource.Submit Credentials
	Login Should Succeed

Login After Failed Registration
	Set Username  matias
	Set Password  salis
	Set Password Confirmation  salis
	Click Button  Register
    Register Should Fail With Message  ${PASSWORD ERROR}
	Go To Login Page
	Login Page Should Be Open
	Set Username  matias
	Set Password  salis
	login_resource.Submit Credentials
	login_resource.Login Should Fail With Message  ${USERNAME PASSWORD ERROR}

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}
