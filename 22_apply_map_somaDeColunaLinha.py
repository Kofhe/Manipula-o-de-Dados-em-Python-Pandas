#22 apply soma coluna e linha, maps
#criar um dataframe para estudos
df = pd.DataFrame({'A':[1,2,3,4],
                   'B':[10,20,30,40],
                   'C':[100, 200,300,400]},
index = ['Linha 1', 'Linha 2','Linha 3','Linha 4'])
df

#é uma função para aplicar ao logo de um eixo de dataframe ou series
#eixo = 0 é linhas 
#eixo = 1 colunas
def nossa_soma (linha):
    return linha.sum() #retorna a soma de todos os valores de uma linha

    df['SOMA(A,B,C)'] = df.apply(nossa_soma, axis = 1) #é para cada linha
df

#mudar o eixo para series (colunas)
df.loc['Linha 5'] = df.apply(nossa_soma, axis = 0) #é para cada linha
df

#usando função lambda
#computar media das linhas
#primeiro filtrar as colunas e depois aplicar a lambda
df[['A','B','C']].apply(lambda series: series.mean(), axis = 1)
#criou uma coluna chamada média
df['MÉDIA(A,B,C)']=df[['A','B','C']].apply(lambda series: series.mean(), axis = 1)
df

#multiplicar apenas uma coluna
df['C'].apply(lambda x: x *2)
#criando a coluna
df['C*2'] = df['C'].apply(lambda x: x *2)
df
#----------------------------------------------------------------------------------
#map usando para cada elemento do dataframe
df = pd.DataFrame({'A':[1,2,3,4],
                   'B':[10,20,30,40],
                   'C':[100, 200,300,400]},
index = ['Linha 1', 'Linha 2','Linha 3','Linha 4'])
df

#retornar cada elemento ao quadrado
df.applymap(lambda x : x ** 2)
df
