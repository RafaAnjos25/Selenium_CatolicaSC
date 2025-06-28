import os
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()
secret = os.environ.get('SENHA')

# F12 no firefox va em Network clique em alguem get ou post depois Request Headers e copie o User-Agent
User_Agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0'
firefox_driver = os.path.join(os.getcwd(), 'geckodriver')
firefox_service = Service(firefox_driver)
firefox_options = Options()
firefox_options.set_preference('general.useragent.override', User_Agent)

browser = webdriver.Firefox(service=firefox_service, options=firefox_options)
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

usuario = browser.find_element(By.ID, "User")
usuario.send_keys("rafael.anjos")
senha = browser.find_element(By.ID, "Pass")
senha.send_keys(secret)
botao_acessar = browser.find_element(By.XPATH, "//input[@type='submit']")
botao_acessar.click()