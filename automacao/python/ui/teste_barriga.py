from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://seubarriga.wcaquino.me/"
EMAIL_VALIDO = "a@a"
SENHA_VALIDA = "a"


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def acessar_pagina_login(self):
        self.driver.get(URL)

    def preencher_email(self, email):
        campo_email = self.wait.until(
            EC.visibility_of_element_located((By.ID, "email"))
        )
        campo_email.clear()
        campo_email.send_keys(email)

    def preencher_senha(self, senha):
        campo_senha = self.driver.find_element(By.ID, "senha")
        campo_senha.clear()
        campo_senha.send_keys(senha)

    def clicar_entrar(self):
        botao = self.driver.find_element(By.XPATH, "//button[contains(.,'Entrar')]")
        botao.click()

    def realizar_login(self, email, senha):
        self.preencher_email(email)
        self.preencher_senha(senha)
        self.clicar_entrar()

    def validar_mensagem_boas_vindas(self):
        mensagem = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='alert alert-success']")
            )
        )
        assert "Bem vindo" in mensagem.text
        print("✅ Login realizado com sucesso!")
        print("Mensagem exibida:", mensagem.text)


def criar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver


def teste_login_sucesso():
    driver = criar_driver()
    login_page = LoginPage(driver)

    try:
        login_page.acessar_pagina_login()
        login_page.realizar_login(EMAIL_VALIDO, SENHA_VALIDA)
        login_page.validar_mensagem_boas_vindas()

    finally:
        driver.quit()


if __name__ == "__main__":
    teste_login_sucesso()