from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import logging
import time
import os
import wget
import zipfile
import shutil

def encontrarLinks():
    service = Service(ChromeDriverManager().install())
    logging.basicConfig(level=logging.WARNING)
    chrome_options = Options()
    chrome_options.add_argument("--disable-logging") 
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--log-level=3") 
    driver = webdriver.Chrome(options=chrome_options)

    site = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    driver.get(site)

    time.sleep(5) 

    links = driver.find_elements(By.TAG_NAME, "a")

    anexos = ["Anexo I.", "Anexo II."]
    pdf_links = [None] * len(anexos)
    controle = 0

    while controle < len(anexos):
        for link in links:
            if anexos[controle] in link.text or anexos[controle] in link.get_attribute("href"):
                pdf_links[controle] = link.get_attribute("href")
                break
        controle += 1

    driver.quit() 

    return pdf_links

def compactarPdfs():
    links = encontrarLinks()

    if None in links:
        print("Erro: Não foi possível encontrar todos os links dos anexos.")
        return

    os.makedirs("./Testes-de-Nivelamento/pdfs", exist_ok=True)

    for posicao, link in enumerate(links):
        if link: 
            nome = "./Testes-de-Nivelamento/pdfs/Anexo {}.pdf".format(posicao + 1)
            wget.download(link, nome)
        else:
            print(f"Erro: O link para o Anexo {posicao + 1} não foi encontrado.")

    caminho_pasta = "./Testes-de-Nivelamento/pdfs"
    nome_zip = "./Testes-de-Nivelamento/anexos_compactados.zip"

  
    if os.listdir(caminho_pasta):
        with zipfile.ZipFile(nome_zip, "w") as zip:
            for file in os.listdir(caminho_pasta):
                caminho_arquivo = os.path.join(caminho_pasta, file)

                if os.path.isfile(caminho_arquivo):
                    zip.write(caminho_arquivo, os.path.basename(caminho_arquivo))
    
    shutil.rmtree(caminho_pasta)  

if __name__ == "__main__":
    compactarPdfs()
