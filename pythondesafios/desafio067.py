#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 
número = contador = total = 0
while True:
  número = int(input('Quer ver a tabuada de qual número? '))
  if número < 0:
    print('PROGRAMA ENCERRADO.')
    break
  print('-='*10)
  while contador < 10:
    contador += 1
    total = número * contador
    print(f'{número} * {contador} = {total}')
  contador = 0
  print('-='*10)