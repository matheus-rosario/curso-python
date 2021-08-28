# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termos = primeiro + razão
contador = 1
print(primeiro, end=' -> ')
while contador < 10:
  print(termos, end=' -> ')
  termos += razão
  contador += 1
print('FIM')