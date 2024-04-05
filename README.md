# Tradução de Arquivos DBF

## Descrição:

Este script Python permite traduzir os dados de um arquivo DBF (dBase) para um novo arquivo DBF, substituindo os acrônimos encontrados nos campos pelos seus respectivos significados. Ele também registra quaisquer erros de tradução em um arquivo de log.

## Funcionalidades:

- Tradução de acrônimos nos campos de um arquivo DBF.
- Registro de erros de tradução em um arquivo de log.

## Requisitos:

- Python 3.x
- Pandas
- dbfread
- dbf

## Como Usar:

1. Defina o dicionário de traduções no script. Adicione novos acrônimos e seus respectivos significados conforme necessário.
   
2. Especifique o caminho para o arquivo DBF de entrada (caminho_dbf) e o caminho para o arquivo DBF de saída (caminho_output_dbf) no script.

3. Execute o script Python.

## Exemplo de Uso:
python3 translate_script.py --input arquivo_entrada.txt --output arquivo_saida.txt

## Documentação das Funções:

### preprocessar_dicionario(traducoes)

Esta função pré-processa o dicionário de traduções e retorna um conjunto contendo todos os acrônimos presentes no dicionário.

#### Parâmetros:
- `traducoes`: Dicionário de traduções contendo acrônimos e seus respectivos significados.

#### Retorno:
- `acronimos`: Conjunto de acrônimos extraídos do dicionário de traduções.

### traduzir_celulas(registro, acronimos, traducoes)

Esta função traduz os acrônimos nas células de um registro do arquivo DBF.

#### Parâmetros:
- `registro`: Dicionário representando um registro do arquivo DBF.
- `acronimos`: Conjunto de acrônimos a serem traduzidos.
- `traducoes`: Dicionário de traduções contendo acrônimos e seus respectivos significados.

#### Retorno:
- `novo_registro`: Dicionário representando o registro traduzido.

### traduzir_dbf_e_salvar_arquivo_dbf(dbf_path, output_path, acronimos, traducoes)

Esta função lê um arquivo DBF, traduz os dados e salva em um novo arquivo DBF.

#### Parâmetros:
- `dbf_path`: Caminho para o arquivo DBF de entrada.
- `output_path`: Caminho para o arquivo DBF de saída.
- `acronimos`: Conjunto de acrônimos a serem traduzidos.
- `traducoes`: Dicionário de traduções contendo acrônimos e seus respectivos significados.

## Configuração do Logging:

O script configura o registro de log para registrar mensagens de informação e erro em um arquivo traducao.log.

## Autor:

# [David Jesus]
## Data:

# [05/04/2024]
# geoprocessing_translate
