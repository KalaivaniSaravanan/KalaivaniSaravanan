*** Settings ***
Library    RequestsLibrary
Library    BuiltIn


*** Variables ***
${API_URL}   https://paywize/api

*** Test Cases ***
Verify User Can Login via API
    ${response}=    POST    ${API_URL}/login    json={"username": "valid_user", "password": "valid_password"}
    Should Be Equal As Strings    ${response.status_code}    200
    Log    ${response.json()}
    Should Contain    ${response.json()}    "token"

Verify Payment API Response Time

    ${response}=    POST    ${API_URL}/payments    json={"amount": "100", "currency": "USD"}
    Should Be Equal As Strings    ${response.status_code}    201
    Log    ${response.elapsed.total_seconds()}

    Should Be Equal    1    1




