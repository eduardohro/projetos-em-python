### APRIMORANDO OS DICIONÁRIOS ###

jogador = dict()
jogadores = list()

while True:
    print('--' * 30)
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    gols = list()
    somagol = 0

    for p in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na {p}ª partida? ')))
    
    print('--' * 30)

    jogador['gols'] = gols
    
    for v in gols:
        somagol += v
    
    jogador['total'] = somagol
    jogadores.append(jogador.copy())

    cont = ' '
    while cont not in 'SsNn':
        cont = str(input('Quer continuar? [S/N]: '))
    if cont in 'Nn':
        break

print('-=' * 40)
print(f'{"COD"} {"NOME"} {"GOLS":>15} {"TOTAL":>20}')
print('--' * 30)
for pos, jogador in enumerate(jogadores):  
    # Converte a lista de gols para uma string com valores separados por vírgula
    gols_formatados = ', '.join(map(str, jogador["gols"]))
   
    print(f'{pos:>3} {jogador["nome"]:<15} {gols_formatados:<20} {jogador["total"]:<5}')
print('--' * 30)

while True:
    num = int(input('Mostrar dados de qual jogador? (999 interrompe): '))

    encontrado = False # Variável para controlar se o jogador foi encontrado

    for pos, jogador in enumerate(jogadores):
        if num == pos:
            print(f'-- LEVANTAMENTO DO JOGADOR {jogador["nome"]}:')
            for i, v in enumerate(jogador['gols']):
                print(f'   No {i + 1}º jogo fez {v} gols.')

            encontrado = True  # Marca como encontrado
            break # Sai do loop ao encontrar o jogador
    
    if num == 999:
        break  # Interrompe o loop se o usuário digitar 999

    if not encontrado:
        print(f'\033[31mERRO!\033[m Não existe jogador com código {num}! Tente novamente.')

    print('-' * 30)
print('<< VOLTE SEMPRE >>')

### CURSO EM VIDEO ###

# time = list()
# jogador = dict()
# partidas = list()
# while True:
#     jogador.clear()
#     jogador['nome'] = str(input('Nome do jogador: '))
#     tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
#     partidas.clear()
#     for c in range(0, tot):
#         partidas.append(int(input(f'  >> Quantos gols na partida {c+1}? ')))
#     jogador['gols'] = partidas[:]
#     jogador['total'] = sum(partidas)
#     time.append(jogador.copy())
#     while True:
#         resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
#         if resp in 'SN':
#             break
#         print('\033[31mERRO!\033[m Responda S ou N.')
#     if resp == 'N':
#         break
# print('-=' * 30)
# print('cod', end='')
# for i in jogador.keys():
#     print(f'{i:<15}', end='')
# print()
# print('-' * 40)
# for k, v in enumerate(time):
#     print(f'{k:>3} ', end='')
#     for d in v.values():
#         print(f'{str(d):<15}', end='')
#     print()
# print('-' * 40)
# while True:
#     busca = int(input('Mostra dados de qual jogador? (999 para parar): '))
#     if busca == 999:
#         break
#     if busca >= len(time):
#         print(f'\033[31mERRO!\033[m Não existe jogador com o código {busca}!')
#     else:
#         print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
#         for i, g in enumerate(time[busca]['gols']):
#             print(f'  => No jogo {i+1} fez {g} gols.')
#     print('-' * 40)
# print('<< VOLTE SEMPRE >>')