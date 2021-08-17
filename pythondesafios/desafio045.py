#Crie um programa que faça o computador jogar Jokenpô com com você.
from random import randint
computador = randint(1, 3)
print('Vamos jogar Jokenpô, escolha sua jogada: \n1 - Pedra \n2 - Papel \n3 - Tesoura')
jogador = int(input('Sua Jogada: '))
if jogador == 1 and computador == 1:
  print(f'Computador jogou Pedra \nVocê jogou Pedra \nEMPATE!')
#elif jogador == 1 and computador == 2:
