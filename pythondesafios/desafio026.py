#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip()
letra = frase.upper().count('A')
print(f'A letra A aparece {letra} vezes na frase')
primeira = frase.upper().find('A')
print(f'A primeira letra A aparece na posição {primeira + 1}')
ultima = frase.upper().rfind('A')
print(f'A última letra A aparece na posição {ultima + 1}')