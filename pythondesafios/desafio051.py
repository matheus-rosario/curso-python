#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
próximo = primeiro + (10 - 1) * razão
for c in range(primeiro, próximo, razão):
  print(c, end= ' -> ')
print('FIM')
