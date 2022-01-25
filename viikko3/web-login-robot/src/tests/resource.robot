*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register
${USERNAME PASSWORD ERROR}  Invalid username or password
${USERNAME REGISTER ERROR}  Malformatted username, min. 3 characters, a-z
${PASSWORD ERROR}  Malformatted password (min. 8 characters, at least 1 other character than a-z)
${PASSWORD MATCH ERROR}  Passwords do not match

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Register Page Should Be Open
    Title Should Be  Register

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Go To Login Page
    Go To  ${LOGIN URL}

Go To Main Page
    Go To  ${HOME URL}

Go To Register Page
    Go To  ${REGISTER URL}