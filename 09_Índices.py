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
