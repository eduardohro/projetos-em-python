### JOGO DA ADVINHAÇÃO 2 ###
from random import randint
from time import sleep # BIBLIOTECA DE TEMPO.
print('=' * 37)
print('\tJOGO DA ADIVINHAÇÃO 2')
print('=' * 37)
nome = str(input('Digite seu nome: '))
print('Carregando...')
sleep(1)
print('-'*12)
print('Bem vindo(a) {}, esse é o JOGO DA ADIVINHAÇÃO 2!'
      '\nVou pensar em um número de 0 a 10 e você irá ter que adivinhar.'
      '\nEstá pronto(a)? Então vamos começar!'.format(nome))
print('-'*12)
n = 1
n = int(input('Digite um número: '))
num = randint(0, 10)
tentativas = 1
while n != num:
    n = int(input('Você \033[31mERROU!\033[m'
                   '\nTente novamente: '))
    tentativas += 1 
print('Você \033[32mACERTOU!\033[m')
print('Para acertar o número {} você precisou de {} tentativas!'.format(num, tentativas))