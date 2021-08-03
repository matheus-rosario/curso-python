#========================================================#
#Faça um algoritimo que leia o salário de um funcionario #
#e mostre seu novo salário, com 15% de aumento.          #
#========================================================#
s = float(input('Digite seu salário atual? '))
print(f'Seu novo salário com 15% de aumento será de R$ {s + (s * 15 / 100)} reais.')