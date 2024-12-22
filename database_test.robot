*** Settings ***
Library           DatabaseLibrary
Library           OperatingSystem

*** Variables ***
${DB_PATH}       C:/Users/user/Desktop/SQAT2024_CEP_2024/Lab_SQAT/Lab_06_PerformanceTest_Using_Python/users.db

*** Test Cases ***
Check Database Exists
    [Documentation]    Check if the database exists, and create if it does not.
    ${exists}=    Run Keyword And Return Status    File Should Exist    ${DB_PATH}
    Run Keyword If    not ${exists}    Create Database

Validate Users Table Exists
    [Documentation]    Check if the "user" table exists in the database.
    Connect To Database    sqlite:///${DB_PATH}
    ${result}=    Query    SELECT name FROM sqlite_master WHERE type='table' AND name='user';
    Should Not Be Empty    ${result}
    Disconnect From Database

Validate Sample Users
    [Documentation]    Validate that sample users are in the database.
    Connect To Database    sqlite:///${DB_PATH}
    ${result}=    Query    SELECT * FROM user
    Log    Sample Users: ${result}
    Should Not Be Empty    ${result}
    Disconnect From Database

*** Keywords ***
Create Database
    [Documentation]    Create the database and the user table if it does not exist.
    Connect To Database    sqlite:///${DB_PATH}
    Execute Sql    CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);
    Disconnect From Database