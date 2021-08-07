#Um professor quer sortear um dos seus quatro alunos
#para apagar o quadro. Faça um programa que ajude ele,
#lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))
sorteado = choice([aluno1, aluno2, aluno3, aluno4])
print(f'O aluno sorteado foi: {sorteado}')