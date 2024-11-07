### CONTAGEM DE PARES ###

for c in range(2, 51, 2):
    print('.', end = '')
    p = c % 2
    if p == 0:
        print(c, end = ' ')
print('Acabou!')