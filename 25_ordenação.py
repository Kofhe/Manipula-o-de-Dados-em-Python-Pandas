#25 ordenação
#criar tabela ficticia de nota
notas = pd.DataFrame({
    'nome': ['João', 'Maria', 'José', 'Alice'],
    'idade': [20,21,19,20],
    'nota_final': [5.0,10.0,6.0,10.0]
})
notas

#organizar por descre pela nota (maior nota pela a menor)
notas.sort_values(by='nota_final',ascending=False)

#organizar por crescente pela nota e o nome
notas.sort_values(by=['nota_final','nome'])

#organizar por nome crescente e pela nota (maior nota pela a menor) 
notas.sort_values(by=['nota_final','nome'], ascending=[False,True])
