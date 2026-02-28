from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base import BasePage


class LoginPage(BasePage):
    """Page Object para a página de login do Seu Barriga."""

    # Localizadores dos elementos
    CAMPO_EMAIL = (By.ID, "email")
    CAMPO_SENHA = (By.ID, "senha")
    BOTAO_ENTRAR = (By.XPATH, "//button[text()='Entrar']")
    MENSAGEM_SUCESSO = (By.XPATH, "//div[@class='alert alert-success']")
    MENSAGEM_ERRO = (By.XPATH, "//div[contains(@class,'alert-danger')]")

    def preencher_email(self, email):
        """Preenche o campo de email.
        
        Args:
            email (str): Email a ser inserido
        """
        campo_email = self.driver.find_element(*self.CAMPO_EMAIL)
        campo_email.clear()
        campo_email.send_keys(email)

    def preencher_senha(self, senha):
        """Preenche o campo de senha.
        
        Args:
            senha (str): Senha a ser inserida
        """
        campo_senha = self.driver.find_element(*self.CAMPO_SENHA)
        campo_senha.clear()
        campo_senha.send_keys(senha)

    def clicar_entrar(self):
        """Clica no botão Entrar."""
        botao = self.driver.find_element(*self.BOTAO_ENTRAR)
        botao.click()

    def obter_mensagem_sucesso(self):
        """Aguarda e retorna a mensagem de sucesso.
        
        Returns:
            str: Texto da mensagem de sucesso
        """
        mensagem_element = self.wait.until(
            EC.presence_of_element_located(self.MENSAGEM_SUCESSO)
        )
        return mensagem_element.text

    def obter_mensagem_erro(self):
        """Aguarda e retorna a mensagem de erro exibida após tentativa de login mal sucedida.
        
        Returns:
            str: Texto da mensagem de erro
        """
        mensagem_element = self.wait.until(
            EC.presence_of_element_located(self.MENSAGEM_ERRO)
        )
        return mensagem_element.text

    def realizar_login(self, email, senha):
        """Realiza o login com email e senha.
        
        Args:
            email (str): Email do usuário
            senha (str): Senha do usuário
        """
        self.preencher_email(email)
        self.preencher_senha(senha)
        self.clicar_entrar()
