#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
número = randint(0, 10)
print('Pensei em um número inteiro entre 0 e 10, tente adivinhar qual foi:')
palpite = int(input('Seu palpite: '))
tentativas = 1
while palpite != número:
  palpite = int(input('Errou! Tente outra vez: '))
  tentativas += 1
print(f'Acertou! Eu pensei no número {número}. \nVocê precisou de {tentativas} tentativas para acertar!')