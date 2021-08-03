#===========================================================#
#Faça um programa que leia a largura e altura de uma parede #
#em metros, calcule a sua área e a quantidade de tinta      #
#necessária para pintá-la, sabendo que cada litro de tinta, #
#pinta uma área de 2m².                                     #
#===========================================================#
n1 = float(input('Qual a altura da parede? '))
n2 = float(input('Qual o comprimento da parede? '))
area = n1 * n2
print(f'Você vai precisar de {area / 2:.2f} litros de tinta para pintar a sua parede de {area:.2f}m².')