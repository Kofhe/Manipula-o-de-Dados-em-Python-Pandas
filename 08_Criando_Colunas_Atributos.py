#criar uma nova coluna
#para criar uma nova coluna basta atribuir uma lista de valores/series ou uma constante a uma nova chave do dataframe


#criando uma coluna a partir de um valor constante, todas as linhas terão o mesmo valor
data['coluna sem nocao'] = 'DEFAULT'
data

#criar a partir de uma lista
#data.shape é uma tupla com o numero de linhas e colunas do dataset, data.shape[0] é o numero de linhas do dataset
data['coluna a partir de lista'] = range(data.shape[0]) #range(data.shape[0]) cria uma lista de numeros de 0 até o numero de linhas do dataset
data

#vai dar erro porque a lista tem apenas 3 elementos, mas o dataset tem mais de 3 linhas
data['nao funciona'] = [1, 2, 3]

#criar coluna atraves de uma existente
#O 6 é o valor do dólar em reais, ou seja, estamos convertendo o preço médio de revenda de dólares para reais
data['PREÇO MÉDIO REVENDA (dólares)'] = data['PREÇO MÉDIO REVENDA'] * 6.0
data
