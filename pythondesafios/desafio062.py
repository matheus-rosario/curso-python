#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termos = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
  total = total + mais
  while contador <= total:
    print(termos, end=' -> ')
    termos += razão
    contador += 1
  print('PAUSA')
  mais = int(input('Quantos termos a mais você quer ver? '))
print(f'A progressão terminou com {total} termos mostrados.')
