'''O mesmo professor do desafio anterior quer sortear
a ordem de apresentação de trabalho dos alunos.
Faça um programa que leia o nome dos quatro alunos
e mostre a ordem sorteada.'''
from random import shuffle
aluno1 = str(input('Nome do Primeiro Aluno: '))
aluno2 = str(input('Nome do Segundo Aluno: '))
aluno3 = str(input('Nome do Terceiro Aluno '))
aluno4 = str(input('Nome do Quarto Aluno: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print(f'A ordem e apresentação será: {alunos}')