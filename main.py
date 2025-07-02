import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()
secret = os.environ.get('SENHA')

browser = webdriver.Firefox()
wait = WebDriverWait(browser, 10)

browser.get("https://www.catolicasc.org.br/")
print("Open on https://www.catolicasc.org.br/ OK")

# Tela cheia
browser.maximize_window()
print("Maximize windows. OK")

# Clicar no botao Ja sou aluno
ja_sou_aluno = browser.find_element(By.CLASS_NAME, "title")
ja_sou_aluno.click()
print("Click Ja sou aluno. OK")

portal_do_aluno = browser.find_element(By.LINK_TEXT, "Portal do Aluno")
portal_do_aluno.click()
print("Click portal do aluno OK.")

windows = browser.window_handles
browser.switch_to.window(windows[1])
print("Window selection. Ok")

print("USER AND PASS FAIL TEST")
wait.until(EC.element_to_be_clickable((By.ID, "User"))).click()
usuario = browser.find_element(By.ID, "User")
usuario.send_keys("rafael.anjos")
print("User field. OK")

senha = browser.find_element(By.ID, "Pass")
senha.send_keys('sadaasdsadassdasd')
print("Senha field. Ok")

botao_acessar = browser.find_element(By.XPATH, "//input[@type='submit']")
botao_acessar.click()
print("Access Button. Ok")

url_atual1 = browser.current_url
url_esperada1 = "https://portal.catolicasc.org.br/Corpore.Net//Source/EDU-EDUCACIONAL/Public/EduPortalAlunoLogin.aspx?AutoLoginType=ExternalLogin&undefined"
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "td:nth-child(2) > .ModalMessageBoxCloseButton"))).click()
if url_atual1 == url_esperada1:
    print("Pass and user fail test. SUCESS")
else:
    print("Pass and user fail test. FAIL")  

print("USER AND PASS SUCESS TEST")
wait.until(EC.element_to_be_clickable((By.ID, "User"))).click()
usuario = browser.find_element(By.ID, "User")
usuario.send_keys("rafael.anjos")
print("User field. OK")

senha = browser.find_element(By.ID, "Pass")
senha.send_keys(secret)
print("Senha field. Ok")

botao_acessar = browser.find_element(By.XPATH, "//input[@type='submit']")
botao_acessar.click()
print("Access Button. Ok")

time.sleep(15)
print("Wait catolica pages. OK")

wait.until(EC.element_to_be_clickable((By.ID, "show-menu")))
print("Show-menu button. OK")

url_atual2 = browser.current_url
url_esperada2 = "https://portal.catolicasc.org.br/FrameHTML//web/app/edu/PortalEducacional/#/"
if url_atual2 == url_esperada2:
    print("Pass and user sucess test. SUCESS")
else:
    print("Pass and user sucess test. FAIL")


browser.quit()
print("END TEST")