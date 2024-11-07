### CÁLCULO DO FATORIAL ###

from math import factorial

n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
c = n

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1

print(f'{f}', end='')

### CURSO EM VIDEO ###

# n = int(input('Digite um número para calcular seu fatorial: '))
# c = n
# f = 1
# print('Calculando {}! = '.format(n), end='')
# while c > 0:
#     print('{}'.format(c), end='')
#     print(' x ' if c > 1 else ' = ', end='')
#     f *= c
#     c -= 1
# print('{}'.format(f), end='')