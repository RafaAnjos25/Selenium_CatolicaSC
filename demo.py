from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

User_Agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0'
firefox_driver = os.path.join(os.getcwd(), 'geckodriver')
firefox_service = Service(firefox_driver)
firefox_options = Options()
firefox_options.set_preference('general.useragent.override', User_Agent)

browser = webdriver.Firefox(service=firefox_service, options=firefox_options)
#browser.get('https://www.vivaolinux.com.br/artigo/Como-compartilhar-a-tela-do-Ubuntu-com-uma-Smart-TV-LG-Samsung-etc/')

browser.get("https://www.catolicasc.org.br/")

wait = WebDriverWait(browser, 10)

ja_sou_aluno = browser.find_element(By.CLASS_NAME, "title")

ja_sou_aluno.click()
wait.until(EC.presence_of_element_located(ja_sou_aluno))# Tempo de espera com condicao

# Selecionar elementos com a mesma classe
lista_botoes = browser.find_elements("class name", "label")

for botao in lista_botoes:
    if "Pós-graduação" in botao.text:
        botao.click()
        break

# Trocar de aba
windows = browser.window_handles
browser.switch_to.window(windows[1])
browser.get("https://selenium-python.readthedocs.io/locating-elements.html")