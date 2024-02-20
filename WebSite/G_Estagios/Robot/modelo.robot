*** Settings ***
Library   SeleniumLibrary
*** Variables ***

${URL}  http://127.0.0.1:8000/
${BTNLogin}  xpath=//a[@id='loginBtn]
*** Keywords ***
Abrir o website
    Open Browser  ${URL}  chrome
    [Teardown]  Close Browser

Fazer login
    Open Browser  ${URL}  chrome
    Click Element  css=#loginBtn
    Input Email  andre.c@ipvc.pt
    Input Password  Andre1gpg
    Submit Credentials
    [Teardown]  Close Browser

Input Email
    [Arguments]    ${email}
    Wait Until Element Is Visible    css=#email    timeout=10s
    Input Text  css=#email  ${email}

Input Password
    [Arguments]    ${Password}
    Input Text  css=#password  ${Password}

Submit Credentials
    Submit Form

*** Test Cases ***
cenario 1: abrir o Website
    Abrir o website

Cenario 2: Faz login
    Fazer login