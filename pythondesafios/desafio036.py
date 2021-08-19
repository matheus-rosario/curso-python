#Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode execer 30% do salário ou então o empréstimo será negado.
casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário: R$'))
anos = int(input('Digite a quantidade de anos: '))
mensal = casa / (anos * 12)
if mensal <= salario * 30 / 100:
  print(f'O seu emprestimo foi aprovado!')
else:
  print('O seu emprestimo foi recusado pois excede o valor de 30% do seu salário')