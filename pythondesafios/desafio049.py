#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
#só que agora utilizando um laço for.
n = int(input('Digite um número: '))
print('-='*10)
print(f'A tabuada do número {n} é a seguinte:')
for c in range(0, 11):
  print(f'{n} * {c} = {n * c}')
print('-='*10)