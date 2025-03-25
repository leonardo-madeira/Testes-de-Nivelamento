from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

site = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

driver.get(site)

time.sleep(5)

links = driver.find_elements(By.TAG_NAME, "a")
pdf_links = ["", ""]

anexos = ["Anexo I.", "Anexo II."]

controle = 0
while controle <= (len(anexos) - 1):
    for link in links:
        if anexos[controle] in link.text or anexos[controle] in link.get_attribute("href"):
            pdf_links[controle] = link.get_attribute("href")

    if pdf_links[controle]:
            print(f"Anexo {controle + 1}: {pdf_links[controle]}")
    else:
            print(f"O anexo {controle + 1} não foi encontrado")


    controle += 1