### JOGO DA ADVINHAÇÃO V.1.0

from random import randint
from time import sleep # BIBLIOTECA DE TEMPO.

print('\n JOGO DA ADIVINHAÇÃO ')
print('-'*12)

nome = str(input('Digite seu nome: '))
print('Carregando...')
sleep(1)

print(f'Bem vindo(a) {nome}, esse é o jogo da adivinhação!'
      '\nSerá gerado um número de 0 a 5 e você irá ter que adivinhar.'
      '\nEstá pronto(a)?, então vamos começar!')
print('-'*12)

n = int(input('Digite um número: '))
print('Processando...')
sleep(2)

num = randint(0, 5)

if n == num:
    print('\033[32mParabéns, você acertou!\033[m')
else:
    print('\033[31mVocê errou!\033[m')
    print(f'O número era {num}, quem sabe na próxima!')