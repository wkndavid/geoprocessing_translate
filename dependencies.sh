#!/bin/bash

# installing pip
echo "Instalando pip :"
sudo apt install pip -y
#
echo "Instalando pandas :"
sudo pip install pandas

# installing openpyxl
echo "Instalando openpyxl :"
sudo pip install openpyxl

# installing dbfread
echo "Instalando dbfread :"
sudo pip install dbfread

# installing geopandas
echo "Instalando geopandas :"
sudo pip install geopandas

# installing pyarrow
echo "Instalando pyarrow :"
sudo pip install pyarrow