#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostar que tipo de triângulo será formado:
#-Equilátero: Todos os lados iguais
#-Isósceles: Dois lados iguais
#-Escaleno: Todos os lados diferentes
reta1 = float(input('Tamanho da primeira reta: '))
reta2 = float(input('Tamanho da segunda reta: '))
reta3 = float(input('Tamanho da terceira reta: '))
if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta1 + reta3 > reta2:
  print('Esses valores podem formar um triângulo ', end='')
  if reta1 == reta2 == reta3:
    print('EQUILÁTERO!')
  elif reta1 != reta2 != reta3 != reta1:
    print('ESCALENO!')
  else:
    print('ISÓSCELES!')
else:
  print('Esses valoes não podem formar um triângulo!')