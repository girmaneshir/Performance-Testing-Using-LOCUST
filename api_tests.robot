*** Settings ***
Library           RequestsLibrary
Library           OperatingSystem
Library           Collections
Library           SeleniumLibrary

*** Variables ***
${BASE_URL}      http://127.0.0.1:5000
${USER_ID}      1
${SESSION_NAME}  my_session

*** Test Cases ***
Create User
    [Documentation]    Test that a user can be created successfully.
    Create Session    ${SESSION_NAME}    ${BASE_URL}
    ${response}=    POST On Session    ${SESSION_NAME}    /users    json={"name": "John Doe"}
    Should Be Equal As JSON    ${response.json()}    {"id": ${USER_ID}, "name": "John Doe"}

Get All Users
    [Documentation]    Test that the API returns a list of users.
    ${response}=    GET On Session    ${SESSION_NAME}    /users
    Should Be Equal As JSON    ${response.json()}    [{"id": ${USER_ID}, "name": "John Doe"}]

Get User By ID
    [Documentation]    Test that a user can be retrieved by ID.
    ${response}=    GET On Session    ${SESSION_NAME}    /users/${USER_ID}
    Should Be Equal As JSON    ${response.json()}    {"id": ${USER_ID}, "name": "John Doe"}

Update User
    [Documentation]    Test that a user can be updated successfully.
    ${response}=    PUT On Session    ${SESSION_NAME}    /users/${USER_ID}    json={"name": "Jane Doe"}
    Should Be Equal As JSON    ${response.json()}    {"id": ${USER_ID}, "name": "Jane Doe"}

Delete User
    [Documentation]    Test that a user can be deleted successfully.
    DELETE On Session    ${SESSION_NAME}    /users/${USER_ID}
    ${response}=    GET On Session    ${SESSION_NAME}    /users/${USER_ID}
    Should Be Equal    ${response.status_code}    404

Create Sample Users
    [Documentation]    Test that sample users can be added successfully.
    ${response}=    POST On Session    ${SESSION_NAME}    /users/sample
    Should Be Equal As JSON    ${response.json()}    {"message": "Sample users added."}

Verify Sample Users
    [Documentation]    Test that all sample users are returned.
    ${response}=    GET On Session    ${SESSION_NAME}    /users
    Should Contain    ${response.json()}    {"name": "Jane Smith"}
    Should Contain    ${response.json()}    {"name": "Alice Johnson"}
    Should Contain    ${response.json()}    {"name": "Bob Brown"}
    Should Contain    ${response.json()}    {"name": "Charlie Davis"}
    Should Contain    ${response.json()}    {"name": "Diana Prince"}
    Should Contain    ${response.json()}    {"name": "Ethan Hunt"}
    Should Contain    ${response.json()}    {"name": "Fiona Apple"}
    Should Contain    ${response.json()}    {"name": "George Washington"}
    Should Contain    ${response.json()}    {"name": "Hannah Montana"}

*** Keywords ***
Should Be Equal As JSON
    [Arguments]    ${actual}    ${expected}
    Should Be True    ${actual} == ${expected}