#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maiores = 0
menores = 0
ano = date.today().year
for c in range(1, 8):
  nascimento = int(input(f'Em que ano a {c}° pessoa nasceu? '))
  idade = ano - nascimento
  if idade >= 21:
    maiores += 1
  else:
    menores += 1
print(f'Ao todo tivemos {maiores} pessoas maiores de idade')
print(f'E também tivemos {menores} pessoas menores de idade')