#24 agrupamento com mais de uma coluna
#qual é o preço médio de cada produto para cada região?
#agrupamento em duas colunas
data_final.groupby(['REGIÃO','PRODUTO'])
grupos = data_final.groupby(['REGIÃO','PRODUTO']) #colocar dentro de uma variavel
grupos

#retornando um dicionario
grupos.groups

#retornando o valor medio
grupos.mean()

#retornando media apenas de um grupo
grupos['PREÇO MÉDIO REVENDA'].mean()

#retornando descrição
grupos['PREÇO MÉDIO REVENDA'].describe()

---------------------------------------------------------------------------------------------
#agregar funções
#criar um dataframe para usar de exemplo
df = pd.DataFrame([
    [1,2,3],
    [10,20,30],
    [100, 200,300],
    [None, None,None]],
columns=['A','B','C'])
df

#agregar, realizar a soma e o minimo de cada coluna
df.agg([sum,min])
