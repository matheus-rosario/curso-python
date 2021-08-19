#Crie um programa que faça o computador jogar Jokenpô com com você.
import random
pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'
computador = random.choice([pedra, papel, tesoura])
print('Vamos jogar Jokenpô, escolha sua jogada: \n1 - Pedra \n2 - Papel \n3 - Tesoura')
jogador = int(input('Sua Jogada: '))
if jogador == computador:
  print(f'Computador jogou {computador.upper()} \nVocê jogou {jogador} \nEMPATE!')
else:
  print('Jogada Inválida')