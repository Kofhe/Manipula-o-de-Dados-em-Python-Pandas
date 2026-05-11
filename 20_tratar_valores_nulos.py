#20 Tratar valores nulos
#função = isnull irá verificar se é nulo 
#criar variavel chamada mask para armazenar os dados
mask = data_pre['PREÇO MÉDIO DISTRIBUIÇÃO'].isnull()

#NaN é nulo ou null
data_pre[mask]

#verificar os dados originais, quais eram os valores do PREÇO MÉDIO DISTRIBUIÇÃO dos registros que agora possuem valores NAN
data[mask]

#preencher todos os valores nulos (NaN) com um valor padrão com fillna e ele irá retornar uma copia
data_pre_fill = data_pre.fillna(0)
data_pre_fill

#preencheu tudo com 0
data_pre_fill[mask]

#nextap alteramos o dataframe preprocessado
data_pre[mask]

#passar um dicionario quaL coluna é para preencher e o valor
data_pre_fill = data_pre.fillna (value={
    'PREÇO MÉDIO DISTRIBUIÇÃO': 10,
    'DESVIO PADRÃO DISTRIBUIÇÃO': 20,
    'PREÇO MÍNIMO DISTRIBUIÇÃO': 30,
     'PREÇO MÁXIMO DISTRIBUIÇÃO': 'vazio'   
})
data_pre_fill
data_pre_fill[mask]

#remover amostras que possuem valores NaN (nulo)
data_pre.dropna(inplace=True) 
data_pre.info()

#salvar o dataset preprocessado
data_pre.to_csv('C:/Users/andre/Desktop/Estudos sozinha/Estudos pandas/preprocessado.csv')
