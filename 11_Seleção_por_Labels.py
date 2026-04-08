#irei criar uma tabela para usar de exemplo
pesquisa_de_satisfacao = pd.DataFrame({
    'bom':[50, 21, 100],
    'ruim':[131, 2, 30],
    'pessimo':[30, 20, 1]
}, index=['XboxOne','PlayStation4','NintendoSwitch'])

pesquisa_de_satisfacao.head()

#seleção por rótulo
#label-based selection, ou seja, selecionar dados usando os rótulos dos índices (row-first,column-second ou seja linha primeiro, coluna depois)

#retorna a linha de indice 0 que é uma linha implicito, usando o método iloc
#selecionar a linha indexada por 'XboxOne'
pesquisa_de_satisfacao.iloc[0]

#retorna o valor da linha de indice 0 (implicitamente indexada por 'XboxOne') e coluna 1 (impliticamente indexada por 'bom'), usando o método iloc
pesquisa_de_satisfacao.iloc[0,1]

#retorna a linha indexada por 'XboxOne' usando o método loc, ou seja, selecionar a linha usando o rótulo do índice
pesquisa_de_satisfacao.loc['XboxOne']

#NÃO FUNCIONA ==> iloc não funciona com rótulos, ou seja, não é possível selecionar a linha indexada por 'XboxOne' usando o método iloc, porque iloc só funciona com índices numéricos, ou seja, índices baseados em posição.
#pesquisa_de_satisfacao.iloc['XboxOne']

#ou 
#não funciona porque loc não funciona com índices numéricos
pesquisa_de_satisfacao.loc[0]

#quantidade de pessoas que avalizaram o playstation 4 como ruim
pesquisa_de_satisfacao.loc['PlayStation4', 'ruim']

#lista de indices rotulados
pesquisa_de_satisfacao.loc[['XboxOne', 'NintendoSwitch']]

#retorna todas as linhas e apenas as colunas com rótulos 'bom' e 'pessimo'
pesquisa_de_satisfacao[['bom', 'pessimo']]

#ou
#começa passando um intervalo de linhas usando o operador : para selecionar todas as linhas de 0 a todas as linhas, e depois passando a lista de colunas com rótulos 'bom' e 'pessimo' para selecionar apenas essas colunas
pesquisa_de_satisfacao.loc[:, ['bom', 'pessimo']]

#com o data.loc, ou seja, usando o método loc para selecionar a linha indexada por 1, ou seja, a linha com rótulo 1
data.loc[1]
