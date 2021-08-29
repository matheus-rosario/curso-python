#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termos = primeiro + razão
contador = 1
print(primeiro, end=' -> ')
while contador < 10:
  print(termos, end=' -> ')
  termos += razão
  contador += 1
  if contador == 10:
    input('Quantos termos a mais você quer ver? ')