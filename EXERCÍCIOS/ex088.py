### PALPITES PARA A MEGA SENA ###

from random import randint
from time import sleep

print('—–' * 20)
print(f'{"JOGA NA MEGA SENA":^40}')
print('—–' * 20)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))

sorteios = []

for i in range(jogos):
    c = []

    while len(c) < 6:
        num = randint(1, 60)
        if num not in c:
            c.append(num)

    c.sort()
    sorteios.append(c)

print(f'\n{" SORTEANDO {} JOGOS... ".format(jogos):=^40}')

for i, jogo in enumerate(sorteios, 1):
    print(f'Jogo {i}: {jogo}')
    sleep(1)

print('—–' * 20)
print(f'{" Boa sorte! ":=^40}')

### CURSO EM VIDEO ###

# from random import randint
# from time import sleep
# lista = []
# jogos = []
# print('-' * 30)
# print('       JOGA NA MEGA SENA         ')
# print('-' * 30)
# quant = int(input('Quantos jogos você quer que eu sorteie? '))
# tot = 1
# while tot <= quant:
#     cont = 0
#     while True:
#         num = randint(1, 60)
#         if num not in lista:
#             lista.append(num)
#             cont += 1
#         if cont >= 6:
#             break
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     tot += 1
# print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
# for i, l in enumerate(jogos):
#     print(f'Jogo {i+1}: {l}')
#     sleep(1)
# print('-=' * 5, '< BOA SORTE! >', '-=' * 5 )