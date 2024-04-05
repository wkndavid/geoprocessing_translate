import pandas as pd

# Caminho para o arquivo DBF
caminho_dbf = '/var/www/python3world/python3_translater_files_geoprocessing/teste/lotes_registrados.dbf'  # Substitua pelo caminho do seu arquivo DBF

# Tamanho do chunk (em linhas)
chunk_size = 100000  # Defina o tamanho do chunk conforme necessário

# Função para processar cada chunk
def process_chunk(chunk):
    # Aqui você pode realizar operações de processamento nos dados do chunk
    # Por exemplo, você pode filtrar, manipular ou analisar os dados
    # Neste exemplo, apenas vamos exibir as primeiras linhas do chunk
    print(chunk.head())

# Loop para ler o arquivo em chunks e processá-lo
for chunk in pd.read_csv(caminho_dbf, chunksize=chunk_size):
    process_chunk(chunk)
    
# => path
# /var/www/python3world/python3_translater_files_geoprocessing/teste/lotes_registrados.dbf