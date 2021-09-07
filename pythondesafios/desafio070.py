#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
mil = total = quantidade = preçobarato = 0
nomebarato = ''
while True:
  print('-'*20)
  print('LOJA SUPER BARATÃO')
  print('-'*20)
  nome = str(input('Nome do Produto: ')).strip()
  preço = float(input('Preço: R$'))
  if preço > 1000:
    mil += 1
  total += preço
  quantidade += 1
  if quantidade == 1:
    preçobarato = preço
    nomebarato = nome
  elif quantidade != 1 and preço < preçobarato:
    preçobarato = preço
    nomebarato = nome
  escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()
  while escolha != 'S' and escolha != 'N':
    print('Opção Inválida!')
    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()
  if escolha == 'N':
    break
print('-'*20)
print('PROGRAMA FINALIZADO!')
print('-'*20)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mil} produtos custando mais que R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R${preçobarato:.2f}')
print('-'*20)