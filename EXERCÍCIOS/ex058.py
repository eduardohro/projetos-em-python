### JOGO DA ADIVINHAÇÃO V.2.0 ###

from random import randint
from time import sleep # BIBLIOTECA DE TEMPO.

print('=' * 37)
print('\tJOGO DA ADIVINHAÇÃO 2')
print('=' * 37)

nome = str(input('Digite seu nome: '))
print('Carregando...')
sleep(1)

print('-'*12)
print(f'''Bem vindo(a) {nome}, esse é o JOGO DA ADIVINHAÇÃO 2!
Vou pensar em um número de 0 a 10 e você irá ter que adivinhar.
Está pronto(a)? Então vamos começar!''')
print('-'*12)

n = 1
n = int(input('Digite um número: '))
num = randint(0, 10)
tentativas = 1

while n != num:
    if n > num:
        print('É um número Menor!')
    else: 
        print('É um número Maior!') 

    n = int(input('Você \033[31mERROU!\033[m'
                   '\nTente novamente: '))
    
    tentativas += 1

print('Você \033[32mACERTOU!\033[m')
print(f'Para acertar o número {num} você precisou de {tentativas} tentativas!')


### CURSO EM VIDEO ###

# from random import randint
# computador = randint(0,10)
# print('Sou seu computador... Acabei de pensar um número entre 0 e 10.')
# print('Será que você consegue adivinhar qual foi?')
# acertou = False
# palpites = 0
# while not acertou:
#     jogador = int(input('Qual é seu palpite? '))
#     palpites += 1
#     if jogador == computador:
#         acertou = True
#     else:
#         if jogador < computador:
#             print('Mais... Tente mais uma vez:')
#         elif jogador > computador:
#             print('Menos... Tente mais uma vez: ')
# print('Acertou! Com {} tentativas. Parabéns!'.format(palpites))