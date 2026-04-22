#16 filtragem com mais de uma comparação
#selecionando registros de postos do rio de janeiro com preços acimas de 2 reais

data.head()

#quais são do rj ou não
data['ESTADO'] == 'RIO DE JANEIRO'

#quais registros que possuem preço media de revenda
data['PREÇO MÉDIO REVENDA'] > 2.0

#guardamos dentro de uma variavel
selecao = (data['ESTADO'] == 'RIO DE JANEIRO') & (data['PREÇO MÉDIO REVENDA']> 2
selecao

#vai filtrar apenas os true
data[selecao]

selecao_1 = data['ESTADO'] == 'RIO DE JANEIRO'
postos_rj = data[selecao_1]
postos_rj
