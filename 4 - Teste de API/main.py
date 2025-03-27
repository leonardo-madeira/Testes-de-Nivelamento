from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

origins = [
    "http://localhost:8080", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("Relatorio_cadop.csv", sep=";")

colunas_interessantes = [
    "CNPJ", "Razao_Social", "Cidade",
    "DDD", "Telefone"
]

@app.get("/buscar")
def buscar_operadora(termo: str = Query(..., min_length=2, description="Termo de busca")):
    if "Razao_Social" not in df.columns:
        return {"erro": "Coluna 'Razao_Social' não encontrada no arquivo CSV."}
    
    resultados = pd.DataFrame()
    
    for coluna in colunas_interessantes:
        coluna_str = df[coluna].astype(str)
        resultados = pd.concat([resultados, df[coluna_str.str.contains(termo, case=False, na=False)]])
    
    resultados = resultados.drop_duplicates()

    resultados = resultados[colunas_interessantes].fillna("")

    resultados["DDD"] = pd.to_numeric(resultados["DDD"], errors="coerce").fillna("0").astype(int).astype(str)

    resultados["Telefone_Completo"] = resultados["DDD"] + " " + resultados["Telefone"].astype(str)

    colunas_retorno = colunas_interessantes + ["Telefone_Completo"]

    return resultados[colunas_retorno].to_dict(orient="records")