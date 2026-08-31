import pathlib

import pandas as pd

PREFIX = "Mortalidade_Geral"

def read_columns(src, year):
    # ; como separador por que é assim nos arquivos .csv que encontramos
    columns = pd.read_csv(src / f"{PREFIX}_{year}.csv", sep = ";", nrows = 0).columns

    return {c.upper() for c in columns}


def columns_info(src = pathlib.Path("data/raw"), start = 1979, end = 2026):
    # nrwos = 0 pra pegar somente o nome das columas
    common_columns = read_columns(src, start)
    total_columns = set() | common_columns

    for i in range(start+1, end+1):
        year_columns = read_columns(src, i)
        common_columns &= year_columns
        total_columns |= year_columns

    # sorted pra que o retorno seja uma lista e esteja sempre na mesma ordem entre execuções
    return sorted(common_columns), sorted(total_columns)

def columns_summary(src = pathlib.Path("data/raw"), start = 1979, end = 2026):
    common_columns, total_columns = columns_info(src, start, end)

    return {
        "start": start,
        "end": end,
        "columns": common_columns,
        "common_cardinality": len(common_columns),
        "total_cardinality": len(total_columns)
    }

def columns_matrix(src = pathlib.Path("data/raw"), start = 1979, end = 2026):
    # dicionário mapeando year -> column[]
    columns_by_year = {}
    total_columns = set()
    years = list(range(start, end+1))

    # loop quase idêntico no columns_info(), ver se tem como separar em uma função
    for y in years:
        year_columns = read_columns(src, y)
        columns_by_year[y] = year_columns
        total_columns |= year_columns

    # dicionário mapeando column -> boolean[]; o que seŕa salvo no CSV
    data = {} 

    for c in sorted(total_columns):
        is_present = []

        for y in years:
            is_present.append(c in columns_by_year[y])

        data[c] = is_present

    return pd.DataFrame(data, index = years)
