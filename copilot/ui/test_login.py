import os
import logging
import pytest
from selenium.webdriver.remote.remote_connection import LOGGER
from pages.login_page import LoginPage
from base.config import DriverConfig


# Configuração de logs
LOGGER.setLevel(logging.WARNING)
os.environ["WDM_LOG_LEVEL"] = "0"

# Dados de login
EMAIL = "a@a"
SENHA = "a"

# Credenciais inválidas para cenário negativo
EMAIL_INVALIDO = "invalido@a"
SENHA_INVALIDA = "b"


@pytest.fixture
def driver():
    """Fixture para criar e gerenciar o driver do Selenium."""
    chrome_driver = DriverConfig.criar_driver()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture
def login_page(driver):
    """Fixture que retorna a página de login."""
    return LoginPage(driver)


class TestLogin:
    """Testes para a funcionalidade de login."""

    def test_login_com_credenciais_validas(self, login_page):
        """Testa login com email e senha válidos."""
        login_page.acessar_pagina()
        login_page.realizar_login(EMAIL, SENHA)
        
        mensagem = login_page.obter_mensagem_sucesso()
        assert "bem vindo" in mensagem.lower(), f"Mensagem inesperada: {mensagem}"

    def test_login_com_credenciais_invalidas(self, login_page):
        """Testa que o sistema rejeita credenciais inválidas."""
        login_page.acessar_pagina()
        login_page.realizar_login(EMAIL_INVALIDO, SENHA_INVALIDA)

        mensagem = login_page.obter_mensagem_erro()
        assert "problemas com o login do usuário" in mensagem.lower(), f"Mensagem inesperada para credenciais inválidas: {mensagem}"
