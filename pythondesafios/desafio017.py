#Faça um programa que leia um comprimento do cateto oposto
#e do cateto adjacente de um triângulo retângulo, calcule
#e mostre o comprimento da hipotenusa.
from math import sqrt
oposto = float(input('Qual o comprimento do cateto oposto? '))
adjacente = float(input('Qual o comprimento do cateto adjacente? '))
print(f'O comprimento da hipotenusa é {sqrt((oposto ** 2) + (adjacente ** 2)):.2f}')