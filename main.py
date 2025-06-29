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
    url_atual1 = browser.current_url
    url_esperada1 = "https://portal.catolicasc.org.br/Corpore.Net//Source/EDU-EDUCACIONAL/Public/EduPortalAlunoLogin.aspx?AutoLoginType=ExternalLogin&undefined"
    assert url_atual1 == url_esperada1
    time.sleep(2)
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
    url_atual2 = browser.current_url
    url_esperada2 = "https://portal.catolicasc.org.br/FrameHTML//web/app/edu/PortalEducacional/#/"
    assert url_atual2 == url_esperada2
except Exception as e:
    print(f"Pagina diferente da esperada") 

browser.get("https://www.catolicasc.org.br/")

try:
    botao_bolsas = browser.find_element(By.LINK_TEXT, "Bolsas e Financiamentos")
    botao_bolsas.click()
    url_atual3 = browser.current_url
    url_esperada3 = "https://www.catolicasc.org.br/academicos/bolsas-e-financiamentos/"
    assert url_atual3 == url_esperada3
except Exception as e:
    print("Botao nao encontrado")
