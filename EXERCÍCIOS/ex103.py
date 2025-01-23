### FICHA DO JOGADOR ###

def ficha(nome='<desconhecido>', gols=0):
    """
    -> Registra os dados de um jogador.
    :param nome: Nome do jogador (opcional, padrão: '<desconhecido>').
    :param gols: Número de gols (opcional, padrão: 0).
    :return: Exibe os dados do jogador formatados.
    """
    
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    
nome = input('Nome do Jogador: ').strip()
gols = input('Números de Gols: ').strip()

# Tratamento das entradas e chamada da função
if not gols.isdigit(): 
    gols = 0  # Define como 0 se for inválido
else:
    gols = int(gols)  # Converte para inteiro se for válido

if nome == '':
    ficha(gols=gols)  # Nome omitido
else:
    ficha(nome, gols)  # Nome e gols informados


### FICHA DO JOGADOR, CURSO EM VIDEO ###

# def ficha(jog='<desconhecido>', gol=0):
#     print(f'O jogador {jog} fez {gol} gols(s) no campeonato.')

# # Programa Pricipal
# n = str(input('Nome do Jogador: '))
# g = str(input('Número de Gols: '))
# if g.isnumeric():
#     g = int(g)
# else:
#     g = 0
# if n.strip() == '':
#     ficha(gol=g)
# else:
#     ficha(n, g)
