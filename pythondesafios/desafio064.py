#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
número = []
contador = 0
while 999 not in número:
  novo = int(input('Digite um número, (999 para parar): '))
  número.append(novo)
  contador += 1
total = sum(número)
print(f'Foram digitados {contador - 1} números e a soma entre eles tem o valor {total - 999}')