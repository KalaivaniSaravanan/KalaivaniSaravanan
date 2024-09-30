*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            https://paywize.com
${BROWSER}        Chrome

*** Test Cases ***
Verify User Can Log In With Valid Credentials
    Open Browser    ${URL}/login    ${BROWSER}
    Input Text      username    valid_user
    Input Text      password    valid_password
    Click Button     login_button
    Title Should Be  Dashboard
    Close Browser

Verify User Cannot Log In With Invalid Credentials
    Open Browser    ${URL}/login    ${BROWSER}
    Input Text      username    invalid_user
    Input Text      password    invalid_password
    Click Button     login_button
    ${error_message}=    Get Text    //div[@class='error']
    Should Contain    ${error_message}    Invalid credentials
    Close Browser

Test Payment Processing
    Open Browser    ${URL}/payment    ${BROWSER}
    Input Text      amount    100
    Select From List By Label    payment_method    Credit Card
    Input Text      card_number    4111111111111111
    Input Text      expiration_date    12/24
    Input Text      cvv    123
    Click Button     pay_button
    ${success_message}=    Get Text    //div[@class='success']
    Should Contain    ${success_message}    Payment successful
    Close Browser

Ensure User Can Register
    Open Browser    ${URL}/register    ${BROWSER}
    Input Text      email    newuser@example.com
    Input Text      password    Password123
    Click Button     register_button
    ${confirmation_message}=    Get Text    //div[@class='confirmation']
    Should Contain    ${confirmation_message}    Registration successful
    Close Browser

Check User Cannot Register With Existing Email
    Open Browser    ${URL}/register    ${BROWSER}
    Input Text      email    existinguser@example.com
    Input Text      password    Password123
    Click Button     register_button
    ${error_message}=    Get Text    //div[@class='error']
    Should Contain    ${error_message}    Email already in use
    Close Browser

Verify Transaction History Is Displayed
    Open Browser    ${URL}/login    ${BROWSER}
    Input Text      username    valid_user
    Input Text      password    valid_password
    Click Button     login_button
    Go To    ${URL}/transactions
    ${transactions}=    Get WebElements    //div[@class='transaction']
    Should Be True    ${transactions}
    Close Browser

Verify User Can Log Out
    Open Browser    ${URL}/login    ${BROWSER}
    Input Text      username    valid_user
    Input Text      password    valid_password
    Click Button     login_button
    Click Button     logout_button
    Title Should Be  Login
