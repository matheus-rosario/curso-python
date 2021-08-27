#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial
número = 0
while número >= 0:
  número = int(input('Digite um número: '))
  fatorial = factorial(número)
  print(f'O fatorial de {número} é {fatorial}')
