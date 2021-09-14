#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
números = (int(input('Primeiro número: ')), int(input('Segundo número: ')), int(input('Terceiro número: ')), int(input('Quarto número: ')))
print(f'O número nove apareceu {números.count(9)} vezes')
if 3 in números:
  print(f'O valor 3 apareceu primeiramente na {números.index(3)+1}° posição')
else:
  print('O valor 3 não foi digitado')
print('Os números pares digitados foram: ', end='')
for n in números:
    if n % 2 == 0:
        print(n, end=' ')