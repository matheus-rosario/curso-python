#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de deconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros
preço = float(input('Digite o preço do produto: '))
print('Escolha a forma de pagamento:')
print('1 - À vista dinheiro/cheque \n2 - À vista no cartão \n3 - Em até 2x no cartão \n4 - 3x ou mais no cartão'.strip())
pagamento = int(input('Forma de pagamento: '))
if pagamento == 1:
  #print('À vista')
  print(f'Sua compra de R${preço:.2f} vai custar R${preço - (preço * 10 / 100):.2f}')
elif pagamento == 2:
  #print('À vista no cartão')
  print(f'Sua compra de R${preço:.2f} vai custar R${preço - (preço * 5 / 100):.2f} ')
elif pagamento == 3:
  #print('2x no cartão')
  print(f'Sua compra vai custar R${preço:.2f}')
elif pagamento == 4:
  #print('3x no cartão')
  preço = preço + (preço * 20 / 100)
  parcelas = int(input('Quantas parcelas? '))
  print(f'Sua compra será parcelada em {parcelas}x de R${preço / parcelas:.2f} COM JUROS \nSua compra vai custar R${preço:.2f}')
else:
  print('Opção Invalida')