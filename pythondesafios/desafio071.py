#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
valor = int(input('Qual o valor a ser sacado? R$'))
cedula50 = cedula20 = cedula10 = cedula1 = 0
while True:
  while valor - 50 >= 0:
    valor -= 50
    cedula50 += 1
  while valor - 20 >= 0:
    valor -= 20
    cedula20 += 1
  while valor - 10 >= 0:
    valor -= 10
    cedula10 += 1
  while valor - 1 >= 0:
    valor -= 1
    cedula1 += 1
  break
if cedula50 > 0:
  print(f'Total de cédulas de 50: {cedula50}')
if cedula20 > 0:
  print(f'Total de cédulas de 20: {cedula20}')
if cedula10 > 0:
  print(f'Total de cédulas de 10: {cedula10}')
if cedula1 > 0:
  print(f'Total de cédulas de 1: {cedula1}')