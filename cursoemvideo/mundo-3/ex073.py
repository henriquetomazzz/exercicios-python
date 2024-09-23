'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato Basileiro de futebol, na ordem
de colocação. Depois mostre: 
a) Os 5 primeiros
b) Os 4 últimos colocados
c) Times em ordem alfabética
d) Em que posição está o time da Chapecoense'''
tabela = ('Grêmio','Palmeiras','Santos','Corinthians','Atlético Mineiro','Cruzeiro','Internacional','São Paulo','Flamengo','Fluminense','Atlético Paranaense',
'Botafogo','Vasco da Gama','Coritiba','Ponte Preta','Figueirense','Sport','Goiás','Chapecoense','Vitória')

print("-="*20)
print(f"Lisa de time do Basileirão: {tabela}")
print("-="*20)
print(f"Os 5 primeiros são {tabela[0:5]}")
print("-="*20)
print(f"Os 4 útimos são {tabela[-4:]}")
print("-="*20)
print(f"Time em ordem alfabética: {sorted(tabela)}")
print(f"O chapecoense está {tabela.index('Chapecoense')+1}ª posição")