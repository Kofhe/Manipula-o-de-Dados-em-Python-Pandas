#19 Limpeza de Dados
data

#verificar se possui valores vazios
data.info()

#possui alguns atributos errados (ex: o object mas era para ser float no preço medio)
#Conversão de tipos de atributos
#criar uma copia para não mexer no original
data_pre = data.copy()

#converter object em data
data_pre['DATA INICIAL'] = pd.to_datetime(data_pre['DATA INICIAL'])
data_pre['DATA FINAL'] = pd.to_datetime(data_pre['DATA FINAL'])

data_pre.info()

#dados numericos
#fazer a lista com o nome das colunas para conversão
#fazer um for
#para cada atributo na lista
#está convertendo a coluna e está sobreescrevendo para numero
#em caso de erro na conversão será atribuido no lugar null ou nan
for atributo in ['MARGEM MÉDIA REVENDA','PREÇO MÉDIO DISTRIBUIÇÃO','DESVIO PADRÃO DISTRIBUIÇÃO','PREÇO MÍNIMO DISTRIBUIÇÃO','PREÇO MÁXIMO DISTRIBUIÇÃO','COEF DE VARIAÇÃO DISTRIBUIÇÃO']:
    data_pre[atributo] = pd.to_numeric(data_pre[atributo], errors = 'coerce')

data_pre.info()
