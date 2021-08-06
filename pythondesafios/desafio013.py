#Faça um algoritimo que leia o salário de um funcionario
#e mostre seu novo salário, com 15% de aumento.
s = float(input('Qual é o salário do funcionario? R$'))
print(f'O salário do funcionario com 15% de aumento será de R${s + (s * 15 / 100):.2f}')