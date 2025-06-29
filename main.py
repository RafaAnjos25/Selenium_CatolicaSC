import os, time
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()
secret = os.environ.get('SENHA')

browser = webdriver.Firefox()
browser.get("https://www.catolicasc.org.br/")

# Tela cheia
browser.maximize_window()

# Clicar no botao Ja sou aluno
ja_sou_aluno = browser.find_element(By.CLASS_NAME, "title")
ja_sou_aluno.click()

portal_do_aluno = browser.find_element(By.LINK_TEXT, "Portal do Aluno")
portal_do_aluno.click()

windows = browser.window_handles
browser.switch_to.window(windows[1])

time.sleep(3)
try:
    usuario = browser.find_element(By.ID, "User")
    usuario.send_keys("rafael.anjos")
    senha = browser.find_element(By.ID, "Pass")
    senha.send_keys('sadaasdsadassdasd')
    botao_acessar = browser.find_element(By.XPATH, "//input[@type='submit']")
    botao_acessar.click()
    url_atual = browser.current_url
    url_esperada = "https://portal.catolicasc.org.br/Corpore.Net//Source/EDU-EDUCACIONAL/Public/EduPortalAlunoLogin.aspx?AutoLoginType=ExternalLogin&undefined"
    assert url_atual == url_esperada
    time.sleep(3)
    browser.back()
except Exception as e:
    print(f"Pagina diferente da esperada") 

time.sleep(3)
try:
    usuario = browser.find_element(By.ID, "User")
    usuario.send_keys("rafael.anjos")
    senha = browser.find_element(By.ID, "Pass")
    senha.send_keys(secret)
    botao_acessar = browser.find_element(By.XPATH, "//input[@type='submit']")
    botao_acessar.click()
    time.sleep(3)
    url_atual = browser.current_url
    url_esperada = "https://portal.catolicasc.org.br/FrameHTML//web/app/edu/PortalEducacional/#/"
    assert url_atual == url_esperada
except Exception as e:
    print(f"Pagina diferente da esperada") 