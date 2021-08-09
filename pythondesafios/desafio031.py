#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km
# e R$0.45 para viagens mais longas.
distancia = float(input('Qual a distância da viagem em Km? '))
if distancia <= 200:
  passagem = distancia * 0.50
  print(f'A passagem custa R${passagem:.2f}')
else:
  passagem = distancia * 0.45
  print(f'A passagem custa R${passagem:.2f}')