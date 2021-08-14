#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostar que tipo de triângulo será formado:
#-Equilátero: Todos os lados iguais
#-Isósceles: Dois lados iguais
#-Escaleno: Todos os lados diferentes
reta1 = float(input('Digite o tamanho da primeira reta: '))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceira reta: '))
if reta1 == reta2 and reta1 == reta3:
  print('Essas retas formam um triângulo equilátero')
elif reta1 == reta2 and reta1 != reta3 or reta1 == reta3 and reta1 != reta2 or reta2 == reta3 and reta2 != reta1:
  print('Essas retas formar um triângulo isósceles')
elif reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta1 + reta3 > reta2:
  print('Essas retas formar um triângulo escaleno')
else:
  print('Essas retas não formar um triângulo')