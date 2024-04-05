import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
# Caminho para o arquivo Excel (.xls .xlsx) local
caminho_excel = '/var/www/html/version2/files/for_test_setor.xlsx'

# Ler dados do Excel para um DataFrame do pandas
dados_excel = pd.read_excel(caminho_excel)

print(dados_excel)

# Adicionar uma geometria de ponto fictícia
geometry = [Point(0, 0) for _ in range(len(dados_excel))]
gdf = gpd.GeoDataFrame(dados_excel, geometry=geometry, crs='EPSG:4326')

# Caminho para salvar o shapefile localmente (com a extensão .shp)
caminho_shapefile = '/var/www/html/version3/files/resultados/results_excel_to_shp/results_excel_to_shp.shp'

# SaivarOGeoDataFramee como shapefile usando o GeoPandas
gdf.to_file(caminho_shapefile, driver='ESRI Shapefile')
