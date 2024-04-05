import geopandas as gpd

# Caminho para o shapefile (.shp) local
caminho_shapefile = '/var/www/html/version2/files/teste/teste.shp'

# Le o shapefile para um GeoDataFrame ajustando a codificação
try:
    gdf = gpd.read_file(caminho_shapefile, encoding='utf-8')
except UnicodeDecodeError:
    try:
        gdf = gpd.read_file(caminho_shapefile, encoding='utf-16')
    except UnicodeDecodeError:
        gdf = gpd.read_file(caminho_shapefile, encoding='latin-1')

# Caminho para salvar o arquivo Excel localmente (com a extensão .xlsx)
caminho_excel = '/var/www/html/version2/files/resultados/results_shp_to_excel/result_shp_to_excel.xlsx'

# Remove a coluna de geometria temporariamente para evitar erros
gdf_temp = gdf.copy()
del gdf_temp['geometry']

# Salva o GeoDataFrame como um arquivo Excel usando o Pandas
gdf_temp.to_excel(caminho_excel, index=False, engine='openpyxl', encoding='utf-8')


    