*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    https://barrigarest.wcaquino.me
${EMAIL}       a@a
${SENHA}       a
${TOKEN}

*** Keywords ***
Criar Sessao API
    Create Session    barriga    ${BASE_URL}

Autenticar Usuario
    ${body}=    Create Dictionary    email=${EMAIL}    senha=${SENHA}
    ${response}=    POST On Session    barriga    /signin    json=${body}
    Should Be Equal As Integers    ${response.status_code}    200
    ${json}=    Set Variable    ${response.json()}
    ${token}=    Get From Dictionary    ${json}    token
    Set Suite Variable    ${TOKEN}

Criar Header Autenticado
    ${headers}=    Create Dictionary    Authorization=JWT ${TOKEN}
    RETURN    ${headers}

Criar Conta
    [Arguments]    ${nome_base}
    ${timestamp}=    Get Time    epoch
    ${nome_conta}=    Set Variable    ${nome_base}_${timestamp}
    ${headers}=    Criar Header Autenticado
    ${body}=    Create Dictionary    nome=${nome_conta}
    ${response}=    POST On Session    barriga    /contas    json=${body}    headers=${headers}
    Should Be Equal As Integers    ${response.status_code}    201
    ${json}=    Set Variable    ${response.json()}
    ${id}=    Get From Dictionary    ${json}    id
    RETURN    ${id}

Atualizar Conta
    [Arguments]    ${conta_id}    ${novo_nome}
    ${headers}=    Criar Header Autenticado
    ${body}=    Create Dictionary    nome=${novo_nome}
    ${response}=    PUT On Session    barriga    /contas/${conta_id}    json=${body}    headers=${headers}
    Should Be Equal As Integers    ${response.status_code}    200

Remover Conta
    [Arguments]    ${conta_id}
    ${headers}=    Criar Header Autenticado
    ${response}=    DELETE On Session    barriga    /contas/${conta_id}    headers=${headers}
    Should Be Equal As Integers    ${response.status_code}    204