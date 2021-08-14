#A Confederação Nacional de Natação precisa de um programa que leia a data de nascimento de um atléta e mostre sua categoria, de acordo com a idade:
#-Até 9 anos: MIRIM
#-Até 14 anos: INFANTIL
#-Até 19 anos: JUNIOR
#-Até 20 anos: SÊNIOR
#-Acima: MASTER
from datetime import date
ano = date.today().year
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = ano - nascimento
if idade <= 9:
  print('Sua categoria é: MIRIM!')
elif idade > 9 and idade <= 14:
  print('Sua categoria é: INFANTIL')
elif idade > 14 and idade <= 19:
  print('Sua caegoria é: JUNIOR')
elif idade > 19 and idade <= 20:
  print('Sua categoria é: SÊNIOR')
elif idade > 20:
  print('Sua categoria é: MASTER')