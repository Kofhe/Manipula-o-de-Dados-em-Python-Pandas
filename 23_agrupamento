#23 agrupamento
data_final.head()

#groupby, cria grupos de elementos
#agrupar todas as regiões e cria um objeto
data_final.groupby('REGIÃO')

grupo = data_final.groupby('REGIÃO') #guardei dentro da variavel grupo
grupo

#trouxe um dicionario (chave e valor)
grupo.groups

#trouxe um array
grupo.indices

#trouxe apenas um grupo
grupo.get_group('CENTRO OESTE')

#descrever estatisticas descritivas de cada grupo
grupo.describe()

#menor valor
grupo.min()
