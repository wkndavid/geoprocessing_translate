import pandas as pd
import re
from dbfread import DBF
import logging

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

# Função para ler um arquivo DBF, traduzir e salvar
def traduzir_dbf_e_salvar(dbf_path, output_path, acronimos, traducoes):
    try:
        with DBF(dbf_path, encoding='utf-8') as table:
            registros_traduzidos = [traduzir_celulas(registro, acronimos, traducoes) for registro in table]
        df = pd.DataFrame(registros_traduzidos)
        df.to_excel(output_path, index=False, engine='openpyxl')
        logging.info(f"Arquivo DBF traduzido e salvo com sucesso")
    except Exception as e:
        logging.error(f"Erro ao processar o arquivo DBF: {str(e)}")
        raise

# Defina o dicionário de traduções
traducoes = {
    'SH' : 'SETOR HABITACIONAL',
    'ACR' :'ABRIGO CRISTO REDENTOR',
    'ADE' : 'ÁREA DE DESENVOLVIMENTO ECONÔMICO',
    'AE' : 'ÁREA ESPECIAL',

    # Setor Habitacional Contagem Sobradinho - está vazio...
}

# Caminho para o arquivo DBF de entrada
caminho_dbf = '/var/www/python3world/version3/ocupacoes_identificadas.dbf'

# Caminho de saída para o arquivo Excel
caminho_output_dbf = '/var/www/python3world/version3/teste-teste.xlsx'

# Execute as funções para traduzir o DBF e salvar como Excel
acr_preprocessados = preprocessar_dicionario(traducoes)
traduzir_dbf_e_salvar(caminho_dbf, caminho_output_dbf, acr_preprocessados, traducoes)
