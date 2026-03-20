#mostra algumas informações sobre o dataset
data.info()

#todo dataset carregado se chama data frame, ou seja, uma tabela de dados

#checar o tipo de dados de cada coluna
type(data)

#acessar as dimensões do dataset (numero de linhas e colunas) e irá retornar uma tupla (linhas, colunas)
data.shape
print(f'O dataset tem {data.shape[0]} linhas/observações/registros e {data.shape[1]} colunas/atributos/variáveis.')

#criar um dataframe com dicionario, as chaves representam as colunas e os valores da linha representam os dados
#coluna chamada index,nome, idade, peso, casa hogwarts
#index,nome,     idade, peso, casa hogwarts
#0    , harry     18    70.5   grifinoria
#1    , hermione  16    60.2   corvinal
#2    , ron       17    65.3   lufa-lufa

personagens_df = pd.DataFrame( #cria um dataframe vazio
    { #passar um dicionário para criar o dataframe
       'nome':['Harry Potter', 'Hermione Granger', 'Ron Weasley'],
        'idade':[18, 16, 17],
       'peso' : [70.5, 60.2, 65.3],
       'casa hogwarts':['grifinoria', 'corvinal', 'lufa-lufa']
        }
) 

personagens_df

#imprimir as informações do dataframe criado
personagens_df.info()

#irá retornar uma lista com os nomes das colunas do dataframe
personagens_df.columns

#converter o tipo de dados de tipo index para uma lista
list(personagens_df.columns)

#renomear a coluna
personagens_df 
personagens_df_renomeado = personagens_df.rename(columns={#vai passar um dicionario
'nome':'Nome Completo', #chave: nome da coluna antiga, valor: nome da coluna nova
'idade':'Idade'
})

#retornou a copia
personagens_df_renomeado

#retornar a propria tabela original sem criar uma copia
personagens_df.rename(columns={#vai passar um dicionario
'nome':'Nome Completo', #chave: nome da coluna antiga, valor: nome da coluna nova
'idade':'Idade'
}
, inplace=True #faça a alteração nessa tabela original 
)

#renomear todas as colunas é passar uma nova lista de nomes para as colunas
personagens_df.columns

personagens_df.columns = ['Nome Completo', 'Idade', 'Peso', 'Casa Hogwarts']

#conferir se mudou
personagens_df.columns
