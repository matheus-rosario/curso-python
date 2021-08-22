#Crie um programa que faça o computador jogar Jokenpô com com você.
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('Vamos jogar Jokenpô, escolha sua jogada: \n0 - Pedra \n1 - Papel \n2 - Tesoura')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 15)
print(f'O computador jogou {itens[computador]}')
print(f'Você jogou {itens[jogador]}')
if computador == 0:
  if jogador == 0:
    print('EMPATOU!')
  elif jogador == 1:
    print('VOCÊ VENCEU!')
  elif jogador == 3:
    print('O COMPUTADOR VENCEU!')
  else:
    print('JOGADA INVÁLIDA!')
elif computador == 1:
  if jogador == 0:
    print('O COMPUTADOR VENCEU!')
  elif jogador == 1:
    print('EMPATOU!')
  elif jogador == 2:
    print('O JOGADOR VENCEU!')
  else:
    print('JOGADA INVÁLIDA')
elif computador == 2:
  if jogador == 0:
    print('O JOGADOR VENCEU!')
  elif jogador == 1:
    print('O COMPUTADOR VENCEU!')
  elif jogador == 2:
    print('EMPATOU!')
  else:
    print('JOGADA INVALIDA!')
print('-=' * 15)