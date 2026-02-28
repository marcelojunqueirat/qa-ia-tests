*** Settings ***
Resource    teste_barriga.resource
Suite Setup    Abrir Navegador
Suite Teardown    Fechar Navegador

*** Variables ***
${EMAIL_VALIDO}    a@a
${SENHA_VALIDA}    a

*** Test Cases ***
Caso de Teste 1 - Login Bem-Sucedido
    [Documentation]    Valida login com sucesso
    Acessar Pagina de Login
    Realizar Login    ${EMAIL_VALIDO}    ${SENHA_VALIDA}
    Validar Mensagem de Boas Vindas
