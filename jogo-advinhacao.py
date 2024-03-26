# O JOGO ABAIXO UTILIZA-SE DE BIBLIOTECAS RANDOM PARA ESCOLHER UM NÚMERO ALEATÓRIO
# E TIME PARA FAZER UM COM QUE DEMORE UM TEMPO PARA IMPRIMIR A RESPOSTA NO TERMINAL.
# ALÉM DISSO, O ESTRUTURA DE REPETIÇÃO WHILE PARA FAZER COM O USUÁRIO TENHA 
# VÁRIAS CHANCES ATÉ ACERTAR O NÚMERO, ACOMPANHADO DE UM CONTADOR QUE MOSTRARÁ 
# QUANTAS VEZES O USUÁRIO TEVE QUE TENTAR ATÉ ACERTAR O NÚMERO.

### JOGO DA ADVINHAÇÃO ###
from random import randint
from time import sleep # BIBLIOTECA DE TEMPO.
print('=' * 37)
print('\tJOGO DA ADIVINHAÇÃO')
print('=' * 37)
nome = str(input('Digite seu nome: '))
print('Carregando...')
sleep(1)
print('-'*12)
print('Bem vindo(a) {}, esse é o JOGO DA ADIVINHAÇÃO!'
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
print('Para acertar o número {} você precisou de {} tentativas!\n'.format(num, tentativas))