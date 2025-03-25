import pdfplumber
import pandas as pd
import zipfile
import os

def PegarTabela():
    anexo_I = "2 - Teste de Tranformação de dados\Anexo 1.pdf"
    tabelas = []

    with pdfplumber.open(anexo_I) as pdf:
        for pagina in pdf.pages:
            table = pagina.extract_table()
            if table:
                df = pd.DataFrame(table[1:], columns=table[0])
                tabelas.append(df)
    
    return tabelas

def converterParaCSV(tabelas):

    tabela_final = pd.concat(tabelas, ignore_index=True)

    tabela_final = tabela_final.rename(columns={"OD": " Seg. Odontológica", "AMB": "Seg. Ambulatorial"})

    tabela_final.to_csv("2 - Teste de Tranformação de dados/Tabela.csv", index=False)

def compactar():

    with zipfile.ZipFile("2 - Teste de Tranformação de dados/Teste__{Leonardo_Madeira}.zip", "w") as zip:
        zip.write("2 - Teste de Tranformação de dados/Tabela.csv", arcname="Tabela.csv")

    csv_caminho = os.path.join( "2 - Teste de Tranformação de dados/Tabela.csv")
    os.remove(csv_caminho)

if __name__ == "__main__":
    tabelas = PegarTabela()
    converterParaCSV(tabelas)
    compactar()

