import os
import subprocess
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class DriverConfig:
    """Gerencia configuração e criação do driver do Selenium."""

    @staticmethod
    def criar_chrome_options():
        """Cria opções do Chrome para reduzir logs.
        
        Returns:
            Options: Opções configuradas do Chrome
        """
        opts = Options()
        opts.add_experimental_option("excludeSwitches", ["enable-logging"])
        opts.add_argument("--log-level=3")
        return opts

    @staticmethod
    def criar_driver() -> Chrome:
        """Cria uma instância do WebDriver Chrome.
        
        Returns:
            Chrome: Driver do Chrome configurado
        """
        service = Service(
            ChromeDriverManager().install(),
            log_output=subprocess.DEVNULL
        )
        driver = Chrome(service=service, options=DriverConfig.criar_chrome_options())
        driver.maximize_window()
        return driver
