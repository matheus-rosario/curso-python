#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
peso = []
for c in range(1, 6):
  novo = float(input(f'Digite o peso da {c}° pessoa: '))
  peso.append(novo)
print(f'O maior peso lido foi de {max(peso)}Kg')
print(f'O menor peso lido foi de {min(peso)}Kg')