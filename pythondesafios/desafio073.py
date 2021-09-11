#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Chapecoense.
tabela = 'Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Corinthians', 'Fluminense', 'Atlético-GO', 'Athletico-PR', 'Ceará', 'Cuiabá', 'Internacional', 'Juventude', 'Santos', 'São Paulo', 'Bahia', 'América-MG', 'Sport', 'Grêmio', 'Chapecoense'
posiçãoChapeco = tabela.index('Chapecoense',)
print('-='*20)
print(f'Os 5 primeros colocados são: {tabela[:5]} ')
print('-='*20)
print(f'Os 4 últimos colocados são: {tabela[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-='*20)
print(f'O Chapecoense está em {posiçãoChapeco + 1}° posição')