#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
maiores = homens = mulheres = 0
while True:
  print('-'*20)
  print('CADASTRE UMA PESSOA')
  print('-'*20)
  idade = int(input('Idade: '))
  if idade >= 18:
    maiores += 1
  sexo = str(input('Sexo [M/F]: ')).strip().upper()
  while sexo != 'M' and sexo != 'F':
    print('Opção Inválida!')
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
  if sexo == 'M':
    homens += 1
  if sexo == 'F' and idade < 20:
    mulheres += 1
  print('-'*20)
  escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()
  while escolha != 'S' and escolha != 'N':
    print('Opção Inválida!')
    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()
  if escolha == 'N':
    break
print('-'*20)
print('PROGRAMA FINALIZADO!')
print('-'*20)
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
print('-'*20)