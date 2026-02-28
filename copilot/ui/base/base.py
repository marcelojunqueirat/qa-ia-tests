from selenium.webdriver.support.ui import WebDriverWait


# Configurações Globais
BASE_URL = "https://seubarriga.wcaquino.me/"
TIMEOUT_PADRAO = 10


class BasePage:
    """Classe base para Page Objects com funcionalidades comuns."""

    def __init__(self, driver):
        """Inicializa a página base com o driver do Selenium.
        
        Args:
            driver: Instância do WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT_PADRAO)

    def acessar_pagina(self, url=None):
        """Acessa uma página específica ou a URL base.
        
        Args:
            url (str, optional): URL a acessar. Se None, usa BASE_URL.
        """
        url_alvo = url or BASE_URL
        self.driver.get(url_alvo)

    def obter_titulo_pagina(self):
        """Retorna o título da página.
        
        Returns:
            str: Título da página
        """
        return self.driver.title

    def fechar_driver(self):
        """Fecha a sessão do driver."""
        self.driver.quit()
