#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
número = contador = soma = 0
número = int(input('Digite um número, (999 para parar): '))
while número != 999:
  soma += número
  contador += 1
  número = int(input('Digite um número, (999 para parar): '))
print(f'Foram digitados {contador} números e a soma entre eles tem o valor {soma}')