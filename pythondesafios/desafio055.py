#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
peso = []
for c in range(0, 5):
  novo = float(input('Digite o peso: '))
  peso.append(novo)
print(f'O maior peso é {max(peso)}')