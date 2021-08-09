#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários supériores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salário = float(input('Digite o salário atual R$: '))
if salário > 1250:
  salário = salário + (salário * 10 / 100)
  print(f'Seu salário com aumento será de R${salário:.2f}')
else:
  salário = salário + (salário * 15 / 100)
  print(f'Seu salário com aumento será de R${salário:.2f}')