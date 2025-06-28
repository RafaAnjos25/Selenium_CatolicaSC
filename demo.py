from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
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