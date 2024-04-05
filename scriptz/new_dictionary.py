import pandas as pd
import re
import logging
import json
from dbfread import DBF
from dbf import *

# Configurando o logging
logging.basicConfig(filename='traducao.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Função para pré-processar o dicionário e armazenar os acrônimos
def preprocessar_dicionario(traducoes):
    acronimos = set()
    for palavra in traducoes.values():
        acronimos.update(palavra.upper().split())
    return acronimos

# Função para traduzir as células
def traduzir_celulas(registro, acronimos, traducoes):
    novo_registro = {}
    for coluna, valor in registro.items():
        novo_valor = []
        palavras = re.findall(r'\b\w+\b', str(valor))
        for palavra in palavras:
            if palavra.upper() in acronimos:
                try:
                    traduzida = traducoes[palavra.upper()]
                    novo_valor.append(traduzida) 
                except KeyError as e:
                    logging.error(f"Erro ao traduzir palavra '{palavra}': {str(e)}")
                    novo_valor.append(palavra)
            else:
                novo_valor.append(palavra)
        novo_registro[coluna] = ' '.join(novo_valor)
    return novo_registro

# Função para ler um arquivo DBF, traduzir e salvar em um arquivo DBF
def traduzir_dbf_e_salvar_arquivo_dbf(dbf_path, output_path, acronimos, traducoes):
    try:
        with DBF(dbf_path, encoding='utf-8') as table:
            registros_traduzidos = [traduzir_celulas(registro, acronimos, traducoes) for registro in table]

        # Obtendo os nomes de campo e dados traduzidos
        nomes_campos = list(registros_traduzidos[0].keys())
        dados_traduzidos = [list(registro.values()) for registro in registros_traduzidos]

        # Criar um novo arquivo DBF
        dbf = DBF(output_path)

        # Adicionar campos ao arquivo DBF
        for nome_campo in nomes_campos:
            dbf.addField(nome_campo)

        # Adicionar registros ao arquivo DBF
        for dado in dados_traduzidos:
            dbf.add(dado)

        # Fechar o arquivo DBF
        dbf.close()

        logging.info(f"Dados traduzidos e salvos no arquivo DBF '{output_path}' com sucesso")
    except Exception as e:
        logging.error(f"Erro ao processar o arquivo DBF e salvar no arquivo DBF: {str(e)}")
        raise

# Carregar o dicionário de traduções do arquivo JSON
with open('/var/www/python3world/python3_translater_files_geoprocessing/scripts/traducoes.json', 'r') as arquivo_json:
    traducoes = json.load(arquivo_json)

# Caminho para o arquivo DBF de entrada
caminho_dbf = '/var/www/python3world/python3_translater_files_geoprocessing/quadras.dbf'

# Caminho de saída para o arquivo DBF
caminho_output_dbf = '/var/www/python3world/resultado2.dbf'

# Execute as funções para traduzir o DBF e salvar no arquivo DBF
acr_preprocessados = preprocessar_dicionario(traducoes)
traduzir_dbf_e_salvar_arquivo_dbf(caminho_dbf, caminho_output_dbf, acr_preprocessados, traducoes)
