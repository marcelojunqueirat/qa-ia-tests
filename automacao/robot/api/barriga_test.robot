*** Settings ***
Resource    barriga_keywords.resource
Suite Setup    Setup API

*** Keywords ***
Setup API
    Criar Sessao API
    Autenticar Usuario

*** Test Cases ***
Fluxo Completo - Gerenciamento de Conta
    ${conta_id}=    Criar Conta    Conta_Automacao
    Atualizar Conta    ${conta_id}    Conta_Atualizada
    Remover Conta    ${conta_id}

Teste Criar Conta
    ${conta_id}=    Criar Conta    Conta_Teste
    Remover Conta    ${conta_id}

Teste Atualizar Conta
    ${conta_id}=    Criar Conta    Conta_Teste
    Atualizar Conta    ${conta_id}    Conta_Editada
    Remover Conta    ${conta_id}

Teste Remover Conta
    ${conta_id}=    Criar Conta    Conta_Teste
    Remover Conta    ${conta_id}
