### CADASTRO DE JOGADOR DE FUTEBOL ###

jogador = dict()
gols = []
somagol = 0

jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for p in range(1, partidas+1):
    gols.append(int(input(f'Quantos gols na {p}º partida? ')))

for v in gols:
    somagol += v

jogador['gols'] = gols
jogador['total'] = somagol

print('-=' * 30)
print(jogador)

print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for p in range(len(jogador['gols'])):
    print(f'  => Na {p+1}º partida, fez {jogador["gols"][p]} gols.')

print(f'Foi um total de {jogador["total"]} gols.')

### CURSO EM VIDEO ###

# jogador = dict()
# partidas = list()
# jogador['nome'] = str(input('Nome do Jogador: '))
# tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
# for c in range(0, tot):
#     partidas.append(int(input(f'  >> Quantos gols na partida {c}? ')))
# jogador['gols'] = partidas[:]
# jogador['total'] = sum(partidas)
# print('-+' * 30)
# print(jogador)
# print('-+' * 30)
# for k, v in jogador.items():
#     print(f'O campo {k} tem o valor {v}')
# print('-+' * 30)
# print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
# for i, v in enumerate(jogador['gols']):
#     print(f'  => Na partida {i}, fez {v} gols.')
# print(f'Foi um total de {jogador["total"]}')