#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
número = randint(0, 5)
print('Pensei em um numéro inteiro entre 0 e 5, tente adivinhar qual foi.')
palpite = int(input('Qual número eu pensei? '))
if palpite == número:
  print(f'Acertou! Eu pensei no número {palpite}')
else:
  print(f'Errou! Eu pensei no número {número}')
