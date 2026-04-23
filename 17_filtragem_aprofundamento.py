#17 filtragem aprofundamento
#selecionar registros de posto de são paulo ou rio de janeiro com gasolina comum acima de 2 reais
#jeito lento primeiro
data.head()

(data['ESTADO'] == 'SAO PAULO') | (data['ESTADO'] == 'RIO DE JANEIRO') #| significa ou 

#Guarda na variavel a seleção dos postos de são paulo ou rio de janeiro
selecao_1 = (data['ESTADO'] == 'SAO PAULO') | (data['ESTADO'] == 'RIO DE JANEIRO') 

#produtos que tem gasolina comum 
selecao_2 = data['PRODUTO'] == 'GASOLINA COMUM'

#preço médio de revenda acima de 2 reais
selecao_3 = data['PREÇO MÉDIO REVENDA'] > 2.0

#combinar as 3 seleções usando o operador & (e)
selecao_final = selecao_1 & selecao_2 & selecao_3
selecao_final

data[selecao_final]

#jeito rapido
selecao_1 = (data['ESTADO'] == 'SAO PAULO') | (data['ESTADO'] == 'RIO DE JANEIRO') 
postos_sp_rj = data[selecao_1]

#apenas registros de postos dos estados de sao paulo e rio de janeiro
postos_sp_rj

#apenas registros de postos dos estados de sao paulo e rio de janeiro com gasolina comum
selecao_2 = (postos_sp_rj['PRODUTO'] == 'GASOLINA COMUM')
postos_sp_rj_gasolina_comum = postos_sp_rj[selecao_2]

postos_sp_rj_gasolina_comum

#qual do data que criamos possui os registros de postos de são paulo ou rio de janeiro com gasolina comum acima de 2 reais?
selecao_3 = (postos_sp_rj_gasolina_comum['PREÇO MÉDIO REVENDA'] > 2.0)
posto_sp_rj_gasolina_comum_acima_2_reais = postos_sp_rj_gasolina_comum[selecao_3]
posto_sp_rj_gasolina_comum_acima_2_reais
