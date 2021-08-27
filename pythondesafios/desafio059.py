#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
  print('='*20)
  print('Escolha uma das opções abaixo: \n[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
  opção = int(input('Sua escolha: '))
  if opção == 1:
    print(f'A soma entre {valor1} e {valor2} é {valor1 + valor2}')
  if opção == 2:
    print(f'O resultado de {valor1} x {valor2} é {valor1 * valor2}')
  if opção == 3:
    if valor1 > valor2:
      print(f'Entre {valor1} e {valor2} o maior é o {valor1}')
    else:
      print(f'Entre o {valor1} e {valor2} o maior é o {valor2}')
  if opção == 4:
    print('Quais os novos valore?')
    valor1 = int(input('Primeiro valor: '))
    valor2 = int(input('Segundo Valor: '))
print('FIM DO PROGRAMA')