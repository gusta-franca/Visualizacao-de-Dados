import os
import json
import pandas as pd

PASTA_JSON = "../src/dictionaries"
PASTA_CSV = "../src/dictionaries/converted"

def alinhar(objeto, prefixo, linhas):
    for chave in objeto:
        valor = objeto[chave]
        if prefixo == "":
            caminho = chave
        else:
            caminho = prefixo + "." + chave

        if isinstance(valor, dict):
            alinhar(valor, caminho, linhas)
        else:
            linhas.append((caminho, str(valor)))


def ler_dicionario(caminho_json):
    with open(caminho_json, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    linhas = []
    alinhar(dados, "", linhas)
    return pd.DataFrame(linhas, columns=["chave", "valor"])


os.makedirs(PASTA_CSV, exist_ok=True)
nomes = sorted(os.listdir(PASTA_JSON))
tabelas = []

for i in range(len(nomes)):
    nome = nomes[i]
    if not nome.lower().endswith(".json"):
        continue

    nome_base = nome[:-5]
    tabela = ler_dicionario(os.path.join(PASTA_JSON, nome))

    caminho_csv = os.path.join(PASTA_CSV, nome_base + ".csv")
    tabela.to_csv(caminho_csv, index=False, encoding="utf-8-sig")

    tabela.insert(0, "variavel", nome_base)
    tabelas.append(tabela)

if len(tabelas) > 0:
    todas = pd.concat(tabelas, ignore_index=True)
    todas.to_csv(os.path.join(PASTA_CSV, "dicionarios.csv"), index=False, encoding="utf-8-sig")
else:
    print("Nenhum .json encontrado em", PASTA_JSON)