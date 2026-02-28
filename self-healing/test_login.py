import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_DIR = Path(__file__).resolve().parent

def new_driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1200,800")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)

def new_remote_driver():
    NODE_URL = "http://localhost:8085"  # Healenium proxy

    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1200,800")
    return webdriver.Remote(command_executor=NODE_URL, options=opts)

def _login_flow(driver, page_url: str):
    driver.get(page_url)

    email = driver.find_element(By.ID, "email")
    pwd   = driver.find_element(By.ID, "senha")
    btn = driver.find_element(By.XPATH, "//button[@type='submit']")

    email.send_keys("a@a")
    pwd.send_keys("a")
    btn.click()

    time.sleep(1)
    timestamp = int(time.time())
    screenshot_path = BASE_DIR / "images" / f"screenshot_{timestamp}.png"
    driver.save_screenshot(str(screenshot_path))

    msg_text = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-success").text
    assert "Bem vindo" in msg_text

def test_login():
    barriga_url = "https://seubarriga.wcaquino.me/"
    # barriga_url = "https://barrigareact.wcaquino.me"
    
    driver = new_driver() #Regular driver
    # driver = new_remote_driver() #Healenium driver

    try:
        _login_flow(driver, barriga_url)
    finally:
        driver.quit()