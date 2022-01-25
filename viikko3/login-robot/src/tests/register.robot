*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
	Input Credentials  matias  salasana123
	Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
	Input Credentials  matias  salasana123
	Output Should Contain  New user registered
	Input New Command
	Input Credentials  matias  salasana234
	Output Should Contain  User with username matias already exists

Register With Too Short Username And Valid Password
	Input Credentials  eh  salasana123
	Output Should Contain  Malformatted username, min. 3 characters, a-z

Register With Valid Username And Too Short Password
	Input Credentials  matias  12salis
	Output Should Contain  Malformatted password (min. 8 characters, at least 1 other character than a-z)

Register With Empty Username And Valid Password
	Input Credentials  ${EMPTY}  salasana123
	Output Should Contain  Username and password are required

Register With Valid Username And Empty Password
	Input Credentials  matias  ${EMPTY}
	Output Should Contain  Username and password are required

Register With Valid Username And Long Enough Password Containing Only Letters
	Input Credentials  matias  onlyletterpassword
	Output Should Contain  Malformatted password (min. 8 characters, at least 1 other character than a-z)



*** Keywords ***
Input New Command And Create User
	Input New Command
	Create User  matias  Salasana123!