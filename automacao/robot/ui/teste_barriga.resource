*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}                 https://seubarriga.wcaquino.me/
${BROWSER}             chrome
${EMAIL_FIELD}         id=email
${PASSWORD_FIELD}      id=senha
${LOGIN_BUTTON}        xpath=//button[contains(.,'Entrar')]
${WELCOME_MESSAGE}     xpath=//div[@class='alert alert-success' and contains(.,'Bem vindo')]

*** Keywords ***
Abrir Navegador
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    ${service}=    Evaluate    sys.modules['selenium.webdriver.chrome.service'].Service(sys.modules['webdriver_manager.chrome'].ChromeDriverManager().install())    sys, selenium.webdriver.chrome.service, webdriver_manager.chrome
    Create Webdriver    Chrome    service=${service}    options=${options}
    Go To    ${URL}
    Maximize Browser Window
    Set Selenium Timeout    10s

Fechar Navegador
    Close Browser

Acessar Pagina de Login
    Go To    ${URL}
    Wait Until Element Is Visible    ${EMAIL_FIELD}

Preencher Email
    [Arguments]    ${email}
    Input Text    ${EMAIL_FIELD}    ${email}

Preencher Senha
    [Arguments]    ${senha}
    Input Password    ${PASSWORD_FIELD}    ${senha}

Clicar Botao Entrar
    Click Button    ${LOGIN_BUTTON}

Realizar Login
    [Arguments]    ${email}    ${senha}
    Preencher Email    ${email}
    Preencher Senha    ${senha}
    Clicar Botao Entrar

Validar Mensagem de Boas Vindas
    Wait Until Element Is Visible    ${WELCOME_MESSAGE}
    Element Should Contain    ${WELCOME_MESSAGE}    Bem vindo