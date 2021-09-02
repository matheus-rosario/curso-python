#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
#Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
termos = int(input('Quantos termos você quer ver? '))
primeiro = 0
segundo = 1
terceiro = primeiro + segundo
contador = 3
print(f'{primeiro}', end=' -> ')
print(f'{segundo}', end=' -> ')
while contador <= termos:
  print(f'{terceiro}', end=' -> ')
  primeiro = segundo
  segundo = terceiro
  terceiro = primeiro + segundo
  contador += 1
print('FIM')