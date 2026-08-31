#

Projeto de visualização de dados para ..., trabalhada na disciplina Visualização de Dados do Bacharelado em Ciência da Computação da Universidade Tecnológica Federal do Paraná.

Estudantes: André Felipe Wonsik Alves, Gustavo Martins França e Maria Eduarda Bambini.

## Uso

- Baixe os datasets em https://drive.google.com/drive/folders/1Dr5Poxj8_S7hHxg9vj47xWIjrE8neCkt?usp=sharing

- `$ make unzip src=PATH dst=PATH`: descomprime todos os arquivos .zip em `src` para `dst`. Por padrão, `src` = `dst` = `data/raw`

- `$ make columns src=PATH out=PATH start=YEAR end=YEAR`: computa metadados sobre as colunas dos datasets do ano `start` até `end` e os salva em `out`. Por padrão, `src` = `data/raw`, `out` = `data/processed`, `start` = 1979 e `end` = 2026

# Pré-processamentos

- Foi computado o conjunto máximo de colunas em comum entre todos os datasets para os anos ..... Por conta de ...., foi(ram) considerado(s) o(s) intervalo(s) de anos tal, tal e tal.

## Faltantes

- Mapear todos os códigos desconhecidos para strings
- Construir datasets com as contagens relevantes para as visualizações. Por exemplo, um dataset com as relações causa_de_morte -> [quantidade_causa_de_morte, quantidade_causa_de_morte_por_genero, quantidade_causa_de_morte_por_cor, x_y_z_causa_de_morte_a_b_c, ...]
