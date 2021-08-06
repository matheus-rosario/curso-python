#Faça um algoritimo que leia o preço de um produto
#e mostre seu novo preço, com 5% de desconto.
p = float(input('Qual o preço do produto? R$'))
print(f'Na liquidação esse produto tem 5% de desconto, e custa R${p * 0.95:.2f} reais')