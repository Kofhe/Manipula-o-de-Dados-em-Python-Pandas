#Voltando ao que estava mexendo

import pandas as pd
#baixar dados desse site https://www.kaggle.com/datasets/matheusfreitag/gas-prices-in-brazil?resource=download

#importar o arquivo csv por caminho relativo ou seja usando uma pasta atual como referencia
# O sep ='\t' ajuda o pandas a dividir corretamente as colunas usando o tab como separador, já que o arquivo é um TSV (Tab-Separated Values)
pd.read_csv('2004-2021.tsv', sep='\t')

#criei uma variavel chamada data para armazenar o dataset
data = pd.read_csv('2004-2021.tsv', sep='\t')
#vai exibir as 5 primeiras linhas do dataset com a variavel data criada antes
data.head()

#selecionando uma coluna inteira
data['ESTADO']

#Outra fornma de acessar a mesma coluna, tem que usar o nome igualzinho, só funciona para colunas 
# com nome sem espaço, ou seja, sem acentos, sem hífen, etc.
data.ESTADO

#Extrair uma data linha
#selecionando a observação indexada por 1, ou seja, a segunda linha do dataset
data.iloc[1]

#Alterar o nome dos índices
pd.Series([5.5,6.0,9.5], index=['prova 1', 'prova 2', 'projeto'], name='Notas dos alunos hogwarts')

#atribuindo dados
#mostrando o nosso dataframe
data.head()

data['PRODUTO'] #a series retornada refente a coluna, NÃO É UMA COPIA, mas sim uma REFERENCIA/VIEW a coluna do dataframe
produto_view = data['PRODUTO']
produto_view

#guardar uma copia
produto_copy = data['PRODUTO'].copy() #retorna uma copia da coluna 'PRODUTO'
produto_copy

#atribuir um valor/constante para todas as linhas da coluna
data['PRODUTO'] = 'Combustível'
data

#data.shape mostra o numero de linhas e colunas do dataset
#nrows = numero de linhas
#ncols = numero de colunas
nrows, ncols = data.shape
nrows, ncols

#De python list comprehension, criar uma lista de produtos novos, usando o numero de linhas do dataset para criar a lista
#criou a varial = novos_produtos 
#f'Produto {i}' = f-string, que serve para colocar valores dentro de texto
#for i in range(nrows) = list comprehension.É uma forma curta de criar listas.

#“Crie uma lista com os nomes Produto 0, Produto 1, Produto 2... até a quantidade de linhas.”
novos_produtos = [f'Produto {i}' for i in range(nrows)]
novos_produtos

#len = retorna o numero de elementos de uma lista, ou seja, o numero de produtos criados
len(novos_produtos)

#atribuir a lista de novos produtos a coluna 'PRODUTO' do dataset
data['PRODUTO'] = novos_produtos
data.head()

#voltando os antigos produtos pelo o backup 

data['PRODUTO'] = produto_copy #produto_copy é uma series
data.head()
