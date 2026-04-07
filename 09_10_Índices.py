#Índices
data.index

#para passar a lista de índices para uma variável, basta usar a função list() para converter o objeto Index em uma lista comum do Python
list(data.index)

#ou 

data.index.to_list()

#indices textuais
#irei criar uma tabela para usar de exemplo
pesquisa_de_satisfacao = pd.DataFrame({
    'bom':[50, 21, 100],
    'ruim':[131, 2, 30],
    'pessimo':[30, 20, 1]
}, index=['XboxOne','PlayStation4','NintendoSwitch'])

pesquisa_de_satisfacao.head()

#apresentou as strings do índice, ou seja, os nomes dos consoles
pesquisa_de_satisfacao.index

#selecao por indice
#indexação
#index-based selection, ou seja, selecionar dados usando os índices

#mostrando linhas especificas de um dataframe usando o método iloc: seleciona elementos por posição baseado em seu indice (numérico/row-first,column-second ou seja linha primeiro, coluna depois)
data.iloc[1] #seleciona a primeira linha do dataset, ou seja, a linha indexada por 1

#selecionando multiplas linhas
#passar um intervalo e fazer um fatiamento, ou seja, selecionar as linhas de 1 a 3 (o 3 não é incluido)
#selecionando as linhas de indice de 0 a 5(incluso)
data.iloc[0:6]

#selecionando as linhas de indice de 10 a 15(incluso)
data.iloc[10:16]

#selecionando as linhas/observações de indice 1, 5, 10 e 15
#passar uma lista de índices para o método iloc, ou seja, selecionar as linhas indexadas por 1, 5, 10 e 15
data.iloc[[1, 5, 10, 15]]

#selecionando as linhas/observações de indices 5, 1, 15, 10
data.iloc[[5, 1, 15, 10]]

#retornar o valor da linha de indice 1 e coluna 3 ('ESTADO')
data.iloc[1,3]
