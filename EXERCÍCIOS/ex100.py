### FUNÇÕES PARA SORTEAR E SOMAR ###

from random import randint
from time import sleep

def sorteia(valores):
    
    print('Sorteando 5 valores da lista: ', end='')
    for v in valores:
        print(f'{ v}', end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')

valores = [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)]

sorteia(valores)

def somaPar(valores):
    print(f'Entre os valores {valores}, somente ', end='')

    somapar = 0
    pares = []
    for v in valores:
        if v % 2 == 0:
            somapar += v
            pares.append(v)

    print(f'{pares} são pares')
    print(f'Somando eles temos {somapar}.')

somaPar(valores)


### FUNÇÕES PARA SORTEAR E SOMAR, CURSO EM VIDEO ###

# from random import randint
# from time import sleep

# def sorteia(lista):
#     print('Sorteando 5 valores da lista: ', end='')
#     for cont in range(0, 5):
#         n = randint(1, 10)
#         lista.append(n)
#         print(f'{n} ', end='', flush=True)
#         sleep(0.3)
#     print('Pronto!')

# def somaPar(lista):
#     soma = 0 
#     for valor in lista:
#         if valor % 2 == 0:
#             soma += valor
#     print(f'Somando os valores pares de {lista}, temos {soma}')

# números = list()
# sorteia(números)
# somaPar(números)
