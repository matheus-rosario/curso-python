#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
próximo = primeiro + razão
print(primeiro)
print(próximo)
for c in range(1, 9):
  próximo += razão
  print(próximo)
