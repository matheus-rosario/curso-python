#Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas. 
# - Quantas letras ao todo (sem considerar espaços). 
# - Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: '))
print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
quantidade = len(nome) - nome.count(' ')
print(f'Seu nome ao todo contém {quantidade} letras')
primeiro = nome.split()
print(f'Seu primeiro nome contém {len(primeiro[0])} letras.')