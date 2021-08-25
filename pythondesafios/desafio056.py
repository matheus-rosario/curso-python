#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre:
#a média de idade do grupo, qual é o nome do homem mais velho
#e quantas mulheres têm menos de 20 anos.
somaidade = 0
media = 0
maioridade = 0
nomevelho = ''
count = 0
for c in range(1, 5):
  print(f'=========={c}° Pessoa==========')
  nome = str(input('Nome: ')).strip()
  idade = int(input('Idade: '))
  sexo = str(input('Sexo [M/F]: ')).strip()
  somaidade += idade
  if c == 1 and sexo in 'Mm':
    maioridade = idade
    nomevelho = nome
  if sexo in 'Mn' and idade > maioridade:
    maioridade = idade
    nomevelho = nome
  if sexo in 'Ff' and idade < 20:
    count += 1
media = somaidade / 4
print(f'A media de idade é de {media} anos')
print(f'O homem mais velho é o {nomevelho}, ele tem {maioridade} anos.')
print(f'{count} mulheres tem menos de 20 anos.')