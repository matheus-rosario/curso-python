#faça um progarama que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#-Se ele ainda vai se alistar ao serviço militar.
#-Se é a hora de se alistar.
#-Se já passou do tempo do alistamento.
# Seu programa também deverá mostar o tempo que falta ou que passou do prazo.
from datetime import date
ano= date.today().year
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = ano - nascimento
if idade == 18:
  print('Já é hora de se alistar!')
elif idade > 18:
  print(f'Ja se passaram {idade - 18} anos do prazo para se alistar!')
elif idade < 18:
  print(f'Faltam {18 - idade} anos para se alistar!')