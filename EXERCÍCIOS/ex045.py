### GAME: PEDRA PAPEL E TESOURA ###

from random import randint
from time import sleep

print('-+-' * 11)
print('\tJOGO DO JOKENPÔ')
print('-+-' * 11)

print('''\nFaça sua escolha: '
1 - PEDRA;
2 - PAPEL;
3 - TESOURA.''')
escolha = int(input(('\nEscolha a PAPEL, PEDRA OU TESOURA de acordo com a numeração: ')))

sorteado = randint(1, 3)
print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ...')

if escolha == 1 and sorteado == 2:
    print('\nO computador escolheu PAPEL e você PEDRA.'
          '\nEntão você \033[31mPERDEU!'
          '\n')
elif escolha == 1 and sorteado == 3:
    print('\nO computador escolheu TESOURA e você PEDRA.'
          '\nEntão você \033[32mGANHOU!'
          '\n')
elif escolha == 2 and sorteado == 1:
    print('\nO computador escolheu PEDRA e você PAPEL.'
          '\nEntão você \033[32mGANHOU!'
          '\n')
elif escolha == 2 and sorteado == 3:
    print('\nO computador escolheu TESOURA e você PAPEL.'
          '\nEntão você \033[31mPERDEU!'
          '\n')
elif escolha == 3 and sorteado == 1:
    print('\nO computador escolheu PEDRA e você TESOURA.'
          '\nEntão você \033[31mPERDEU!'
          '\n')
elif escolha == 3 and sorteado == 2: 
    print('\nO computador escolheu PAPEL e você TESOURA.'
          '\nEntão você \033[32mGANHOU!'
          '\n')
    
### CURSO EM VIDEO ###

# from random import randint
# itens = ('Pedra', 'Papel', 'Tesoura')
# computador = randint(0, 2)
# print('''Suas opções:
# [ 0 ] PEDRA
# [ 1 ] PAPEL
# [ 2 ] TESOURA''')
# jogador = int(input('Qual é a sua jogada? '))
# print('-+' * 11)
# print(f'Computador jogou {(itens[computador])}')
# print(f'Jogador jogou {(itens[jogador])}')
# print('-+' * 11)
# if computador == 0: # Computador jogou PEDRA
#     if jogador == 0:
#         print('EMPATE!')
#     elif jogador == 1:
#         print('JOGADOR VENCE!')
#     elif jogador == 2:
#         print('COMPUTADOR VENCE!')
#     else:
#         print('JOGADA INVÁLIDA!')
# elif computador == 1: # Computador jogou PAPEL
#     if jogador == 0:
#         print('COMPUTADOR VENCE!')
#     elif jogador == 1:
#         print('EMPATE!')
#     elif jogador == 2:
#         print('JOGADOR VENCE!')
#     else:
#         print('JOGADA INVÁLIDA!')
# elif computador == 2: # Computador jogou TESOURA
#     if jogador == 0:
#         print('JOGADOR VENCE!')
#     elif jogador == 1:
#         print('COMPUTADOR VENCE!')
#     elif jogador == 2:
#         print('EMPATE!')
#     else:
#         print('JOGADA INVÁLIDA!')
# print()