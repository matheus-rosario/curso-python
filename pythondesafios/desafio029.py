#Escreva um programa que leia a velocidade de um carro.
# Se ele ultapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa deve custar R$7.00 por cada Km acima do limite.
velocidade = float(input('Qual a velocidade do carro? Km: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
  print(f'Você foi multado em R${multa:.2f}')
else:
  print('Você está dirigindo dentro do limite, Parabéns!')