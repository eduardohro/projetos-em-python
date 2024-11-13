### JOGO DE DADOS EM PYTHON ###

from random import randint
from time import sleep

jogadores = []
jogador1 = {'nome': 'Eduardo'}
jogador2 = {'nome': 'Alice'}
jogador3 = {'nome': 'Carlos'}
jogador4 = {'nome': 'Isabela'}

jogadores.append(jogador1.copy())
jogadores.append(jogador2.copy())
jogadores.append(jogador3.copy())
jogadores.append(jogador4.copy())

print('Valores sorteados:')
for jogador in jogadores:
    jogador['num'] = randint(1, 6)
    sleep(1)
    print(f'   {jogador["nome"]:} tirou {jogador["num"]}.')

print('Ranking dos jogadores: ')
ranking = sorted(jogadores, key=lambda jogador: jogador['num'], reverse=True)
for i, j in enumerate(ranking):
    print(f'   {i+1}º lugar: {j["nome"]} com {j["num"]}')
    sleep(1)

### CURSO EM VIDEO ###

# from random import randint
# from time import sleep
# from operator import itemgetter # itemgetter seleciona com qual chave vai ser a referencia para ordenar a lista
# jogo = {'Eduardo': randint(1, 6),
#         'Alice': randint(1, 6),
#         'Carlos': randint(1, 6),
#         'Isabela': randint(1, 6),}
# ranking = list()
# print('Valores Sorteados:')
# for k, v in jogo.items():
#     print(f'{k} tirou {v} no dado.')
#     sleep(1)
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print('-=' * 30)
# print('  == RANKING DOS JOGADORES ==')
# for i, v in enumerate(ranking):
#     print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
#     sleep(1)