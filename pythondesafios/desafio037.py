#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual sera a base de conversão: 
#-1 para binário,
#-2 para octal e
#-3 para hexadecimal.
numero = int(input('Digite um número inteiro: '))
print('Qual será a base de conversão? ')
print('  1 - Binário \n  2 - Octal \n  3 - Hexadecimal' )
conversao = int(input('Base de conversão: '))
if conversao == 1: 
  print(f'O número {numero} convertido para binário é: {bin(numero)[2:]}')
elif conversao == 2:
  print(f'O número {numero} convertido para octal é: {oct(numero)[2:]}')
elif conversao == 3:
  print(f'O número {numero} convertido para hexadecimal é: {hex(numero)[2:]}')
else:
  print('Número Invalido')