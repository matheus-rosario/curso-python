'''Faça um programa que leia um ângulo qualquer e mostre
na tela o valore seno, cosseno e tangente desse ângulo.'''
import math
angulo = float(input('Digite um ângulo '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo}° tem o seno de {seno:.2f}, o cosseno de {cosseno:.2f} e a tangente de {tangente:.2f}.')