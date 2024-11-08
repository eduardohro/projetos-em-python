### JOGO DO PAR OU ÍMPAR ###

from random import randint

print('>'*40)
print('      VAMOS JOGAR PAR OU ÍMPAR?')
print('<'*40)

vezes = 0

while True:

    computador = randint(0, 10)
    valor = int(input('Diga um valor: '))
    escolha = str(input('Você quer Par ou Ímpar? [P/I]: ')).strip().upper()[0]

    soma = valor + computador
    resultado = 'PAR' if soma % 2 == 0 else 'ÍMPAR'
    
    print('-'*60)
    print(f'Você jogou {valor} e o computador jogou {computador}. No total de {soma} e deu {resultado}')
    print('-'*60)

    if (escolha == 'P' and resultado == 'PAR') or (escolha == 'I' and resultado == 'ÍMPAR'):
        print('Você \033[32mVENCEU!\033[m')
        print('Vamos jogar novamente...')
        vezes += 1
    else:
        print('Você \033[31mPERDEU!\033[m')
        break
    print('-='*30)

print(f'GAME OVER! Você venceu {vezes} vezes.\n')

### CURSO EM VIDEO ###

# from random import randint
# print('>'*40)
# print('      VAMOS JOGAR PAR OU ÍMPAR?')
# print('<'*40)
# v = 0
# while True:
#     jogador = int(input('Diga um valor: '))
#     computador = randint(0, 10)
#     total = jogador + computador
#     tipo = ' '
#     while tipo not in 'PI':
#         tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
#     print('-'*54)
#     print(f'Você jogou {jogador} e o computador {computador}. Total de {total} e ', end='')
#     print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
#     print('-'*54)
#     if tipo == 'P':
#         if total % 2 == 0:
#             print('VOCÊ VENCEU!')
#             v += 1
#         else:
#             print('VOCÊ PERDEU!')
#             break
#     if tipo == 'I':
#         if total % 2 == 1:
#             print('VOCÊ GANHOU!')
#             v += 1
#         else:
#             print('VOCÊ PERDEU!')
#             break
#     print('Vamos jogar novamente...')
# print(f'GAME OVER! Você venceu {v} vezes.\n')