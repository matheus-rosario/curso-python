#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
soma = contador = 0
resultado = ''
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)
while True:
  computador = randint(0, 10)
  número = int(input('Digite um valor: '))
  jogador = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
  soma = computador + número
  print('-'*15)
  if soma % 2 == 0:
    resultado = 'P'
    print(f'Você jogou {número} e o computador {computador}. Total de {soma} DEU PAR')
    print('-'*15)
  else:
    resultado = 'I'
    print(f'Você jogou {número} e o computador {computador}. Total de {soma} DEU ÍMPAR')
    print('-'*15)
  if resultado == jogador:
    contador += 1
    print('VOCÊ VENCEU!')
    print('Vamos jogar novamente...')
    print('-='*15)
  else:
    print('VOCÊ PERDEU!')
    print('-='*15)
    print(f'GAME OVER! Você venceu {contador} vezes.')