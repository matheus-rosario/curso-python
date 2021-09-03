#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
escolha = 'S'
número = []
contador = 0
while escolha == 'S':
  novo = int(input('Digite um número: '))
  escolha = str(input('Quer continuar? [S/N] ')).strip().upper()
  número.append(novo)
  contador += 1
  while escolha != 'S' and escolha != 'N':
    print('Opção Inválida!')
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()
print('FIM')
média = sum(número) / len(número)
print(f'Você digitou {contador} números e a média foi {média}')
print(f'O maior valor foi {max(número)} e o menor valor foi {min(número)}')