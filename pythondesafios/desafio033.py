#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
import math
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))
menor = numero1
if numero2<numero1 and numero2<numero3:
  menor = numero2
if numero3<numero1 and numero3<numero2:
  menor = numero3
maior = numero1
if numero2>numero1 and numero2>numero3:
  maior = numero2
if numero3>numero1 and numero3>numero2:
  maior = numero3
print(f'O menor número é o {menor}.')
print(f'O maior número é o {maior}.')