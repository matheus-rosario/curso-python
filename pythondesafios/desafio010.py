'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar.'''
n = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Com R${n} reais você pode comprar US${n / 3.27:.2f} dólares')