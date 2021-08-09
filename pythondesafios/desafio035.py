#Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se eles podem formar um triângulo.
reta1 = float(input('Tamanho da primeira reta: '))
reta2 = float(input('Tamanho da segunda reta: '))
reta3 = float(input('Tamanho da terceira reta: '))
if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta1 + reta3 > reta2:
  print('Esses valores podem formar um triângulo!')
else:
  print('Esses valoes não podem formar um triângulo!')