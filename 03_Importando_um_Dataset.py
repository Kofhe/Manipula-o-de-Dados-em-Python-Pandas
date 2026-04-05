#instalar extensão notebook jupyter
#pip install pandas

import pandas as pd
#baixar dados desse site https://www.kaggle.com/datasets/matheusfreitag/gas-prices-in-brazil?resource=download

#importar o arquivo csv por caminho relativo ou seja usando uma pasta atual como referencia
# O sep ='\t' ajuda o pandas a dividir corretamente as colunas usando o tab como separador, já que o arquivo é um TSV (Tab-Separated Values)
pd.read_csv('2004-2021.tsv', sep='\t')

#criei uma variavel chamada data para armazenar o dataset
data = pd.read_csv('2004-2021.tsv', sep='\t')
#vai exibir as 5 primeiras linhas do dataset com a variavel data criada antes
data.head()

#ver as 10 primeiras linhas
data.head(10)
