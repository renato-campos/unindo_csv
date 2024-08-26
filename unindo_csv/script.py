import os
import pandas as pd

# Caminho para a pasta onde estão os arquivos CSV
pasta_csv = 'data_in'

# Lista para armazenar os DataFrames
dataframes = []

# Percorre todos os arquivos na pasta
for arquivo in os.listdir(pasta_csv):
    if arquivo.endswith('.csv'):
        caminho_arquivo = os.path.join(pasta_csv, arquivo)

        # Lê o CSV e adiciona à lista de DataFrames
        df = pd.read_csv(caminho_arquivo)
        dataframes.append(df)

# Concatena todos os DataFrames
df_unido = pd.concat(dataframes, ignore_index=True)

# Salva o DataFrame unido em um novo arquivo CSV
df_unido.to_csv('data_out/arquivo_final.csv', index=False)

print("Todos os arquivos CSV foram unidos com sucesso!")
